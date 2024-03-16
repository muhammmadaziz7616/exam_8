from django import forms
from django.core.exceptions import ValidationError

from apps.models import Product


class EmailForm(forms.ModelForm):
    def clean_email(self):
        email = self.data.get('email')
        if Product.objects.filter(email=email):
            raise ValidationError('Email already exists !')
        return email

    class Meta:
        model = Product
        fields = ('email',)
