from django.urls import include
from django.urls import path
from Threadly import views
app_name= 'Threadly'
urlpatterns = [
    path('', views.index, name='index'),  
    path('home/', views.index, name='home'),  
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('trending/', views.trending, name='trending'),
    path('search/', views.search, name='search'),
    path('account/', views.account, name='account'),
    path('categories/', views.categories, name='categories'),
    path('create-post/', views.create_post, name='create_post'),
    path('category/<slug:slug>/', views.show_category, name='show_category'),
    path('post/<int:post_id>/', views.show_post, name='show_post'),
    path('post/<int:post_id>/add_comment', views.add_comment, name='add_comment'),
    path('follow-thread/<int:thread_id>/', views.follow_thread, name='follow_thread'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    path('post/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
    
    
]