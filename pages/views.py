from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from django.views.generic.edit import FormMixin
from products.models import Product, Comment, Wishlist
from products.forms import CommentForm, ProductForm, FiltersForm
from mycart.forms import CheckoutForm
from accountsettings.models import SavedPayment, SavedAddress 
import datetime
from django.core.paginator import Paginator
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
import os
import shutil
from django.conf import settings

class HomePageView(FormMixin, ListView):
    template_name = "home.html"
    form_class = FiltersForm
    
    def get_form_kwargs(self):
        prices = self.request.GET.get('prices')
        categories = self.request.GET.get('categorys')
        frominput = self.request.GET.get('frominput')
        toinput = self.request.GET.get('toinput')
        form_kwargs = super().get_form_kwargs()
        if(prices == "Other"):
            form_kwargs['request'] = "0"
        else:
            form_kwargs['request'] = "1"
        return form_kwargs
    
    def get_initial(self):
        prices = self.request.GET.get('prices')
        categories = self.request.GET.get('categorys')
        frominput = self.request.GET.get('frominput')
        toinput = self.request.GET.get('toinput')
        initial = super().get_initial()
        initial['categorys'] = categories
        if(prices == None):
            initial['prices'] = 'AP'
        else:
            initial['prices'] = prices
        initial['frominput'] = frominput
        initial['toinput'] = toinput
        return initial
    
    def get_queryset(self):
        page = self.request.GET.get('page', 1)
        searchquery = self.request.GET.get('search')
        usernamequery = self.request.GET.get('username')
        if(searchquery == None):
            searchqueryfinal = ""
        else:
            searchqueryfinal = searchquery
        prices = self.request.GET.get('prices')
        categories = self.request.GET.get('categorys')
        frominput = self.request.GET.get('frominput')
        toinput = self.request.GET.get('toinput')
        orderfin = "id"
        order = self.request.GET.get('order')
        if(order == None or order == "popular"):
            orderfin = "id"
        elif(order == "pricel"):
            orderfin = "price"
        elif(order == "priceh"):
            orderfin = "-price"
        if(usernamequery != None):
            tag = Product.objects.all().filter(owner=get_user_model().objects.get(pk=usernamequery))
        if(categories == None and prices == None):
            tag = Product.objects.all().filter(name__contains=searchqueryfinal).order_by(orderfin)
        elif(categories == None):
            if(prices == "AP"):
                tag = Product.objects.all().filter(name__contains=searchqueryfinal).order_by(orderfin)
            elif(prices == "25"):
                tag = Product.objects.all().filter(price__lte=25,name__contains=searchqueryfinal).order_by(orderfin)
            elif(prices == "2550"):
                tag = Product.objects.all().filter(price__range=(25,50),name__contains=searchqueryfinal).order_by(orderfin)
            elif(prices == "50100"):
                tag = Product.objects.all().filter(price__range=(50,100),name__contains=searchqueryfinal).order_by(orderfin)
            elif(prices == "Other"):
                tag = Product.objects.all().filter(price__range=(frominput,toinput),name__contains=searchqueryfinal).order_by(orderfin)
        elif(prices == None):
            if(categories == None or categories == "SA"):
                tag = Product.objects.all().filter(name__contains=searchqueryfinal).order_by(orderfin)
            else:
                tag = Product.objects.all().filter(categorys=categories,name__contains=searchqueryfinal).order_by(orderfin)
        else:
            if(categories == "SA"):
                if(prices == "AP"):
                    tag = Product.objects.all().filter(name__contains=searchqueryfinal).order_by(orderfin)
                elif(prices == "25"):
                    tag = Product.objects.all().filter(price__lte=25,name__contains=searchqueryfinal).order_by(orderfin)
                elif(prices == "2550"):
                    tag = Product.objects.all().filter(price__range=(25,50),name__contains=searchqueryfinal).order_by(orderfin)
                elif(prices == "50100"):
                    tag = Product.objects.all().filter(price__range=(50,100),name__contains=searchqueryfinal).order_by(orderfin)
                elif(prices == "Other"):
                    tag = Product.objects.all().filter(price__range=(frominput,toinput),name__contains=searchqueryfinal).order_by(orderfin)
            else:
                if(prices == "AP"):
                    tag = Product.objects.all().filter(categorys=categories,name__contains=searchqueryfinal).order_by(orderfin)
                elif(prices == "25"):
                    tag = Product.objects.all().filter(price__lte=25,categorys=categories,name__contains=searchqueryfinal).order_by(orderfin)
                elif(prices == "2550"):
                    tag = Product.objects.all().filter(price__range=(25,50),categorys=categories,name__contains=searchqueryfinal).order_by(orderfin)
                elif(prices == "50100"):
                    tag = Product.objects.all().filter(price__range=(50,100),categorys=categories,name__contains=searchqueryfinal).order_by(orderfin)
                elif(prices == "Other"):
                    tag = Product.objects.all().filter(price__range=(frominput,toinput),categorys=categories,name__contains=searchqueryfinal).order_by(orderfin)
        paginator = Paginator(tag, 6)
        tag = paginator.page(page)
        return tag
        
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)  
        var1 = []
        var2 = []
        for key, value in self.request.GET.items():
            var1.append(key)
            var2.append(value)
        context.update({'keys': var1,'values':var2})
        return context

