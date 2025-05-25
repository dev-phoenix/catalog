# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
# from .models import Book, Author, BookInstance, Genre
from .models import *
# from .models import \
#     TemplateModel, WorkTypeModel, VuzModel, TplFileModel, \
#     StyleModel, ParagraphModel, FontModel, FontModificationModel, FontTypefaceModel
# from .forms import UploadFileForm

from django.core.mail import send_mail
from .forms import LoginForm #, Templateform, DateSelectorWidget
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from catalog.lib import dump, printc
from django.conf import settings

# templatetags
# templatetags

messages = {}
def mess(mess, request, _type='success'):
    uid = request.user.id
    if not uid in messages:
        messages[uid] = []
    messages[uid].append({'type':_type, 'mess':mess})

def _404View(request):
    """
    404 page template
    """
    context = {
        'django': 'the web framework for perfectionists with deadlines',
        'home_link':'/',
        'home_title':'Home',
    }
    return render(request, '404.html', context=context)

def index(request):
    """View function for home page of site."""

    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login/")

    # Generate counts of some of the main objects
    # num_books = TemplateModel.objects.all().count()
    # num_instances = WorkTypeModel.objects.all().count()

    # Available books (status = 'a')
    # num_instances_available = WorkType.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    # num_authors = TplFileModel.objects.count()

    context = {
        'django': 'the web framework for perfectionists with deadlines',
        # 'num_books': num_books,
        # 'num_instances': num_instances,
        # 'num_instances_available': num_instances_available,
        # 'num_authors': num_authors,
        'home_link':'/',
        'home_title':'Home',
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'login.html', context=context)

def logoutView(request):
    logout(request)
    return HttpResponseRedirect("/login/")

def loginView(request):
    """View function for home page of site.
    https://docs.djangoproject.com/en/5.0/topics/forms/
    https://forum.djangoproject.com/t/form-template-name-issue-templatenotfound/11451/4
    Try placing that form template in your app/templates/common directory,
    where app is the app containing that form.

    authentication system
    https://docs.djangoproject.com/en/5.0/topics/auth/default/
    """

    mess = ''
    messClass = 'success'
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect("/")

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # rendered_form = form.render("form_login.html")
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            u = None
            user = None
            try:
                user = authenticate(username=form.cleaned_data['login_name'],
                                    password=form.cleaned_data['login_pass'])
                dump('user', user)
                u = User.objects.get(username=form.cleaned_data['login_name'])
                dump('u', u)
            except Exception as e:
                dump('user', e)
            dump('form.cleaned_data', form.cleaned_data)
            # redirect to a new URL:
            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                mess = 'Вы успешно залогинены'
                messClass = 'success'
                # return HttpResponseRedirect("/login/")
            else:
                # No backend authenticated the credentials
                mess = 'Не верные данные'
                messClass = 'warning'
                # return HttpResponseRedirect("/login/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()
        # rendered_form = form.render("form_login.html")

    # ***************
    # Generate counts of some of the main objects
    # num_books = TemplateModel.objects.all().count()
    # num_instances = WorkTypeModel.objects.all().count()

    # Available books (status = 'a')
    # num_instances_available = WorkType.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    # num_authors = TplFileModel.objects.count()

    context = {
        # "form": rendered_form,
        "form": form,
        "mess": mess,
        "messClass": messClass,
        'django': 'the web framework for perfectionists with deadlines',
        # 'num_books': num_books,
        # 'num_instances': num_instances,
        # 'num_instances_available': num_instances_available,
        # 'num_authors': num_authors,
        'home_link':'/',
        'home_title':'Home',
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'login.html', context=context)