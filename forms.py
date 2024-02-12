from django import forms

# def validate_phone_number(value):
#         pattern = r'^\+[0-9]+(?:[0-9] ?)*$'
#         if not re.match(pattern, value):
#             raise ValidationError("Invalid phone number format.")


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=11)
    upload_image = forms.ImageField()
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class EditProfile(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    full_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    login_date = forms.DateField()
    upload_image = forms.ImageField()


class EditPassword(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
