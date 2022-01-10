from django import forms


class SignIn(forms.Form):
    email = forms.EmailField(max_length=155,required=True,label='Email')
    password = forms.CharField(max_length=512,widget=forms.PasswordInput,label='Password')


class StudentSignIn(forms.Form):
    username = forms.CharField(max_length=255, required=True, label='Username')
    password = forms.CharField(max_length=512, required=True, label='Password', widget=forms.PasswordInput)


class SignUp(forms.Form):
    name = forms.CharField(max_length=255, min_length=3, required=True, label='Name')
    email = forms.EmailField(max_length=155, required=True,label='Email')
    password1 = forms.CharField(max_length=512,widget=forms.PasswordInput, label='Password', required=True)
    password2 = forms.CharField(max_length=512, widget=forms.PasswordInput, label='Confirm Password', required=True)


class OTPForm(forms.Form):
    otp = forms.CharField(min_length=6,max_length=6,label='Verify One Time Password ')


class StudentRegister(forms.Form):
    first_name = forms.CharField(max_length=512, required=True, label='First Name ')
    last_name = forms.CharField(max_length=512, label='Last Name ')
    email = forms.EmailField(max_length=512, required=True, label='Email')
    phone = forms.IntegerField(label='Phone Number',)
    password1 = forms.CharField(max_length=512, widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(max_length=512, widget=forms.PasswordInput, label='Confirm Password')


class CompleteSetup(forms.Form):
    name = forms.CharField(max_length=255, min_length=3, required=True, label='Name')
    phone = forms.CharField(max_length=13, label='Phone Number', required=False)
    bio = forms.CharField(max_length=155, label='Bio', required=False)
    address = forms.CharField(max_length=255, label='Place', required=False)
    profile_pic = forms.ImageField(required=False)

