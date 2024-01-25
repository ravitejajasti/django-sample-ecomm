from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register, name='register'),
    path('add/', views.add_company, name='add_company'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('<int:id>/', views.companydetail, name='detail'),

    # Add more paths as needed
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
