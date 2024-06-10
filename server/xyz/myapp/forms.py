from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_code', 'description', 'unit_price', 'categories', 'details', 'stockquantity']

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description:
            raise forms.ValidationError('Description should not be empty.')
        return description

    def clean_unit_price(self):
        unit_price = self.cleaned_data.get('unit_price')
        if unit_price is None or unit_price <= 0:
            raise forms.ValidationError('Unit price must be a positive number.')
        return unit_price

    def clean_stockquantity(self):
        stockquantity = self.cleaned_data.get('stockquantity')
        if stockquantity is None or stockquantity < 0:
            raise forms.ValidationError('Stock quantity cannot be negative.')
        return stockquantity
