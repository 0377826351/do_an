from django.urls import path
from .views.website import home,about_us,cart,detail_item,items,store,pay,myorder,user
from .views.admin.auth import login,admin,category_admin,items_admin,staff,receipt,customer
urlpatterns = [
    path('',home.index,name='home_index'),
    path('items',items.index,name='items_index'),
    path('items/filter/<str:ft>',items.index,name='items_filter_index'),
    path('items/<int:slug>/',items.index,name='items_click_index'),
    path('items/<int:slug>/<str:ft>',items.index,name='items_click_index'),
    path('store',store.index,name='store_index'),
    path('detail-item/<str:slug>',detail_item.index,name='detai_item_index'),
    path('about-us',about_us.index,name='about_us_index'),
    path('cart',cart.index,name='cart_index'),
    path('pay',pay.index,name='pay_index'),
    path('myorder',myorder.index,name='myorder_index'),
    path('myorder/delete/<int:id>',myorder.delete,name='myorder_delete'),
    path('delete/<str:code>-<str:size>',cart.delete,name='delete_item'),

    path('login',user.login,name='user_login'),
    path('register',user.register,name='user_register'),
    path('change-password',user.changePassword,name='user_changePassword'),
    path('forgot-password',user.forgotPassword,name='user_forgotPassword'),
    path('reset-password-user-confirm/<int:id>/<token>/<token_date>', user.reset_password_confirm_user, name='reset_password_user_done_index'),

    # path('forget-password',user.Forget_Password,name='forget_password'),
    # path('changeps/<token>/',user.changeps,name='changeps'),

    path('logout',user.log_out,name='user_logout'),
    
    path('logout-admin', admin.log_out, name='logout_index'),
    path('change_password-admin', admin.change_password, name='change_password_index'),
    path('login-admin', login.login, name='login_index'),
    path('register-admin', login.regis, name='register_index'),
    path('adduser-admin', login.adduser, name='adduser_index'),
    path('forgot-password-admin', login.forgot, name='forgot-password_index'),
    path('reset-password-confirm/<int:id>/<token>/<token_date>', login.reset_password_confirm, name='reset_password_done_index'),
    path('home-admin', admin.index, name='home-admin_index'),
    path('profile', admin.profile, name='profile_index'),
    path('edit_profile', admin.edit_profile, name='edit_profile_index'),
    path('update_profile', admin.update_profile, name='update_profile_index'),


    path('category-admin', category_admin.category, name='category_admin_index'),
    path('category-admin/add-cate', category_admin.add, name='form_cate_index'),
    path('category-admin/update/<int:id>', category_admin.update, name='form_cate_index'),
    path('category-admin/delete/<int:id>', category_admin.delete, name='delete_cate_index'),


    path('items-admin', items_admin.items, name='items_admin_index'),
    path('items-admin/add_item', items_admin.add_item, name='add_items_index'),
    path('items-admin/update/<int:id>', items_admin.update_item, name='update_items_index'),
    path('items-admin/delete/<int:id>', items_admin.delete_item, name='delete_items_index'),

    path('staff-admin', staff.staff, name='staff_admin_index'),
    path('staff-admin/delete/<int:id>', staff.delete, name='staff_admin_delete'),

    path('customer-admin', customer.customer, name='customer_admin_index'),
    path('customer-admin/delete/<int:id>', customer.delete, name='customer_admin_delete'),


    path('receipt-admin', receipt.receipt, name='receipt_admin_index'),
    path('receipt-admin/update/<str:id>', receipt.update_receipt, name='update_rec_index'),
    path('receipt-admin/delete/<int:id>', receipt.delete_rec, name='delete_rec_index'),


    
]