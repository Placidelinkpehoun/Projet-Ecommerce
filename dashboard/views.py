from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit, Categories
from front.models import Commande, Commande_Produit
from django.contrib.auth.models import User
from .forms import Add_Produit_Form, Add_Categorie_Form
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

def is_admin(user):
    return user.is_superuser

def login_admin(request):
    if request.user.is_authenticated:
        user = request.user
        if user.is_superuser:
            return True
        else:
            return render(request, 'front/index.html', {})
    else:
        return render(request, 'front/login.html', {})

#@login_required(login_url='login_admin')
@user_passes_test(is_admin)
def index_dash(request):
    user = request.user
    users = User.objects.get(username=user.username)
    return render(request, 'dashboard/index_dashboard.html', {'users':users})



def login_dashboard(request):
    return render(request, 'dashboard/login.html')

#@login_required(login_url='login_admin')
@user_passes_test(is_admin)
def logout_dashboard(request):
    logout(request)
    return render(request, 'front/login.html', {})

def sign_up(request):
    return render(request, 'dashboard/sign-up.html')

#@login_required(login_url='login_admin')
@user_passes_test(is_admin)
def list_page(request):
    return render(request, 'dashboard/list-page.html')

#@login_required(login_url='login_admin')
@user_passes_test(is_admin)
def states(request):
    return render(request, 'dashboard/states.html')

#@login_required(login_url='login_admin')
@user_passes_test(is_admin)
def settings(request):
    user = request.user
    users = User.objects.get(username=user.username)
    return render(request, 'dashboard/setting.html', {'users':users})

#@login_required(login_url='login_admin')
@user_passes_test(is_admin)
def report(request):
    return render(request, 'dashboard/report.html')

@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def product_detail_1(request):
    return render(request, 'dashboard/product-detail-1.html')

@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def product_detail_2(request):
    return render(request, 'dashboard/product-detail-2.html')

@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def product_detail_3(request):
    return render(request, 'dashboard/product-detail-3.html')

@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def oder_tracking(request):
    return render(request, 'dashboard/oder-tracking.html')

@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def oder_list(request):
    return render(request, 'dashboard/oder-list.html')

@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def oder_details(request):
    return render(request, 'dashboard/oder-detail.html')

@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def new_page(request):
    return render(request, 'dashboard/new-page.html')


@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def new_category(request):
    user = request.user
    users = User.objects.get(username=user.username)
    if request.method == 'POST':
        add_categorie_form= Add_Categorie_Form(request.POST, request.FILES)
        if add_categorie_form.is_valid():
            add_categorie_form.save()
            return redirect('category_list')
        else:
            return render(request, 'dashboard/new-category.html', {'add_categorie_form': add_categorie_form})
    else:
        add_categorie_form = Add_Categorie_Form() 
    return render(request, 'dashboard/new-category.html', {'add_categorie_form': add_categorie_form, 'users':users})


@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def home_menu_icon_hover(request):
    user = request.user
    users = User.objects.get(username=user.username)
    return render(request, 'dashboard/home-menu-icon-hover.html', {'users': users})


@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def home_menu_icon_default(request):
    user = request.user
    users = User.objects.get(username=user.username)
    return render(request, 'dashboard/home-menu-icon-default.html', {'users': users})


@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def home_boxed(request):
    user = request.user
    users = User.objects.get(username=user.username)
    return render(request, 'dashboard/home-boxed.html', {'users' : users})


@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def home_4(request):
    user = request.user
    users = User.objects.get(username=user.username)
    return render(request, 'dashboard/home-4.html', {'users': users})


@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def home_3(request):
    user = request.user
    users = User.objects.get(username=user.username)
    return render(request, 'dashboard/home-3.html', {'users':users})


@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def home_2(request):
    user = request.user
    users = User.objects.get(username=user.username)
    produits = Produit.objects.all()
    return render(request, 'dashboard/home-2.html', {'produits': produits, 'users': user})


'''def header_dash(request):
    user = request.user
    users = User.objects.get(username=user.username)
    context = {
        'users' : users
    }
    return render(request, 'dashboard/header_dashboard.html', context)'''

@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def gallery(request):
    return render(request, 'dashboard/gallery.html')


@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def edit_page(request):
    return render(request, 'dashboard/edit-page.html')


@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def create_role(request):
    return render(request, 'dashboard/create-role.html')


@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def countries(request):
    return render(request, 'dashboard/countries.html')


@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def components(request):
    return render(request, 'dashboard/components.html')


@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def cities(request):
    return render(request, 'dashboard/cities.html')


@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def attributes(request):
    return render(request, 'dashboard/attributes.html')


@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def all_user(request):
    return render(request, 'dashboard/all-user.html')


@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def all_roles(request):
    return render(request, 'dashboard/all-roles.html')

@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def add_product(request):
    user = request.user
    users = User.objects.get(username=user.username)
    if request.method == 'POST':
        add_produit_form = Add_Produit_Form(request.POST, request.FILES)
        if add_produit_form.is_valid():
            add_produit_form.save()
            return redirect('product_list')
        else:
            return render(request, 'dashboard/add-product.html', {'add_produit_form': add_produit_form})
    else:
        add_produit_form = Add_Produit_Form() 
        return render(request, 'dashboard/add-product.html', {'add_produit_form': add_produit_form, 'users': users})
    

def delete_produit_dash(request, id_categorie):
    produit = get_object_or_404(Categories, id_categorie)
    produit.delete()
    return redirect('category_list')

@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def add_new_user(request):
    return render(request, 'dashboard/add-new-user.html')

@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def add_attributes(request):
    return render(request, 'dashboard/add-attributes.html')

@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def product_list(request):
    products = Produit.objects.all()  
    return render(request, 'dashboard/product-list.html', {'products': products})

@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def category_list(request):
    categories = Categories.objects.all()
    return render(request, 'dashboard/category-list.html', {'categories': categories})

@user_passes_test(is_admin)
#@login_required(login_url='login_admin')
def add_category(request):
    if request.method == 'POST':
        category_name = request.POST.get('name')
        #icon_file = request.FILES.get('filename')
        '''if icon_file:
            fs = FileSystemStorage()
            filename = fs.save(icon_file.name, icon_file)'''

        new_category = Categories.objects.create(name=category_name, )
        new_category.save()
        return redirect('category_list')
    
    else:
         return render(request, 'dashboard/new-category.html')