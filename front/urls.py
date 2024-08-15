from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('header', views.header, name="header"),
    path('index-two/', views.index_two, name='index_two'),
    path('index-three/', views.index_three, name='index_three'),
    path('index-four/', views.index_four, name='index_four'),
    path('index-five/', views.index_five, name='index_five'),
    path('invoice/', views.invoice, name='invoice'),
    path('login_front/', views.login_front, name='login_front'),
    path('logout_front/', views.logout_front, name='logout_front'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('register/', views.register, name='register'),
    path('shop-compare/', views.shop_compare, name='shop_compare'),
    path('shop-details/', views.shop_details, name='shop_details'),
    path('shop-details-2/', views.shop_details_2, name='shop_details_2'),
    path('shop-details-4/', views.shop_details_4, name='shop_details_4'),
    path('shop-details-affiliats/', views.shop_details_affiliats, name='shop_details_affiliats'),
    path('shop-details-group/', views.shop_details_group, name='shop_details_group'),
    path('shop-details-right-sidebar/', views.details_right_sidebar, name='details_right_sidebar'),
    path('shop-details-variable/', views.shop_details_variable, name='shop_details_variable'),
    path('shop-grid-sidebar/<int:id_categorie>', views.shop_grid_sidebar, name='shop_grid_sidebar'),
    path('shop-grid-top-filter/', views.shop_grid_top_filter, name='shop_grid_top_filter'),
    path('shop-list-sidebar/', views.shop_list_sidebar, name='shop_list_sidebar'),
    path('shop-list-top-filter/', views.shop_list_top_filter, name='shop_list_top_filter'),
    path('store/', views.store, name='store'),
    path('terms-condition/', views.terms_condition, name='terms_condition'),
    path('this-params/', views.this_params, name='this_params'),
    path('trackorder/', views.trackorder, name='trackorder'),
    path('vendor-details/', views.vendor_details, name='vendor_details'),
    path('vendor-details-grid/', views.vendor_details_grid, name='vendor_details_grid'),
    path('vendor-list/', views.vendor_list, name='vendor_list'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('faq/', views.faq, name='faq'),
    path('e/', views.e, name='e'),
    path('cookies-policy/', views.cookies_policy, name='cookies_policy'),
    path('contact/', views.contact, name='contact'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name='cart'),
    path('blog-list-right-sidebar/', views.blog_list_right_sidebar, name='blog_list_right_sidebar'),
    path('blog-list-left-sidebar/', views.blog_list_left_sidebar, name='blog_list_left_sidebar'),
    path('blog-details/', views.blog_details, name='blog_details'),
    path('blog/', views.blog, name='blog'),
    path('account/', views.account, name='account'),
    path('about/', views.about, name='about'),
    path('404/', views.page_not_found, name='page_not_found'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact_view, name='contact_view'),
    path('add_produits/<int:produit_id>', views.add_produits, name='add_produits'),
    path('delete_produit/<int:commande_id>', views.delete_produit, name='delete_produit'),
    path('delete_all_produit/', views.delete_all_produit, name='delete_all_produit'),
]
