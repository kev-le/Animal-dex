# users/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

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
