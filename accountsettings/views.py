from django.shortcuts import render
from django.views.generic import TemplateView, View, FormView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate
from .forms import ProfileSettingsForm
from django.core.files.storage import FileSystemStorage
from products.models import Product, Wishlist
from django.core.paginator import Paginator
from .models import SavedAddress, SavedPayment
from .forms import SavedAddressForm, SavedPaymentForm, PlanForm
from django.views.generic.detail import SingleObjectMixin
from mycart.models import CheckoutModel
import os

class MyProductsView(LoginRequiredMixin, ListView):
    template_name = "account/my-products.html"
    
    def get_queryset(self):
        page = self.request.GET.get('page', 1)
        tag = Product.objects.all().filter(owner=self.request.user)
        paginator = Paginator(tag, 6)
        tag = paginator.page(page)
        return tag

class AccountSettingsView(LoginRequiredMixin, FormView):
    model = get_user_model()
    form_class = ProfileSettingsForm
    template_name = "account/profile-settings.html"
    success_url = 'profile-settings'
    
    def form_valid(self, form):
        userpk = self.request.user.pk
        model = get_user_model()
        data = form.cleaned_data
        if(data['username'] != ''):
            model.objects.filter(id=userpk).update(username=data['username'])
        if(data['email'] != ''):
            model.objects.filter(id=userpk).update(email=data['email'])
        if(data['profileimage'] != None):
            if(str(model.objects.get(id=userpk).profileimage) != "not.png"):
                if(os.path.exists(model.objects.get(id=userpk).profileimage.path)):
                    os.remove(model.objects.get(id=userpk).profileimage.path)
            myfile = self.request.FILES['profileimage']
            fs = FileSystemStorage()
            filename = fs.save('{0}/{1}'.format(userpk,myfile.name), myfile)
            model.objects.filter(id=userpk).update(profileimage='{0}/{1}'.format(userpk, data['profileimage']))
        return super().form_valid(form)
    
class SecuritySettingsView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        type = get_user_model().objects.get(id=self.request.user.id).type
        return render(request,"account/security-settings.html",{"type": type})

    def post(self, request, *args, **kwargs):
        userpk = request.user.pk
        model = get_user_model()
        if("currentPassword" in request.POST):
            user = authenticate(request, username=request.user.username, password=request.POST.get("currentPassword", ""))
            if user is not None:
                if(request.POST.get("newPassword", "") == request.POST.get("confirmPassword", "")):
                    u = model.objects.get(id=userpk)
                    u.set_password(request.POST.get("newPassword", ""))
                    u.save()
                    return HttpResponseRedirect(reverse('login'))
        elif("deleter" in request.POST):
            u = model.objects.get(id=userpk)
            u.delete()
            return HttpResponseRedirect(reverse('login'))
        elif("radioPrivacy" in request.POST):
            typ = 0
            if(request.POST.get("radioPrivacy") == "1"):
                typ = 1
            elif(request.POST.get("radioPrivacy") == "0"):
                typ = 0
            updateuser = get_user_model().objects.get(id=self.request.user.id)
            updateuser.type = typ
            updateuser.save()
            return HttpResponseRedirect(reverse('securitysettings'))
        return render(request,"account/security-settings.html")

class BillingSettingsView(LoginRequiredMixin, TemplateView):
    template_name = "account/billing-settings.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        var1 = SavedAddress.objects.all().filter(owner=self.request.user)
        var2 = SavedPayment.objects.all().filter(owner=self.request.user)
        context.update({'addresses': var1,'payments':var2})
        return context
    
class AddAddressView(LoginRequiredMixin, FormView):
    model = SavedAddress
    form_class = SavedAddressForm
    template_name = "account/addadress.html"
    
    def form_valid(self, form):
        if(self.request.user.is_authenticated):
            finform = form.save(commit=False)
            finform.owner=self.request.user
            finform.save()
            return super().form_valid(form)
    
    def get_success_url(self):
        if(self.request.user.type == 0):
            return reverse('billsettings')
        else:
            return reverse('billingsettings')
        
class EditAddressView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = SavedAddress
    form_class = SavedAddressForm
    template_name = "account/addadress.html"
    
    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user
    
    def get_initial(self):
        addressinfo = self.get_object()
        initial = super().get_initial()
        initial['name'] = addressinfo.name
        initial['email'] = addressinfo.email
        initial['phone'] = addressinfo.phone
        initial['address'] = addressinfo.address
        initial['country'] = addressinfo.country
        initial['city'] = addressinfo.city
        initial['zipcode'] = addressinfo.zipcode
        return initial
    
    def form_valid(self, form):
        if(self.request.user.is_authenticated):
            finform = form.save(commit=False)
            finform.owner=self.request.user
            finform.save()
            return super().form_valid(form)
            
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)
    
    def get_success_url(self):
        if(self.request.user.type == 0):
            return reverse('billsettings')
        else:
            return reverse('billingsettings')

