import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from django.contrib.auth.models import Permission
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout

from django.conf import settings
from jwt import register_algorithm
from .forms import CustomUserChangeForm, UserRegisterForm, SellerChangeForm, UserLoginForm
from .models import Seller, EmailActivateCodes
from menu.models import Product, Type
import smtplib
import ssl

def register(request):
    if request.method == 'GET':
        context = {'register' : UserRegisterForm(), 'login' : UserLoginForm()}
        return render(request, template_name='register.html', context=context)    
    else:
        register_form = UserRegisterForm(request.POST)
        login_form = UserLoginForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.is_active = False
            user.save()

            # One user Group
            user_group = Group.objects.get(name=register_form.cleaned_data['groups'])
            user.groups.add(user_group)

            # Multiple user Groups
            # for form_ug in register_form.cleaned_data['groups']:
            #     user_group = Group.objects.get(name=form_ug.name)
            #     user.groups.add(user_group)
            

            subject = "Verificate your email"
            body = "You can verificate your email with this link"
            sender_email = settings.EMAIL_HOST_USER
            receiver_email = request.POST.get('email')
            # Create a multipart message and set headers
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
            message["Bcc"] = receiver_email  # Recommended for mass emails
            # Add body to email
            message.attach(MIMEText(body, "plain"))
            password = settings.EMAIL_HOST_PASSWORD
            code = str(random.randint(1000, 1000000))
            email = EmailActivateCodes(user=user, code=code)
            email.save()
            message = (
                f"Your verification code is {code}")
            print(message)    
            text = message
            context = ssl.create_default_context()

            with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
                server.connect(settings.EMAIL_HOST, settings.EMAIL_PORT)
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, text)
                print('SEND')
                server.close()
            reverse_match = reverse_lazy('verifiy', kwargs={'id': user.id})
            return redirect(reverse_match)
        if login_form.is_valid():  
            username = request.POST.get('username')  
            password = request.POST.get('password')  
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home')
        


class SignUpView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('log_in')
    template_name = 'registration/register.html'

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print('post')
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # One user Group
            user_group = Group.objects.get(name=form.cleaned_data['groups'])
            user.groups.add(user_group)

            # Multiple user Groups
            # for form_ug in form.cleaned_data['groups']:
            #     user_group = Group.objects.get(name=form_ug.name)
            #     user.groups.add(user_group)
            

            subject = "Verificate your email"
            body = "You can verificate your email with this link"
            sender_email = settings.EMAIL_HOST_USER
            receiver_email = request.POST.get('email')
            # Create a multipart message and set headers
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
            message["Bcc"] = receiver_email  # Recommended for mass emails
            # Add body to email
            message.attach(MIMEText(body, "plain"))
            password = settings.EMAIL_HOST_PASSWORD
            code = str(random.randint(1000, 1000000))
            email = EmailActivateCodes(user=user, code=code)
            email.save()
            message = (
                f"Your verification code is {code}")
            print(message)    
            text = message
            context = ssl.create_default_context()

            with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
                server.connect(settings.EMAIL_HOST, settings.EMAIL_PORT)
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, text)
                print('SEND')
                server.close()
            reverse_match = reverse_lazy('verifiy', kwargs={'id': user.id})
            return redirect(reverse_match)
            # return render(request, 'registration/email-verificate,html', {'form': form})
        else:
            return render(request, self.template_name, {'form': form})


def verificate_view(request, *args, **kwargs):
    if request.method == 'GET':
        print('if ga kirmadi method==GET')
        if request.GET.get('code'):
            username = request.GET.get('id')
            code = request.POST.get('email_verificate')
            print(code, username, 'method==POST')
            user = EmailActivateCodes.objects.filter(user__username=username).first()
            if code == object.code:
                user.is_active = True
                user.save()
                return redirect('home')
            else:
                print('code togri kelmadi')
                context = {'error':'Invalid code'}
                return render(request, 'registration/email-verificate.html', context)    
        else:
            print('else method==POST')
            user = User.objects.filter(id=kwargs.get('id')).first()
            user_verifiy = EmailActivateCodes.objects.filter(user=username).first()
            context = {'code':user_verifiy.code}
            return render(request, 'registration/email-verificate.html', context=context)
                 
    if request.method == 'POST':
        username = kwargs.get('id')
        code = request.POST.get('email_verificate')
        print(code, username, 'method==POST')
        user_verifiy = EmailActivateCodes.objects.filter(user=username).first()
        user = User.objects.filter(id=username).first()
        print(user, 'if ga kirmadi method==POST')
        if code == user_verifiy.code:
            user.is_active = True
            user.save()
            user = authenticate(request, username=user.username, password=user.password)
            login(request, user)
            return redirect('home')
        else:
            print('else method==POST')
            context = {'error':'Invalid code'}
            return render(request, 'registration/email-verificate.html', context)




class LoginView(LoginView):
    template_name = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return self.render_to_response(self.get_context_data())


class ProfilePageView(ListView):
    form_class = UserRegisterForm
    template_name = 'users/user-info.html'
    context_object_name = 'user'

    def get_queryset(self, **kwargs):
        return User.objects.get(pk=self.kwargs.get('id'))


# def update_seller(request, id):
#     if request.method == 'GET':
#         user = request.user
#         ctx = {'user': CustomUserChangeForm(instance=user)}
#         if 'menu.add_product' in user.get_user_permissions():
#             try:
#                 seller = Seller.objects.get(user=user)
#                 ctx['seller'] = SellerChangeForm(instance=seller)
#             except:
#                 ctx['seller'] = SellerChangeForm()
#             return render(request, template_name="users/edit-user-profile.html", context=ctx)
#         else:
#             return render(request, template_name="users/edit-user-profile.html", context=ctx)

