from django.urls import path
from .views.website import home,about_us,cart,detail_item,items,store,pay,myorder,user
from .views.admin.auth import login,admin,category_admin,article_admin,question_admin


urlpatterns = [
    path('home',home.index,name='home_index'),

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


    path('login',user.login,name='user_login'),
    path('register',user.register,name='user_register'),
    path('change-password',user.changePassword,name='user_changePassword'),
    path('forgot-password',user.forgotPassword,name='user_forgotPassword'),
    path('logout',user.log_out,name='user_logout'),
    
    path('logout-admin', admin.log_out, name='logout_index'),
    path('change_password-admin', admin.change_password, name='change_password_index'),
    path('login-admin', login.login, name='login_index'),
    path('register-admin', login.regis, name='register_index'),
    path('adduser-admin', login.adduser, name='adduser_index'),
    path('forgot-password-admin', login.forgot, name='forgot-password_index'),
    path('reset-password-confirm/<int:id>/<token>/<token_date>', login.reset_password_confirm, name='reset_password_done_index'),
    path('home-admin', admin.index, name='home-admin_index'),
    # path('contact-admin', admin.contact, name='contact_admin_index'),
    path('profile', admin.profile, name='profile_index'),
    path('edit_profile', admin.edit_profile, name='edit_profile_index'),
    path('update_profile', admin.update_profile, name='update_profile_index'),


    path('category-admin', category_admin.category, name='category-admin_index'),
    path('category-admin/form_cate', category_admin.form_cate, name='form_cate_index'),
    path('category-admin/form_cate/<str:alias>', category_admin.form_cate, name='form_cate_index'),
    path('category-admin/delete/<str:alias>', category_admin.delete_cate, name='delete_cate_index'),


    path('article-admin', article_admin.article, name='article-admin_index'),
    path('article-admin/form_art', article_admin.form_art, name='update_article_index'),
    path('article-admin/form_art/<str:alias>', article_admin.form_art, name='update_article_index'),
    path('article-admin/delete/<str:alias>', article_admin.delete_article, name='delete_article_index'),


    path('question-admin', question_admin.question, name='question-admin_index'),
    path('question-add', question_admin.add_question, name='add_ques_index'),
    path('question-admin/update/<str:id>', question_admin.update_question, name='update_ques_index'),
    path('question-admin/delete/<int:id>', question_admin.delete_ques, name='delete_ques_index'),


    
]