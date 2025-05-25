from django import forms
from .models import *
from datetime import date

from .models import * #\
    # TemplateModel, WorkTypeModel, VuzModel, TplFileModel, \
    # StyleModel, ParagraphModel, FontModel, FontModificationModel, FontTypefaceModel


class CategoryForm(forms.Form):
    """
    Login form
    Add class to form field Django ModelForm
    https://stackoverflow.com/questions/29716023/add-class-to-form-field-django-modelform
    """

                    # form_login.html
    template_name =  "form_node.html"
    
    # =========================
    
    wSelect = forms.Select(attrs={'placeholder': "", "class":"22",'data-issel':'1'})
    wMSelect = forms.CheckboxSelectMultiple(attrs={'placeholder': "", "class":"22",'data-issel':'1'})
    widgetNum = forms.NumberInput(attrs={'placeholder': ""})
    wRadio = forms.RadioSelect
    wCheck = forms.CheckboxInput
    wCheck = forms.CheckboxSelectMultiple

    # =========================

    _workTypeDt = Category.objects.all().order_by('id')
    id = forms.IntegerField(label="ID", required=False, initial=0,
        widget=forms.HiddenInput)

    # =========================

    parent = forms.ModelChoiceField(queryset = _workTypeDt, required=False, widget=wSelect,
                                    label="Категория",initial='')
    # categories = forms.ModelMultipleChoiceField(queryset = _workTypeDt, required=False,
    #                                 label="Категории",initial=1)
    
    # login_name = forms.CharField(label="Логин", max_length=100,
    #                             widget=forms.TextInput(attrs={'placeholder': "login"}))
    # login_pass = forms.CharField(label="Пароль", max_length=100,
    #                             widget=forms.TextInput(attrs={'placeholder': "password", 'type': "password"}))

    # categories = forms.ManyToManyField(Category, label='Категория')
    weight = forms.IntegerField(label='Вес')
    name = forms.CharField( max_length=64, help_text='', label='Название')
    key = forms.CharField( max_length=64, help_text='', label='Ключ')

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        # print('kwargs', kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            # visible.field.widget.attrs['placeholder'] = ''


# class NodeForm2(forms.ModelForm):

#     class Meta:
#         model = Node
#         # exclude = ['user']
