# users/views.py
from django.urls import reverse_lazy,reverse
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required

from animals.models import Has_Spotted
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('index')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        form.save()

        username = self.request.POST['username']
        password = self.request.POST['password1']

        user = authenticate(username=username, password=password)
        login(self.request, user)

        return HttpResponseRedirect(reverse_lazy('index'))

@login_required(login_url='/users/login/')
def profile(request):
    spotted_animals = set()

    for spotted in Has_Spotted.objects.filter(user=request.user).select_related('animal'):
        # Without select_related(), this would make a database query for each
        # loop iteration in order to fetch the related animal for each entry.
        spotted_animals.add(spotted.animal)
    context = {'animals': spotted_animals}

    return render(request, 'users/profile.html', context)
