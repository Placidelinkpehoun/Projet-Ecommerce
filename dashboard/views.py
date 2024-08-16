from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Produit, Categories
from front.models import Commande, Commande_Produit
from .forms import Add_Produit_Form, Add_Categorie_Form
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_admin(request):
    if request.user.is_authenticated:
        user = request.user
        if user.is_superuser:
            return True
        else:
            return render(request, 'front/index.html', {})
    else:
        return render(request, 'front/login.html', {})

@login_required(login_url='login_admin')
def index_dash(request):
    return render(request, 'dashboard/index_dashboard.html')



def login_dashboard(request):
    return render(request, 'dashboard/login.html')

@login_required(login_url='login_admin')
def logout_dashboard(request):
    logout(request)
    return render(request, 'front/login.html', {})

def sign_up(request):
    return render(request, 'dashboard/sign-up.html')

@login_required(login_url='login_admin')
def list_page(request):
    return render(request, 'dashboard/list-page.html')

@login_required(login_url='login_admin')
def states(request):
    return render(request, 'dashboard/states.html')

@login_required(login_url='login_admin')
def settings(request):
    return render(request, 'dashboard/setting.html')

@login_required(login_url='login_admin')
def report(request):
    return render(request, 'dashboard/report.html')

@login_required(login_url='login_admin')
def product_detail_1(request):
    return render(request, 'dashboard/product-detail-1.html')

@login_required(login_url='login_admin')
def product_detail_2(request):
    return render(request, 'dashboard/product-detail-2.html')

@login_required(login_url='login_admin')
def product_detail_3(request):
    return render(request, 'dashboard/product-detail-3.html')

@login_required(login_url='login_admin')
def oder_tracking(request):
    return render(request, 'dashboard/oder-tracking.html')

@login_required(login_url='login_admin')
def oder_list(request):
    return render(request, 'dashboard/oder-list.html')

@login_required(login_url='login_admin')
def oder_details(request):
    return render(request, 'dashboard/oder-detail.html')

@login_required(login_url='login_admin')
def new_page(request):
    return render(request, 'dashboard/new-page.html')

@login_required(login_url='login_admin')
def new_category(request):
    if request.method == 'POST':
        add_categorie_form= Add_Categorie_Form(request.POST, request.FILES)
        if add_categorie_form.is_valid():
            add_categorie_form.save()
            return redirect('category_list')
        else:
            return render(request, 'dashboard/new-category.html', {'add_categorie_form': add_categorie_form})
    else:
        add_categorie_form = Add_Categorie_Form() 
    return render(request, 'dashboard/new-category.html', {'add_categorie_form': add_categorie_form})

@login_required(login_url='login_admin')
def home_menu_icon_hover(request):
    return render(request, 'dashboard/home-menu-icon-hover.html')

@login_required(login_url='login_admin')
def home_menu_icon_default(request):
    return render(request, 'dashboard/home-menu-icon-default.html')

@login_required(login_url='login_admin')
def home_boxed(request):
    return render(request, 'dashboard/home-boxed.html')

@login_required(login_url='login_admin')
def home_4(request):
    return render(request, 'dashboard/home-4.html')

@login_required(login_url='login_admin')
def home_3(request):
    return render(request, 'dashboard/home-3.html')

@login_required(login_url='login_admin')
def home_2(request):
    produits = Produit.objects.all()
    return render(request, 'dashboard/home-2.html', {'produits': produits})

@login_required(login_url='login_admin')
def gallery(request):
    return render(request, 'dashboard/gallery.html')

@login_required(login_url='login_admin')
def edit_page(request):
    return render(request, 'dashboard/edit-page.html')

@login_required(login_url='login_admin')
def create_role(request):
    return render(request, 'dashboard/create-role.html')

@login_required(login_url='login_admin')
def countries(request):
    return render(request, 'dashboard/countries.html')

@login_required(login_url='login_admin')
def components(request):
    return render(request, 'dashboard/components.html')

@login_required(login_url='login_admin')
def cities(request):
    return render(request, 'dashboard/cities.html')

@login_required(login_url='login_admin')
def attributes(request):
    return render(request, 'dashboard/attributes.html')

@login_required(login_url='login_admin')
def all_user(request):
    return render(request, 'dashboard/all-user.html')

@login_required(login_url='login_admin')
def all_roles(request):
    return render(request, 'dashboard/all-roles.html')

@login_required(login_url='login_admin')
def add_product(request):
    if request.method == 'POST':
        add_produit_form = Add_Produit_Form(request.POST, request.FILES)
        if add_produit_form.is_valid():
            add_produit_form.save()
            return redirect('product_list')
        else:
            return render(request, 'dashboard/add-product.html', {'add_produit_form': add_produit_form})
    else:
        add_produit_form = Add_Produit_Form() 
        return render(request, 'dashboard/add-product.html', {'add_produit_form': add_produit_form})

@login_required(login_url='login_admin')
def add_new_user(request):
    return render(request, 'dashboard/add-new-user.html')

@login_required(login_url='login_admin')
def add_attributes(request):
    return render(request, 'dashboard/add-attributes.html')

@login_required(login_url='login_admin')
def product_list(request):
    products = Produit.objects.all()  
    return render(request, 'dashboard/product-list.html', {'products': products})

@login_required(login_url='login_admin')
def category_list(request):
    categories = Categories.objects.all()
    return render(request, 'dashboard/category-list.html', {'categories': categories})

@login_required(login_url='login_admin')
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