class ProductPageViewGet(DetailView):
    model = Product
    template_name = "product-details.html"
    
    def get_context_data(self, **kwargs): 
        starsaverage = []
        var1 = []
        var2 = []
        for timeof in Comment.objects.filter(product=self.get_object()):
            starsaverage.append(timeof.stars)
            date = datetime.datetime.now(datetime.timezone.utc) - timeof.timeof
            dateseconds = date.seconds
            days = dateseconds / 86400
            if(days < 1):
                hours = dateseconds / 3600
                if(hours < 1):
                    minutes = dateseconds / 60
                    if(minutes < 1):
                        var1.append(int(dateseconds))
                        var2.append("seconds")
                    else:
                        var1.append(int(minutes))
                        var2.append("minutes")
                else:
                    var1.append(int(hours))
                    var2.append("hours")
            else:
                var1.append(int(days))
                var2.append("days")
        if(len(starsaverage) > 0):
            starsaveragefinal = int(sum(starsaverage)/len(starsaverage))
        else:
            starsaveragefinal = 0
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["comments"] = Comment.objects.filter(product=self.get_object())
        context["timelapsed"] = var1
        context["days"] = var2
        context["starsaverage"] = starsaveragefinal
        if(self.request.user.is_authenticated):
            if(len(Wishlist.objects.all().filter(owner=self.request.user,product=self.get_object())) == 0):
                context["wishlish"] = 0
            else:
                context["wishlish"] = 1
        return context
        
class ProductPageViewPost(LoginRequiredMixin, FormView):
    model = Product
    form_class = CommentForm
    template_name = "home.html"
    success_url = '.'
    
    def form_invalid(self,form):
        if(self.request.user.is_authenticated):
            if(self.request.POST.get("productid") != None):
                if(len(Wishlist.objects.all().filter(owner=self.request.user,product=Product.objects.all().get(pk=self.request.POST.get("productid")))) == 0):
                    Wishlist.objects.create(owner=self.request.user,product=Product.objects.all().get(pk=self.request.POST.get("productid")))
                    return HttpResponseRedirect(self.get_success_url())
                else:
                    Wishlist.objects.filter(owner=self.request.user,product=Product.objects.all().get(pk=self.request.POST.get("productid"))).delete()
                    return HttpResponseRedirect(self.get_success_url())
            return HttpResponseRedirect(reverse("home"))
    
    def form_valid(self, form):
        if(self.request.user.is_authenticated):
            finform = form.save(commit=False)
            finform.product=Product.objects.get(pk=self.request.POST.get("iidd"))
            finform.owner=self.request.user
            finform.save()
            return super().form_valid(form)
        
    def get_success_url(self):
        if(self.request.POST.get("productid") == None):
            return reverse('productdetails', kwargs={'pk': self.request.POST.get("iidd")})
        else:
            return reverse('productdetails', kwargs={'pk': self.request.POST.get("productid")})
    
    
class ProductPageView(View):
    def get(self, request, *args, **kwargs):
        view = ProductPageViewGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):  
        view = ProductPageViewPost.as_view()
        return view(request, *args, **kwargs)
    
class AddProductView(LoginRequiredMixin, FormView):
    model = Product
    form_class = ProductForm
    template_name = "addproduct.html"
    success_url = '.'
    
    def form_valid(self, form):
        finform = form.save(commit=False)
        finform.certified=0
        finform.owner=self.request.user
        finform.save()
        instancerefid = finform.id
        instanceref = Product.objects.get(id=instancerefid)
        if(finform.image == None):
            if(os.path.exists(str(os.path.join(settings.BASE_DIR,"data/media/"))+'{0}/{1}/'.format(instanceref.owner.id, instanceref.pk))):
                shutil.copyfile(str(os.path.join(settings.BASE_DIR,"data/media/not.png")), str(os.path.join(settings.BASE_DIR,"data/media/"))+'{0}/{1}/{2}'.format(instanceref.owner.id, instanceref.pk, "not.png"))
            else:
                os.makedirs(str(os.path.join(settings.BASE_DIR,"data/media/"))+'{0}/{1}/'.format(instanceref.owner.id, instanceref.pk))
                shutil.copyfile(str(os.path.join(settings.BASE_DIR,"data/media/not.png")), str(os.path.join(settings.BASE_DIR,"data/media/"))+'{0}/{1}/{2}'.format(instanceref.owner.id, instanceref.pk, "not.png"))
            Product.objects.filter(id=instanceref.id).update(image='{0}/{1}/{2}'.format(instanceref.owner.id, instanceref.pk, "not.png"))
        return super().form_valid(form)
        
