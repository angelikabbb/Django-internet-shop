from django import forms

# QUANTITY_CHOICES = [(i, str(i) for i in range(1, 10))]
# color = [
#     ('red': '',
#      'blue': '',
#      'black': ,
#     )
# ]

class CartAddProductForm(forms.Form):

    quantity = forms.IntegerField(
        max_value= 1000,
        min_value= 1,
        label='Количество',
        widget=forms.NumberInput(attrs={'style': 'width:80px', 'id':'quantity', 'onchange':'sendCount(this)'}),
        initial=1
        )
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    
    # quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, coerce=int, label='Количество')
    # quantity = forms.IntegerField(max_value=1000, label='Количество')
    # override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput )