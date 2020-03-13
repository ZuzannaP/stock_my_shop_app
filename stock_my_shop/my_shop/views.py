from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView, FormView

from .forms import LoginForm
from .models import Category, Product


def homepage(request):
    return render(request, "homepage.html")


class CategoriesView(View):
    def get(self, request):
        categories = Category.objects.all().order_by("category_name")
        ctx = {"categories": categories}
        return render(request, "categories_view.html", ctx)


class OneCategory(View):
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        products = category.product_set.all().order_by("name")
        ctx = {
            "category": category,
            "products": products,
        }
        return render(request, "one_category.html", ctx)


class ProductsView(View):
    def get(self, request):
        products = Product.objects.all().order_by("name")
        ctx = {"products": products}
        return render(request, "products_view.html", ctx)


class OneProduct(View):
    def get(self, request, id):
        product = Product.objects.get(pk=id)
        ctx = {"product": product, }
        return render(request, "one_product.html", ctx)


class CategoryCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'my_shop.add_category'
    template_name = "category_form.html"
    model = Category
    fields = "__all__"
    success_url = reverse_lazy("categories")


class CategoryUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'my_shop.change_category'
    template_name = 'category_update_form.html'
    model = Category
    fields = "__all__"
    success_url = reverse_lazy("categories")


class CategoryDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'my_shop.delete_category'
    template_name = 'category_confirm_delete.html'
    model = Category
    success_url = reverse_lazy("categories")


class ProductCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'my_shop.add_product'
    template_name = "product_form.html"
    model = Product
    fields = "__all__"
    success_url = reverse_lazy("products")


class ProductUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'my_shop.change_product'
    template_name = 'product_update_form.html'
    model = Product
    fields = "__all__"
    success_url = reverse_lazy("products")


class ProductDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'my_shop.delete_product'
    template_name = 'product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy("products")


class SearchDB(View):
    def post(self, request):
        ctx = {}
        searched_word = request.POST.get("search", False)
        matching_products = Product.objects.filter(name__istartswith=searched_word)
        matching_categories = Category.objects.filter(category_name__istartswith=searched_word)
        ctx["matching_products"] = matching_products
        ctx["matching_categories"] = matching_categories
        return render(request, "search_results.html", ctx)


class LoginView(FormView):
    form_class = LoginForm
    success_url = "/products"
    template_name = "login.html"

    def form_valid(self, form: LoginForm):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(self.request, username=username, password=password)

        if user is None:
            form.add_error(None, "Incorrect login or password")
            return super().form_invalid(form)

        login(self.request, user)
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        return render(request, "logout.html")

    def post(self, request):
        ctx = {}
        logout(request)
        if request.user.is_authenticated:
            ctx["my_verdict"] = "Ups. Something went wrong."
        else:
            ctx["my_verdict"] = "You have been logged out"
        return render(request, "logout.html", ctx)
