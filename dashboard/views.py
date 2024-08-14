from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Produit, Categories

# Create your views here.

def index_dash(request):
    return render(request, 'dashboard/index_dashboard.html')

def login(request):
    return render(request, 'dashboard/login.html')

def sign_up(request):
    return render(request, 'dashboard/sign-up.html')

def list_page(request):
    return render(request, 'dashboard/list-page.html')

def states(request):
    return render(request, 'dashboard/states.html')

def settings(request):
    return render(request, 'dashboard/setting.html')

def report(request):
    return render(request, 'dashboard/report.html')

def product_detail_1(request):
    return render(request, 'dashboard/product-detail-1.html')

def product_detail_2(request):
    return render(request, 'dashboard/product-detail-2.html')

def product_detail_3(request):
    return render(request, 'dashboard/product-detail-3.html')

def oder_tracking(request):
    return render(request, 'dashboard/oder-tracking.html')

def oder_list(request):
    return render(request, 'dashboard/oder-list.html')

def oder_details(request):
    return render(request, 'dashboard/oder-detail.html')

def new_page(request):
    return render(request, 'dashboard/new-page.html')

def new_category(request):
    return render(request, 'dashboard/new-category.html')

def home_menu_icon_hover(request):
    return render(request, 'dashboard/home-menu-icon-hover.html')

def home_menu_icon_default(request):
    return render(request, 'dashboard/home-menu-icon-default.html')

def home_boxed(request):
    return render(request, 'dashboard/home-boxed.html')

def home_4(request):
    return render(request, 'dashboard/home-4.html')

def home_3(request):
    return render(request, 'dashboard/home-3.html')

def home_2(request):
    return render(request, 'dashboard/home-2.html')

def gallery(request):
    return render(request, 'dashboard/gallery.html')

def edit_page(request):
    return render(request, 'dashboard/edit-page.html')

def create_role(request):
    return render(request, 'dashboard/create-role.html')

def countries(request):
    return render(request, 'dashboard/countries.html')

def components(request):
    return render(request, 'dashboard/components.html')

def cities(request):
    return render(request, 'dashboard/cities.html')

def attributes(request):
    return render(request, 'dashboard/attributes.html')

def all_user(request):
    return render(request, 'dashboard/all-user.html')

def all_roles(request):
    return render(request, 'dashboard/all-roles.html')

def add_product(request):
    return render(request, 'dashboard/add-product.html')

def add_new_user(request):
    return render(request, 'dashboard/add-new-user.html')

def add_attributes(request):
    return render(request, 'dashboard/add-attributes.html')

def product_list(request):
    products = Produit.objects.all()  
    return render(request, 'dashboard/product-list.html', {'products': products})


def category_list(request):
    categories = Categories.objects.all()
    return render(request, 'dashboard/category-list.html', {'categories': categories})


def add_category(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        category_name = request.POST.get('name')
        #icon_file = request.FILES.get('filename')

        # Si un fichier est téléchargé, sauvegarder ce fichier
        '''if icon_file:
            fs = FileSystemStorage()
            filename = fs.save(icon_file.name, icon_file)'''

        # Créer une nouvelle instance de Categories
        new_category = Categories.objects.create(name=category_name, )

        # Sauvegarder la nouvelle catégorie dans la base de données
        new_category.save()

        # Rediriger vers la liste des catégories ou vers une autre page après la soumission
        return redirect('category_list')  # Assurez-vous d'avoir une URL avec ce nom
    
    else:
         return render(request, 'dashboard/new-category.html')