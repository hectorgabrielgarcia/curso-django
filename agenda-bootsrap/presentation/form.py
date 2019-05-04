from django import forms
from data import models

class projectform(forms.ModelForm):
    class Meta:
        model = models.contactos
        fields = ('nombre','segundonombre','apellidomaterno','apelludopaterno','telcasa','celular','email','twitter')