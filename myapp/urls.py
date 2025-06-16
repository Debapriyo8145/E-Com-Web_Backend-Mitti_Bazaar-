from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('account/', views.account, name='account'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('order-history/', views.order_history, name ="orders" ),
    path('shop/', views.shop, name ="shop" ),
    path('product_details/<int:product_id>/', views.product_details, name='product_details'),
    
]