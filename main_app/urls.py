from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="Home"),
    path('about/', views.About.as_view(), name="About"),
    path('allgoats/', views.GoatsList.as_view(), name="goats_list"),
    path('allgoats/new/', views.GoatCreate.as_view(), name="goat_create"),
    path('allgoats/<int:pk>/', views.GoatDetail.as_view(), name="goat_detail"),
    path('allgoats/<int:pk>/update',views.GoatUpdate.as_view(), name="goat_update"),
    path('allgoats/<int:pk>/delete',views.GoatDelete.as_view(), name="goat_delete"),
    path('allgoats/<int:pk>/expertises/new/', views.ExpertiseCreate.as_view(), name="expertise_create"),
    path('customgoats/<int:pk>/expertises/<int:expertise_pk>/', views.CustomGoatExpertiseAssoc.as_view(), name="customgoat_expertise_assoc"),
    path('accounts/signup/', views.Signup.as_view(), name="signup")
]