from django.shortcuts import render, get_object_or_404, redirect
from dashboard.models import Categories, Produit, Message
from .models import Commande, Commande_Produit

def home(request):
    return render(request, 'front/home.html')


def index(request):
    categories = Categories.objects.all()
    produits = Produit.objects.all()
    #commande = get_object_or_404(Commande_Produit, produits_id=produits.id_produit)
    return render(request, 'front/index.html', {'categories': categories, 'produits': produits})


def index_two(request):
    return render(request, 'front/index-two.html')


def index_three(request):
    return render(request, 'front/index-three.html')


def index_four(request):
    return render(request, 'front/index-four.html')


def index_five(request):
    return render(request, 'front/index-five.html')


def invoice(request):
    return render(request, 'front/invoice.html')


def login(request):
    return render(request, 'front/login.html')


def privacy_policy(request):
    return render(request, 'front/privacy-policy.html')


def register(request):
    return render(request, 'front/register.html')


def shop_compare(request):
    return render(request, 'front/shop-compare.html')


def shop_details(request):
    return render(request, 'front/shop-details.html')


def shop_details_2(request):
    return render(request, 'front/shop-details-2.html')


def shop_details_4(request):
    return render(request, 'front/shop-details-4.html')


def shop_details_affiliats(request):
    return render(request, 'front/shop-details-affiliats.html')


def shop_details_group(request):
    return render(request, 'front/shop-details-group.html')


def details_right_sidebar(request):
    return render(request, 'front/shop-details-right-sidebar.html')


def shop_details_variable(request):
    return render(request, 'front/shop-details-variable.html')


def shop_grid_sidebar(request, id_categorie):
    categorie_id = get_object_or_404(Categories, id_categorie=id_categorie)
    produits = Produit.objects.filter(categorie_id=categorie_id.id_categorie)
    return render(request, 'front/shop-grid-sidebar.html', {'categorie_id': categorie_id, 'produits': produits})


def shop_grid_top_filter(request):
    return render(request, 'front/shop-grid-top-filter.html')


def shop_list_sidebar(request):
    return render(request, 'front/shop-list-sidebar.html')


def shop_list_top_filter(request):
    return render(request, 'front/shop-list-top-filter.html')


def store(request):
    return render(request, 'front/store.html')


def terms_condition(request):
    return render(request, 'front/terms-condition.html')


def this_params(request):
    return render(request, 'front/this.params.html')


def trackorder(request):
    return render(request, 'front/trackorder.html')


def vendor_details(request):
    return render(request, 'front/vendor-details.html')


def vendor_details_grid(request):
    return render(request, 'front/vendor-details.html')


def vendor_list(request):
    return render(request, 'front/vendor-list.html')


def wishlist(request):
    return render(request, 'front/wishlist.html')


def faq(request):
    return render(request, 'front/faq.html')


def e(request):
    return render(request, 'front/e.html')


def cookies_policy(request):
    return render(request, 'front/cookies-policy.html')


def contact(request):
    return render(request, 'front/contact.html')


def checkout(request):
    return render(request, 'front/checkout.html')


def add_produits(request, produit_id):
    if request.method == 'POST':
        produits = get_object_or_404(Produit, id_produit=produit_id)
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None
        commande = Commande.objects.filter(user=user)
        if commande.exists():
            commande = commande.first()
        else:
            commande = Commande.objects.create(user=user)

        commande_produit, created = Commande_Produit.objects.get_or_create(
            commande=commande,
            produits=produits
        )
        if not created:
            commande_produit.quantite += 1
            commande_produit.save()
        else:
            commande_produit.quantite = 1
            commande_produit.save()
        return redirect('cart')
    else:
        produits = Produit.objects.all()
        return render(request, 'front/index.html', {'produits': produits})
    
def cart(request):
    commande = Commande_Produit.objects.all()
    count = 0
    for command in commande:
        count += 1
    count4 = count - 3
    if count4 == -3 or count4 == -2 or count4 == -1 or count4 == 0:
        header_commande = Commande_Produit.objects.all()
    else:
        header_commande = Commande_Produit.objects.all()[count4:count]
    return render(request, 'front/cart.html', {'commande': commande, 'header_commande': header_commande,})

def delete_produit(request, commande_id):
    commande_produit = get_object_or_404(Commande_Produit, id=commande_id)
    commande_produit.delete()
    return redirect(cart)

def delete_all_produit(request):
    commande_produit = Commande_Produit.objects.all()
    commande_produit.delete()
    return redirect(cart)


def blog_list_right_sidebar(request):
    return render(request, 'front/blog-list-right-sidebar.html')


def blog_list_left_sidebar(request):
    return render(request, 'front/blog-list-left-sidebar.html')


def blog_details(request):
    return render(request, 'front/blog-details.html')


def blog(request):
    return render(request, 'front/blog.html')


def account(request):
    return render(request, 'front/account.html')


def about(request):
    return render(request, 'front/about.html')


def page_not_found(request):
    return render(request, 'front/404.html')


def search(request):
    query = request.GET.get('query')
    categories = Categories.objects.none()

    if query:
        categories = Categories.objects.filter(name__icontains=query)
        results = Produit.objects.filter(name__icontains=query)
    else:
        results = Produit.objects.none()
    return render(request, 'front/search_results.html', {'results': results, 'query': query, 'categories': categories})


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Message.objects.create(name=name, email=email, subject=subject, message=message)

    context = {'name': name, 'email': email, 'subject': subject, 'message': message}
    return render(request, 'front/contact.html', context)