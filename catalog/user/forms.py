from django import forms
from .models import *
from datetime import date

from .models import * #\
    # TemplateModel, WorkTypeModel, VuzModel, TplFileModel, \
    # StyleModel, ParagraphModel, FontModel, FontModificationModel, FontTypefaceModel


class LoginForm(forms.Form):
    """
    Login form
    Add class to form field Django ModelForm
    https://stackoverflow.com/questions/29716023/add-class-to-form-field-django-modelform
    """

                    # form_login.html
    template_name =  "form_login.html"
    login_name = forms.CharField(label="Логин", max_length=100,
                                widget=forms.TextInput(attrs={'placeholder': "login"}))
    login_pass = forms.CharField(label="Пароль", max_length=100,
                                widget=forms.TextInput(attrs={'placeholder': "password", 'type': "password"}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            # visible.field.widget.attrs['placeholder'] = ''


