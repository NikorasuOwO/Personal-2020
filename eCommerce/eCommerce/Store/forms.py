from django import forms

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

    usage_tuple = [

        ('running','Running'),
        ('hiking', 'Hiking')
    ]

    color_tuple = [
        ('black','Black'),
        ('red', 'Red'),
        ('violet','Violet'),
        ('brown', 'Brown'),
        ('gray', 'Gray'),
        ('white', 'White'),
        ('celeste', 'Celeste')
    ]

    usage = forms.ChoiceField(label="Usage", choices=usage_tuple)
    color = forms.ChoiceField(label="Contains color", choices=color_tuple)
    price_below = forms.FloatField(label="Price is below")
    order = forms.ChoiceField(label="Order by", choices=order_tuple)