from django import forms
from allauth.account.forms import SignupForm


class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='first_name')
    last_name = forms.CharField(max_length=30, label='last_name')
    address = forms.CharField(max_length=30, label='address', required=False)
    tel = forms.CharField(max_length=30, label='tel', required=False)


class SignupUserForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='first_name')
    last_name = forms.CharField(max_length=30, label='last_name')

    def save(self, request):
        user = super(SignupUserForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

    # print(vars(first_name))

