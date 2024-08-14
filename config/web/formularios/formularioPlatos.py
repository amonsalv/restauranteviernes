from django import forms

class FormularioRegistroPlatos(forms.Form):

    PLATOS=(  
        (1, 'Entrada'),
        (2, 'Plato Fuerte'),
        (3, 'Postres'),
        (4, 'Bebidas')
    )

    nombrePlato=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=5,
        required=True,
        label="Nombre del Plato"
    )
    descripcionPlato=forms.CharField(
        widget=forms.Textarea(attrs={"class":"form-control mb-3"}),
        max_length=50,
        required=True,
        label="Descripción del Plato"
    )
    fotoPlato=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=200,
        required=True,
        label="Foto del Plato"
    )
    precioPlato=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        label="Precio del Plato"
    )
    tipoPlato=forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-control mb-3"}),
        choices=PLATOS,
        required=True,
        label="Tipo de Plato"
    )

    