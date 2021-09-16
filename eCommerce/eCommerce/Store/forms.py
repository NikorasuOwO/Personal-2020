from django import forms

class FilterForm(forms.Form):

    usage = forms.TypedChoiceField(label="Usage")
    color = forms.TypedChoiceField(label="Contains color")
    price_below = forms.FloatField(label="Price is below")
    order = forms.TypedChoiceField(label="Order by")