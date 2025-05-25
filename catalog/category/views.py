from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
# from .models import Book, Author, BookInstance, Genre
from .models import *
from node.models import *
# from .models import \
#     TemplateModel, WorkTypeModel, VuzModel, TplFileModel, \
#     StyleModel, ParagraphModel, FontModel, FontModificationModel, FontTypefaceModel
# from .forms import UploadFileForm

from django.core.mail import send_mail
from .forms import CategoryForm # LoginForm, Templateform, DateSelectorWidget
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from catalog.lib import dump, printc
from django.conf import settings
from django.urls import reverse


'''
add
edit
view
delete
list
find
filter

'''

messages = {}
def mess(mess, request, _type='success'):
    uid = request.user.id
    if not uid in messages:
        messages[uid] = []
    messages[uid].append({'type':_type, 'mess':mess})



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


def getData(id=0):
    '''
    Получить данные категории
    '''
    # dump('tplid', tplid, color='green')
    filesCou = 0
    data = {
        'id': id,
        'parent': None,
        'weight': 1,
        'name': '',
        'key': '',
    }
    if id==0:
        return data

    # =========================
    
    # if id > 0:
    #     filesCou = Category.objects.filter(id=int(id)).all().count()
    # data['filesCou'] =  filesCou

    # =========================
    
    # tpl = TemplateModel(id=tplid)
    item = Category.objects.filter(id=id).first()
    # print('Category')
    # dump('cat methods', dir(item))
    if item:
        data['id'] = item.id
        data['parent'] = item.parent
        data['weight'] = item.weight
        data['name'] = item.name
        data['key'] = item.key

    # =========================
    # printc('getTemplate data', data, color='green')

    return data

def update(request,id,form):
    '''
    обновление или создание категории
    '''
    # dump( 'request.POST', dict(request.POST) )
    # print( 'Templateform', dict(form.cleaned_data) )
    # dump( 'request.FILES', dict(request.FILES) )

    data = form.cleaned_data
    id = data['id']
    created = False

    item = Category.objects.filter(id=id).first()
    if not item:
        item = Category()
        created = True

    item.parent = data['parent']
    item.weight = data['weight']
    item.name = data['name']
    item.key = data['key']
    item.save()
    id = item.id

    if created:
        mess(f'добавлена категория с id:{item.id}', request)
    else:
        mess(f'изменёна категория с id:{item.id}', request)
    return item.id


def add(request, id=0):
    '''
    создание или изменение
    '''

    if not request.user.is_authenticated:        return HttpResponseRedirect("/login/")
    uid = request.user.id
    if not uid in messages:
        messages[uid] = []

    # mess(id,request,'success')
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        # dump( 'request.POST', request.POST )
        if form.is_valid():
            id = update(request,id,form)
            # templateform.cleaned_data['tplid'] = tplid
            form.id = id
            return HttpResponseRedirect(reverse('editCategory', args=[id]))
        # Сategory
        # Category
        else:
            mess('have some error', request)
    else:
        data = getData(id)
        # dump('cat initial data', ())
        # print('cat initial data', data)
        form = CategoryForm(initial=data)
        # print('cat form', form)
    # form = CategoryForm()
    context = {
        'messages': messages[uid],
        "Nodeform": form,
        # "form": rendered_form,
    }
    messages[uid] = []
    return render(request, 'nodeAdd.html', context=context)


def edit(request, id=0):
    return add(request, id)


def view(request):
    context = {
        # "form": rendered_form,
    }
    return render(request, 'login.html', context=context)


def delete(request):
    context = {
        # "form": rendered_form,
    }
    return render(request, 'login.html', context=context)


def items(request,page=1,limit=100):
    """список шаблонов"""
    tpls_cou = Category.objects.all().count()
    tplfrom = int(page-1) * int(limit)
    tpls = Category.objects.all().order_by('-id')[tplfrom:tplfrom+int(limit)] 
    filesCou = {}
    tlist = []
    for tpl in tpls:
        id = tpl.id
        # fcou = Category.objects.filter(parent__id=id).all().count()
        # fcou = Node.objects.filter(categories__id=id).all().count()
        fcou = tpl.node_set.count()
        filesCou[id] = fcou
        tlist.append( {'tpl':tpl,"files":fcou} )

    pageCou = tpls_cou//limit
    if tpls_cou%limit:
        pageCou +=1
    # pageCou *=10
    pages = [(p, p) for p in range(1,pageCou+1)]

    pagePrevDis = False
    pageNextDis = False
    if page <= 1: pagePrevDis = True
    if page >= pageCou: pageNextDis = True
    pagePrev = page - 1
    pageNext = page + 1
    if pagePrev < 1: pagePrev = 1
    if pageNext > pageCou: pageNext = pageCou

    sli = 5
    if page > sli and page < pageCou - sli: pages = pages[page - sli - 1:]
    # pages = pages[:sli*2 + 1:]
    if page < pageCou - sli : pages = pages[:sli*2 + 1:]
    else: pages = pages[-(sli*2+1)::]


    pagename = 'Список категорий'
    context = {
        'pagename': pagename,
        'action': '/tplnew/',

        'pages': pages,
        'pagePrev': pagePrev,
        'pagePrevDis': pagePrevDis,
        'pageNext': pageNext,
        'pageNextDis': pageNextDis,
        'limit': limit,
        'currentPage': page,
        'pageCou': pageCou,
        'sli': sli,

        # 'tpls' = tlist,
        'tpls_cou': tpls_cou,
        'tplsList': tlist,
        'filesCou': filesCou,
    }
    return render(request, 'categories-list.html', context=context)


def findItems(request):
    context = {
        # "form": rendered_form,
    }
    return render(request, 'login.html', context=context)


def filterItems(request):
    context = {
        # "form": rendered_form,
    }
    return render(request, 'login.html', context=context)