class AddPaymentView(LoginRequiredMixin, FormView):
    model = SavedPayment
    form_class = SavedPaymentForm
    template_name = "account/addpayment.html"
    
    def form_valid(self, form):
        if(self.request.user.is_authenticated):
            finform = form.save(commit=False)
            finform.owner=self.request.user
            if(self.request.POST.get("pay-method") == "creditcard"):
                finform.type = 0
                if(form.cleaned_data['cardnumber'] == "" or form.cleaned_data['cardname'] == "" or form.cleaned_data['cardexp'] == "" or form.cleaned_data['cardcvv'] == ""):
                    return super().form_invalid(form)
                else:
                    finform.save()
                    return super().form_valid(form)
            elif(self.request.POST.get("pay-method") == "paypal"):
                finform.type = 1
                if(form.cleaned_data['paypalemail'] == ""):
                    return super().form_invalid(form)
                else:
                    finform.save()
                    return super().form_valid(form)
            else:
                return super().form_invalid(form)
    
    def get_success_url(self):
        if(self.request.user.type == 0):
            return reverse('billsettings')
        else:
            return reverse('billingsettings')
        
class EditPaymentView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = SavedPayment
    form_class = SavedPaymentForm
    template_name = "account/addpayment.html"
    
    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user
    
    def get_initial(self):
        paymentinfo = self.get_object()
        initial = super().get_initial()
        initial['cardnumber'] = paymentinfo.cardnumber
        initial['cardname'] = paymentinfo.cardname
        initial['cardexp'] = paymentinfo.cardexp
        initial['cardcvv'] = paymentinfo.cardcvv
        initial['paypalemail'] = paymentinfo.paypalemail
        return initial
    
    def form_valid(self, form):
        if(self.request.user.is_authenticated):
            finform = form.save(commit=False)
            finform.owner=self.request.user
            if(self.request.POST.get("pay-method") == "creditcard"):
                finform.type = 0
                if(form.cleaned_data['cardnumber'] == "" or form.cleaned_data['cardname'] == "" or form.cleaned_data['cardexp'] == "" or form.cleaned_data['cardcvv'] == ""):
                    return super().form_invalid(form)
                else:
                    finform.save()
                    return super().form_valid(form)
            elif(self.request.POST.get("pay-method") == "paypal"):
                finform.type = 1
                if(form.cleaned_data['paypalemail'] == ""):
                    return super().form_invalid(form)
                else:
                    finform.save()
                    return super().form_valid(form)
            else:
                return super().form_invalid(form)
            
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)
    
    def get_success_url(self):
        if(self.request.user.type == 0):
            return reverse('billsettings')
        else:
            return reverse('billingsettings')

class BillSettingsView(LoginRequiredMixin, TemplateView):
    template_name = "account/bill-settings.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        var1 = SavedAddress.objects.all().filter(owner=self.request.user)
        var2 = SavedPayment.objects.all().filter(owner=self.request.user)
        var3 = CheckoutModel.objects.all().filter(owner=self.request.user)
        context.update({'addresses': var1,'payments':var2,'billinghistory':var3})
        return context
    
class MyWishlistView(LoginRequiredMixin, ListView):
    template_name = "account/wishlist.html"
    
    def get_queryset(self):
        page = self.request.GET.get('page', 1)
        tag = Wishlist.objects.all().filter(owner=self.request.user)
        paginator = Paginator(tag, 6)
        tag = paginator.page(page)
        return tag
        
class PlanView(LoginRequiredMixin, FormView):
    model = get_user_model()
    form_class = PlanForm
    template_name = "account/plan.html"
    
    def form_valid(self, form):
        if(self.request.user.is_authenticated):
            if(self.request.POST.get("plan-name") == "1"):
                self.model.objects.filter(pk=self.request.user.pk).update(plan=1)
            elif(self.request.POST.get("plan-name") == "2"):
                self.model.objects.filter(pk=self.request.user.pk).update(plan=2)
            elif(self.request.POST.get("plan-name") == "3"):
                self.model.objects.filter(pk=self.request.user.pk).update(plan=3)
            else:
                self.model.objects.filter(pk=self.request.user.pk).update(plan=1)
            return super().form_valid(form)
    
    def get_success_url(self):
        if(self.request.user.type == 0):
            return reverse('billsettings')
        else:
            return reverse('billingsettings')
