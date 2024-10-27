from django.contrib.auth.forms import UserCreationForm
from django import forms
from authentication.models import UserProfile
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    user_type = forms.ChoiceField(
        choices = (("admin", "Admin"), ("customer", "Customer")),
        label="Choose your user type:",
        required=True
    )
    email = forms.EmailField(label = "Email", required=True)
    name = forms.CharField(label = "Name", required=True)

    class Meta:
        model = User
        fields = ("user_type", "username", "name","email","password1", "password2")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        if commit:
            user.save()
        UserProfile.objects.create(
            user = user,
            full_name = self.cleaned_data["full_name"],
            user_type = self.cleaned_data["user_type"]
        )
        return user