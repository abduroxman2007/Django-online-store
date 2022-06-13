from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from matplotlib.style import context
from .models import Contact, Product, Type
from django.db.models import Q
from django.contrib.auth import logout, login
from django.core.paginator import Paginator
# Create your views here.

# ------------------------------------------------- Main menu ---------------------------------------------------------------------------#

# class Register(ListView):
#     model = Users
#     template_name = 'register.html'

#     def post(self, request):
#         if request.POST.get('email'):
#             Users.objects.create(username=request.POST.get('username'), email=request.POST.get(
#                 'email'), password=request.POST.get('password'))
#             return render(request, 'register.html')
#         else:
#             if request.POST.get('username') == 'admin' and request.POST.get('password') == 'admin':
#                 return redirect('/dashboard/')

#             elif Users.objects.filter(username=request.POST.get('username'), password=request.POST.get('password')):
#                 id = Users.objects.filter(username=request.POST.get('username')).values_list('id', flat=True).first()
#                 return redirect(f'/profile/{id}/')
#             else:
#                 return render(request, 'register.html', context={'wrong': 1})

             


def returhomeview(request):
    return HttpResponseRedirect(reverse_lazy('home'))


class HomePageView(ListView):
    template_name = 'index.html'
    context_object_name = 'products_list'
    queryset = Product.objects.all()[:6]


def product_page_view(request):
    if request.method == 'GET':
        context = {
            'types': Type.objects.all()
        }
        print(context)
        return render(request, 'products.html', context={'types':Type.objects.all()})


class ProductsPageView(ListView):   
    model = Product
    template_name = 'products.html'
    context_object_name = 'products_list'
    paginate_by = 6

    def get_queryset(self):
        # context = {'types' : Type.objects.all()}
        if 'search_text' in self.request.GET:
            result = Product.objects.filter(
                Q(product_title__icontains=self.request.GET.get('search_text')))
            product_page_view(self.request)
            return result
        else:
            product_page_view(self.request)
            return Product.objects.all()      

    # def get_context_data(self, **kwargs):
    #     if 'search_text' in self.request.GET:
    #         result = Product.objects.filter(
    #             Q(product_title__icontains=self.request.GET.get('search_text')))
    #         context = {'types' : Type.objects.all(), 'products_list': Paginator(result, 6)}
    #         return context
    #     else:
    #         object = Product.objects.all()
    #         context = {'types' : Type.objects.all(), 'products_list': Paginator(object, 6)}
    #         return context


class ProductInfoView(ListView):
    model = Product
    template_name = 'product/product-info.html'
    context_object_name = 'product'

    def get_queryset(self):
        id = self.kwargs.get('product_id')
        print(id)
        # context = {'prodcut':Product.objects.get(pk=id)}
        # print(context)
        return Product.objects.get(pk=id)

class AboutPageView(TemplateView):
    template_name = 'about.html'
    

# ------------------------------------------------- UpdateView ---------------------------------------------------------------------------#




# ------------------------------------------------- Dashboard ---------------------------------------------------------------------------#

def senddashboardview(request):
    return redirect('dashboard/')

# ------------------------------------------------- ListView ---------------------------------------------------------------------------#


class DashboardPageView(ListView):
    model = Product
    template_name = 'dashboard.html'


class DashboardProductsListPageView(ListView):
    model = Product
    context_object_name = 'products_list'
    template_name = 'products-list.html'


class DashboardProductsView(ListView):
    model = Product
    template_name = 'dashboard-products.html'


class DashboardNotificationsView(ListView):
    model = Contact
    template_name = 'dashboard-notifications.html'
    context_object_name = 'notifications'


class DashboardTypeView(ListView):
    model = Type
    template_name = 'dashboard-type/type-list.html'
    context_object_name = 'type_list'


# ------------------------------------------------- CreateView ---------------------------------------------------------------------------#


class DashboardCreatNotificationsView(CreateView):
    model = Contact
    fields = ['name', 'email', 'text']
    template_name = 'contact.html'
    success_url = '/home/'


class CreateProductsView(CreateView):
    model = Product
    template_name = 'create-product.html'
    fields = ['product_title', 'type','description',
              'price', 'image']
    context_object_name = 'form'
    success_url = '/dashboard/products-list/'

    def get_object(self):
        return Product.objects.get(pk=self.kwargs.get('id'))


class  CreateTypeView(CreateView):
    model = Type
    template_name =  'dashboard-type/create-type.html'
    fields = ['name']
    success_url = '/dashboard/dashboard/'



# ------------------------------------------------- UpdateView ---------------------------------------------------------------------------#


class UpdateProductsView(UpdateView):
    model = Product
    template_name = 'edit-product.html'
    fields = ['image', 'product_title', 'description',
              'price', 'seller']
    context_object_name = 'form'
    success_url = '/dashboard/products-list/'

    def get_object(self):
        return Product.objects.get(pk=self.kwargs.get('id'))


class UpdateTypeView(UpdateView):
    model = Type
    template_name = 'dashboard-type/type-edit.html'
    fields = ['name']
    context_object_name = 'form'
    success_url = '/dashboard/products-list/'

    def get_object(self):
        return Type.objects.get(pk=self.kwargs.get('id'))


# ------------------------------------------------- DeleteView ---------------------------------------------------------------------------#


class DeleteProductsView(DeleteView):
    model = Product
    template_name = 'delete-product.html'
    success_url = '/dashboard/products-list/'

    def get_object(self):
        return Product.objects.get(pk=self.kwargs.get('id'))


class DeleteTypeView(DeleteView):
    model = Type
    template_name = 'dashboard-type/type-delete.html'
    success_url = '/dashboard/type-list/'

    def get_object(self):
        return Type.objects.get(pk=self.kwargs.get('id'))



