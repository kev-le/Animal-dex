from django import forms


class create_pet_form(forms.Form):
    """Form for creating new pets"""
    pet_name = forms.CharField(required=True)
    pet_bio = forms.CharField(required=False)
    animal_breed = forms.IntegerField(required=True)
    animal_type = forms.CharField(required=True)
    pet_image = forms.ImageField(required=True)
