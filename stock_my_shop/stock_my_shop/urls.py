"""stock_my_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from my_shop.views import homepage, CategoriesView, ProductsView, OneCategory, OneProduct, CategoryCreate, \
    CategoryUpdate, CategoryDelete, ProductCreate, ProductDelete, ProductUpdate, SearchDB, LoginView,\
    LogoutView


urlpatterns = [
    path('manager/', admin.site.urls),
    path("", homepage, name="homepage"),
    path("categories/", CategoriesView.as_view(), name="categories"),
    path("category/<slug:slug>/", OneCategory.as_view(), name="one_category"),
    path("products/", ProductsView.as_view(), name="products"),
    path("product/<int:id>/", OneProduct.as_view(), name="one_product"),
    path("add_category/", CategoryCreate.as_view()),
    path("edit_category/<slug:slug>/", CategoryUpdate.as_view()),
    path("delete_category/<slug:slug>/", CategoryDelete.as_view()),
    path("add_product/", ProductCreate.as_view()),
    path("edit_product/<int:pk>/", ProductUpdate.as_view()),
    path("delete_product/<int:pk>/", ProductDelete.as_view()),
    path("search/", SearchDB.as_view(), name="search"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout")
]
