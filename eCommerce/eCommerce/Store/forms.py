from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']


class FilterForm(forms.Form):

    order_tuple = [
    ('Alphabetically', (
            ('aa', 'Ascending'),
            ('ad', 'Decending'),
        )
    ),
    ('Numerically', (
            ('na', 'Ascending'),
            ('nd', 'Decending'),
        )
    )
    ]

    type_tuple = [

        ('sneakers','Sneakers'),
        ('boots', 'Boots'),
        ('shoes', 'shoes'),
        ('any','Any')
    ]

    color_tuple = [
        ('black','Black'),
        ('red', 'Red'),
        ('violet','Violet'),
        ('brown', 'Brown'),
        ('gray', 'Gray'),
        ('white', 'White'),
        ('celeste', 'Celeste'),
        ('pink', 'Pink'),
            ('any','Any')
    ]

    type = forms.ChoiceField(label="Type", choices=type_tuple)
    color = forms.ChoiceField(label="Contains color", choices=color_tuple)
    price_below = forms.FloatField(label="Price is below", required=False)
    order = forms.ChoiceField(label="Order by", choices=order_tuple)

    class Meta:
        fields = ('type', 'color', 'price_below', 'order')
        widgets = {'type': forms.Select(attrs={'id': 'my_HTML_id', 'class': 
                   'form_type'})}

