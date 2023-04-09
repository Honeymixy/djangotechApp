from django.urls import path

# from .views import PostUpdateView, HomePageView, ContactPageView, AboutPageView, PostDetailView, AddPostView, PostDeleteView
from . import views
urlpatterns = [
    path('register/', views.registerPage, name='register'),
    # path('login/', views.login_user, name='login'),
    # path('logout/', views.logoutPage, name='logout')
]
