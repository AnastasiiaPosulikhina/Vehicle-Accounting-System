"""kursovaya URL Configuration
"""
from django.contrib import admin
from django.urls import path
from kurs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signinRender),
    path('signOut/', views.signOutRender),
    path('users/', views.usersRender),
    path('newuser/', views.newUserRender),
    path('editUser/', views.editUsersRender),
    path('deleteUser/', views.deleteUserRender),
    path('newCompany/', views.newCompanyRender),
    path('deleteCompany/', views.deleteCompanyRender),
    path('companyList/', views.companyListRender),
    path('companyInfo/<int:companyid>', views.companyInfoRender),
    path('staffList/<int:companyid>', views.staffListRender),
    path('newWorker/<int:companyid>/', views.newWorkerRender),
    path('deleteWorker/<int:companyid>/', views.deleteWorkerRender),
    path('carsList/<int:companyid>/', views.carsListRender),
    path('carInfo/<int:carid>/', views.carInfoRender),
    path('newCar/<int:companyid>/', views.newCarRender),
    path('deleteCar/<int:companyid>/', views.deleteCarRender)
]

