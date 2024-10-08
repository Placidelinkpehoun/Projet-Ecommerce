from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_dash, name='dashboard_index'),
    path('home_2/', views.home_2, name='home_2'),
    path('home_4/', views.home_4, name='home_4'),
    path('home_3/', views.home_3, name='home_3'),
    path('home_boxed/', views.home_boxed, name='home_boxed'),
    path('home_menu_icon_default/', views.home_menu_icon_default, name='home_menu_icon_default'),
    path('home_menu_icon_hover/', views.home_menu_icon_hover, name='home_menu_icon_hover'),
    #path('header_dash', views.header_dash, name='header_dash'),
    path('new_category/', views.new_category, name='new_category'),
    path('new_page/', views.new_page, name='new_page'),
    path('oder_details/', views.oder_details, name='oder_details'),
    path('oder_list/', views.oder_list, name='oder_list'),
    path('oder_tracking/', views.oder_tracking, name='oder_tracking'),
    path('product_detail_3/', views.product_detail_3, name='product_detail_3'),
    path('product_detail_2/', views.product_detail_2, name='product_detail_2'),
    path('product_detail_1/', views.product_detail_1, name='product_detail_1'),
    path('product_list/', views.product_list, name='product_list'),
    path('report/', views.report, name='report'),
    path('settings/', views.settings, name='settings'),
    path('states/', views.states, name='states'),
    path('list_page/', views.list_page, name='list_page'),
    path('gallery/', views.gallery, name='gallery'),
    path('edit_page/', views.edit_page, name='edit_page'),
    path('create_role/', views.create_role, name='create_role'),
    path('countries/', views.countries, name='countries'),
    path('components/', views.components, name='components'),
    path('cities/', views.cities, name='cities'),
    path('category_list/', views.category_list, name='category_list'),
    path('attributes/', views.attributes, name='attributes'),
    path('all_user/', views.all_user, name='all_user'),
    path('all_roles/', views.all_roles, name='all_roles'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_new_user/', views.add_new_user, name='add_new_user'),
    path('add_attributes/', views.add_attributes, name='add_attributes'),
    path('login_dashboard/', views.login_dashboard, name='login_dashboard'),
    path('logout', views.logout_dashboard, name='logout_dashboard'),
    path('login_admin', views.login_admin, name='login_admin'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('is_admin', views.is_admin, name='is_admin'),
    path('category_list', views.category_list, name='category_list'),
    path('cities/', views.cities, name='cities'),
    path('components/', views.components, name='components'),
    path('attributes', views.attributes, name='attributes'),
    path('delete_produit_dash/<int:id_categorie>', views.delete_produit_dash, name='delete_produit_dash'),
    path('add_category/', views.add_category, name='add_category'),
]
