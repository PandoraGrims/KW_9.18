from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.models import User


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username',
                  'password1',
                  'password2',
                  'first_name',
                  'phone']


class UserChangeForm(forms.ModelForm):
    phone = forms.CharField(label='Телефон', required=False)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'phone']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Email',
            'phone': 'Телефон'
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone:
            return phone

        if not phone.startswith('+996') or len(phone) != 13 or not phone[4:].replace(' ', '').isdigit():
            raise forms.ValidationError('Неправильный формат номера телефона. Используйте формат +996 XXX XXX XXX')
        return phone
