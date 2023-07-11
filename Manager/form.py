from django import forms
from django.forms import ModelForm, fields
from .models import *

categories = (
    ('January' , 'January'),
    ('February' , 'February'),
    ('March' , 'March'),
    ('April' , 'April'),
    ('May' , 'May'),
    ('June' , 'June'),
    ('July' , 'July'),
    ('August' , 'August'),
    ('September' , 'September'),
    ('October' , 'October'),
    ('November' , 'November'),
    ('December' , 'December'),
    ('Advance' , 'Advance')
)

class choicesform(forms.Form):
    tag = forms.MultipleChoiceField( choices=categories)
    
class Customerform(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class Productsform(ModelForm):
    class Meta:
        model = Products
        fields = '__all__'

class Orderform(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class Receiptform(ModelForm):
    class Meta:
        model = Receipt
        fields = '__all__'

class Installmentform(ModelForm):
    class Meta:
        model = Installment
        fields = '__all__'