from django import forms
from .models import Comment, Product
from django_starfield import Stars
from .renderer import CustomRadioSelect

class FiltersForm(forms.Form):
    CATEGORIES = [
        ('SA', 'Show All'),
        ('Art', 'Art'),
        ('Baby', 'Baby'),
        ('Books', 'Books'),
        ('BI', 'Business & Industrial'),
        ('CP', 'Cameras & Photo'),
        ('CPA', 'Cell Phones & Accessories'),
        ('CSA', 'Clothing, Shoes & Accessories'),
        ('CTN', 'Computers/Tablets & Networking'),
        ('CE', 'Consumer Electronics'),
        ('Crafts', 'Crafts'),
        ('DB', 'Dolls & Bears'),
        ('DM', 'DVDs & Movies'),
        ('GCC', 'Gift Cards & Coupons'),
        ('HB', 'Health & Beauty'),
        ('HG', 'Home & Garden'),
        ('JW', 'Jewelry & Watches'),
        ('Music', 'Music'),
        ('MIG', 'Musical Instruments & Gear'),
        ('PS', 'Pet Supplies'),
        ('PG', 'Pottery & Glass'),
        ('RE', 'Real Estate'),
        ('SS', 'Specialty Services'),
        ('SG', 'Sporting Goods'),
        ('SMCFS', 'Sports Mem, Cards & Fan Shop'),
        ('TE', 'Tickets & Experiences'),
        ('TH', 'Toys & Hobbies'),
        ('Travel', 'Travel'),
        ('VGC', 'Video Games & Consoles'),
        ('EE', 'Everything Else')
    ]
    PRICEOPTIONS = [
        ('AP', 'All Prices'),
        ('25', 'Under $25'),
        ('2550','$25 to $50'),
        ('50100','$50 to $100'),
        ('Other','Other (specify)'),
    ]
    categorys = forms.ChoiceField(widget=forms.Select(attrs={'class':'btn btn-primary dropdown-toggle'}), choices=CATEGORIES)
    prices = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'radio'}), choices=PRICEOPTIONS, initial=PRICEOPTIONS[0][0])
    frominput = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'shop-filter-price_from','min':'0','class':'form-control','placeholder':'From'}))
    toinput = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'shop-filter-price_to','min':'0','class':'form-control','placeholder':'To'}))
    
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request','1')
        super(FiltersForm, self).__init__(*args, **kwargs)
        if request == "1":
            self.fields['frominput'].widget.attrs.update({'disabled': 'true'})
            self.fields['toinput'].widget.attrs.update({'disabled': 'true'})

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"rows":"2", "class":"form-control", "placeholder": "Write a review"}), required=True)
    stars = forms.IntegerField(widget=Stars,required=True)
    image1 = forms.ImageField(widget=forms.FileInput(attrs={'style':'display: none;'}),required=False)
    
    class Meta:
        model = Comment
        fields = ("body","stars","image1")
        
class ProductForm(forms.ModelForm):
    CATEGORIES = [
        ('EE', 'Everything Else'),
        ('Art', 'Art'),
        ('Baby', 'Baby'),
        ('Books', 'Books'),
        ('BI', 'Business & Industrial'),
        ('CP', 'Cameras & Photo'),
        ('CPA', 'Cell Phones & Accessories'),
        ('CSA', 'Clothing, Shoes & Accessories'),
        ('CTN', 'Computers/Tablets & Networking'),
        ('CE', 'Consumer Electronics'),
        ('Crafts', 'Crafts'),
        ('DB', 'Dolls & Bears'),
        ('DM', 'DVDs & Movies'),
        ('GCC', 'Gift Cards & Coupons'),
        ('HB', 'Health & Beauty'),
        ('HG', 'Home & Garden'),
        ('JW', 'Jewelry & Watches'),
        ('Music', 'Music'),
        ('MIG', 'Musical Instruments & Gear'),
        ('PS', 'Pet Supplies'),
        ('PG', 'Pottery & Glass'),
        ('RE', 'Real Estate'),
        ('SS', 'Specialty Services'),
        ('SG', 'Sporting Goods'),
        ('SMCFS', 'Sports Mem, Cards & Fan Shop'),
        ('TE', 'Tickets & Experiences'),
        ('TH', 'Toys & Hobbies'),
        ('Travel', 'Travel'),
        ('VGC', 'Video Games & Consoles')
    ]
    DELIVERTIME = [
        ('1-3 Days', '1-3 Days'),
        ('1 Week', '1 Week'),
        ('15 Days', '15 Days'),
        ('1 Month', '1 Month')
    ]
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),max_length=100)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':'5','class':'form-control'}),max_length=5000,required=False)
    specifications = forms.CharField(widget=forms.Textarea(attrs={'rows':'5','class':'form-control'}),max_length=5000,required=False)
    deliverytime = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=DELIVERTIME)
    price = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','step':'0.01','type':'number'}))
    categorys = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=CATEGORIES)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}),required=False)
    image2 = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}),required=False)
    image3 = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}),required=False)
    
    class Meta:
        model = Product
        fields = ("name","description","specifications","deliverytime","price","categorys","image","image2","image3")
