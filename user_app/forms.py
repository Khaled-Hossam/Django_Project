from django import forms
from django.contrib.auth.models import User
from user_app.models import UserProfileInfo
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
# from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class UserForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ("first_name","last_name","username","password","email",)
    
    # def __init__(self, *args, **kwargs):
    #     helper = FormHelper()
    #     super(UserForm, self).__init__(*args, **kwargs)
    #     helper.label_class = 'col-sm-2'
    #     helper.field_class = 'col-sm-8'
    #     helper.layout = Layout('first_name','last_name','username','password','email',)

class UserUpdateInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_picture',)

    # def __init__(self, *args, **kwargs):
    #     helper = FormHelper()
    #     super(UserUpdateInfoForm, self).__init__(*args, **kwargs)
    #     helper.label_class = 'col-sm-2'
    #     helper.field_class = 'col-sm-8 form-control-file'
    #     helper.layout = Layout('profile_picture',)

class UserProfileUpdate(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)

    class Meta():
        model = User
        fields = ("first_name","last_name","email",)
    
    # def __init__(self, *args, **kwargs):
    #     helper = FormHelper()
    #     super(UserProfileUpdate, self).__init__(*args, **kwargs)
    #     helper.label_class = 'col-4 col-form-label'
    #     helper.field_class = 'form-control here'
    #     helper.layout = Layout('first_name', 'last_name', 'email',)

class UserProfileInfoUpdate(forms.ModelForm):
    profile_picture = forms.ImageField(required=False)
    class Meta():
            model = UserProfileInfo
            fields = ('profile_picture',)

    # def __init__(self, *args, **kwargs):
    #     helper = FormHelper()
    #     super(UserProfileInfoUpdate, self).__init__(*args, **kwargs)
    #     helper.label_class = 'col-4 col-form-label'
    #     helper.field_class = 'form-control here'
    #     helper.layout = Layout('profile_picture',)

        