class EditProductView(LoginRequiredMixin, UserPassesTestMixin, SingleObjectMixin, FormView):
    model = Product
    form_class = ProductForm
    template_name = "editproduct.html"
    success_url = '.'
    
    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user
    
    def get_initial(self):
        productinfo = self.get_object()
        initial = super().get_initial()
        initial['name'] = productinfo.name
        initial['price'] = productinfo.price
        initial['description'] = productinfo.description
        initial['specifications'] = productinfo.specifications
        initial['deliverytime'] = productinfo.deliverytime
        initial['categorys'] = productinfo.categorys
        return initial
        
    def updateimages(self, imageref, path, fil):
        productid = self.get_object().id
        if(imageref != None):
            if(os.path.exists(path)):
                os.remove(path)
            myfile = fil
            fs = FileSystemStorage()
            filename = fs.save('{0}/{1}/{2}'.format(self.get_object().owner.id,productid,myfile.name), myfile)
        Product.objects.filter(id=productid).update(image='{0}/{1}/{2}'.format(self.get_object().owner.id,productid, imageref))
    
    def form_valid(self, form):
        productid = self.get_object().id
        finform = form.save(commit=False)
        objectinstance = Product.objects.get(pk=productid)
        finform2 = self.form_class(form.cleaned_data, instance=objectinstance)
        finform2.save()
        if("image" in self.request.FILES):
            self.updateimages(form.cleaned_data['image'],Product.objects.get(id=productid).image.path,self.request.FILES['image'])
        if("image2" in self.request.FILES):
            self.updateimages(form.cleaned_data['image2'],Product.objects.get(id=productid).image2.path,self.request.FILES['image2'])
        if("image3" in self.request.FILES):
            self.updateimages(form.cleaned_data['image3'],Product.objects.get(id=productid).image3.path,self.request.FILES['image3'])
        return super().form_valid(form)
        
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)
        
    def get_success_url(self):
        return reverse('productdetails', kwargs={'pk': self.get_object().id})
        
class CartView(LoginRequiredMixin, TemplateView):
    template_name = "cart.html"
    
class CheckoutView(LoginRequiredMixin, FormView):
    template_name = "checkout.html"
    model = Product
    form_class = CheckoutForm
    success_url = '.'

    def get_initial(self):
        initial = super().get_initial()
        addressvalues = SavedAddress.objects.all().filter(owner=self.request.user).first()
        creditcardvalues = SavedPayment.objects.all().filter(owner=self.request.user,type=0).first()
        paypalvalues = SavedPayment.objects.all().filter(owner=self.request.user,type=1).first()
        if(addressvalues == None):
            initial['name'] = self.request.user.username
            initial['email'] = self.request.user.email
        else:
            initial['name'] = addressvalues.name
            initial['email'] = addressvalues.email
            initial['phone'] = addressvalues.phone
            initial['address'] = addressvalues.address
            initial['country'] = addressvalues.country
            initial['city'] = addressvalues.city
            initial['zipcode'] = addressvalues.zipcode
        if(creditcardvalues != None):
            initial['cardnumber'] = creditcardvalues.cardnumber
            initial['cardname'] = creditcardvalues.cardname
            initial['cardexp'] = creditcardvalues.cardexp
            initial['cardcvv'] = creditcardvalues.cardcvv
        if(paypalvalues != None):
            initial['paypalemail'] = paypalvalues.paypalemail
        return initial
        
    def form_valid(self, form):
        finform = form.save(commit=False)
        if(self.request.user.is_authenticated):
            finform.owner=self.request.user
        if(form.cleaned_data['paymentmethods'] == "creditcard"):
            if(form.cleaned_data['cardnumber'] == "" or form.cleaned_data['cardname'] == "" or form.cleaned_data['cardexp'] == "" or form.cleaned_data['cardcvv'] == ""):
                return super().form_invalid(form)
            else:
                finform.save()
                return super().form_valid(form)
        elif(form.cleaned_data['paymentmethods'] == "paypal"):
            if(form.cleaned_data['paypalemail'] == ""):
                return super().form_invalid(form)
            else:
                finform.save()
                return super().form_valid(form)
        else:
            finform.save()
            return super().form_valid(form)

