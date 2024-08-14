from django.shortcuts import render

from web.formularios.formularioPlatos import FormularioRegistroPlatos

# Create your views here.

#CADA VISTA ES UNA FUNCION DE PY

def Home(request):
    return render(request,'index.html')

def Platos(request):

    #cargar el formulario de registro de platos
    formulario=FormularioRegistroPlatos()

    #Creamos un diccionario para enviar datos hacia el template
    diccionarioEnvioDatos={
        'formulario':formulario
    }
    
    #Recibiendo datos del formulario
    #PETICION DE TIPO POST
    if request.method=='POST':
        datosFormulario=FormularioRegistroPlatos(request.POST)
        if datosFormulario.is_valid():
            datosLimpios=datosFormulario.cleaned_data
            print(datosLimpios)

    return render(request,'platos.html',diccionarioEnvioDatos)