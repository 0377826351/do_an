from django.urls import path
from .views.website import home,about_us,cart,detail_item,items,store,pay,myorder,user

urlpatterns = [
    path('home',home.index,name='home_index'),
    path('items',items.index,name='items_index'),
    path('store',store.index,name='store_index'),
    path('detail-item',detail_item.index,name='detai_item_index'),
    path('about-us',about_us.index,name='about_us_index'),
    path('cart',cart.index,name='cart_index'),
    path('pay',pay.index,name='pay_index'),
    path('myorder',myorder.index,name='myorder_index'),


    path('login',user.login,name='user_login'),
    path('register',user.register,name='user_register'),
    path('changePassword',user.changePassword,name='user_changePassword'),
    path('forgotPassword',user.forgotPassword,name='user_forgotPassword'),
    path('logout',user.log_out,name='user_logout'),

]