#     if request.method == 'POST':
#         user = request.user

        # user_form = CustomUserChangeForm(request.POST, instance=user)
        # if user.groups.filter(name="Seller"):
        #     data = request.POST.copy()
        #     seller_form = SellerChangeForm(data=data)
        #     if user_form.is_valid() and seller_form.is_valid():

        #         user_group = Group.objects.get(pk=data['groups'])
        #         user.groups.add(user_group)
        #         user.save()

        #         if user.seller is None:
        #             seller = seller_form.instance
        #             seller.user = user
        #             seller.save()
        #         else:
        #             print(user.seller)
        #             seller_form.save()
        # else:
        #     if user_form.is_valid():
        #         print('else if')
        #         user_group = Group.objects.get(pk=data['groups'])
        #         user.groups.add(user_group)
        #         user.save()

        # return redirect(f'/profile/{request.user.id}/')


class EditProfileView(UpdateView):
    user_form = CustomUserChangeForm
    seller_form = SellerChangeForm
    template_name = 'users/edit-user-profile.html'
    success_url = reverse_lazy('home')

    def get_user_permissions(self, user, request):
        return render(request, self.template_name, context=(user.get_user_permissions() | Permission.objects.filter(group__user=user)))

    def get(self, request, *args, **kwargs):
        user = request.user
        ctx = {'user_form': CustomUserChangeForm(
            instance=user), 'user_id': user.id}
        if user.groups.filter(name="Seller"):
            try:
                seller = Seller.objects.get(user=user)
                ctx['seller_form'] = SellerChangeForm(instance=seller)
            except:
                ctx['seller_form'] = SellerChangeForm()

            return render(request, template_name="users/edit-user-profile.html", context=ctx)
        else:
            return render(request, template_name="users/edit-user-profile.html", context=ctx)

    def post(self, request, *args, **kwargs):
        user = request.user
        user_form = CustomUserChangeForm(request.POST, instance=user)
        if user.groups.filter(name="Seller"):
            data = request.POST.copy()
            seller_form = SellerChangeForm(data=data)
            if user_form.is_valid() and seller_form.is_valid():

                user_group = Group.objects.get(pk=data['groups'])
                user.groups.add(user_group)
                user.save()

                try:
                    seller = Seller.objects.get(user=user.id)
                    seller.gender = data['gender']
                    seller.phone_number = data['phone_number']
                    seller.age = data['age']
                    seller.save()
                except:
                    seller = seller_form.instance
                    seller.user = user
                    seller.save()
        else:
            if user_form.is_valid():
                print('else if')
                user_group = Group.objects.get(pk=data['groups'])
                user.groups.add(user_group)
                user.save()

        return redirect(f'/profile/{request.user.id}/')


class DeleteProfileView(DeleteView):
    model = User
    template_name = 'users/delete-user-profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return User.objects.get(pk=self.kwargs.get('id'))


class SellerProducts(ListView):
    model = Product
    template_name = 'seller/seller-products.html'
    context_object_name = 'products_list'

    def get_queryset(self):
        try:
            seller = Seller.objects.get(user_id=self.kwargs.get('id'))
            context = Product.objects.filter(seller_id=seller.id)
        except:
            context = {}
        return context


class SellerAddProduct(CreateView):
    model = Product
    template_name = 'seller/seller-add-product.html'
    fields = ['image', 'product_title', 'type', 'description',
              'price']
    context_object_name = 'form'
    success_url = reverse_lazy('seller_add_product')

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.seller = Seller.objects.filter(
            user=self.request.user).first()
        return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     request.POST['seller'] = kwargs={'id':self.kwargs['user_id']}
    #     return super().post(request, *args, **kwargs)


class SellerUpdateProduct(UpdateView):
    model = Product
    fields = ['image', 'product_title', 'description',
              'price', 'seller']
    template_name = 'seller/seller-update-product.html'

    def get_success_url(self):
        return reverse_lazy('seller_products', kwargs={'id': self.kwargs['user_id']})


class SellerDeleteProduct(DeleteView):
    model = Product
    template_name = 'seller/seller-delete-product.html'
    context_object_name = 'product'

    def get_success_url(self):
        return reverse_lazy('seller_products', kwargs={'id': self.kwargs['user_id']})


class SellerTypes(ListView):
    model = Type
    template_name = 'seller/seller-types.html'
    context_object_name = 'types_list'

    def get_queryset(self):
        try:
            seller = Seller.objects.get(user_id=self.kwargs.get('id'))
            context = Type.objects.filter(seller_id=seller.id)
        except:
            context = {}
        return context


class SellerAddType(CreateView):
    model = Type
    template_name = 'seller/seller-add-type.html'
    fields = ['name']
    success_url = reverse_lazy('seller_add_type')

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.seller = Seller.objects.filter(
            user=self.request.user).first()
        return super().form_valid(form)


class SellerUpdateType(UpdateView):
    model = Type
    fields = ['name']
    template_name = 'seller/seller-update-type.html'
    context_object_name = 'type'

    def get_success_url(self):
        return reverse_lazy('seller_types', kwargs={'id': self.kwargs['user_id']})


class SellerDeleteType(DeleteView):
    model = Type
    template_name = 'seller/seller-delete-type.html'
    context_object_name = 'type'

    def get_success_url(self):
        return reverse_lazy('seller_types', kwargs={'id': self.kwargs['user_id']})
