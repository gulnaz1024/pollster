from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField() # Required is True in default. So i keep it default

#     class Meta:
#         model = User # Whenever the form is validate it is going to create a new user
#         fields = ['username', 'email', 'password1', 'password2']
    
#     def save(self, commit=True):
#         user=super(UserRegisterForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user


# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()  # This For Additional Field

#     class Meta:
#         model = User
#         fields = ['username', 'email']
        

