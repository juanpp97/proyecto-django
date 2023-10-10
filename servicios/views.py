from django.shortcuts import render
from .models import Eventos
# Create your views here.

def servicios_adicionales (request):
   

    comidas = (
            {'imagen': ['roomservice/img_comidas/comida_1.webp','roomservice/img_comidas/comida_2.webp'],
             'titulo' : ['Platos de Autor', 'Opciones Rapidas' ],
             'descripcion': 'Platos con la variedad de comidas directo de nuestra cocina a tu habitación',
             'opciones':['Bistec de Costilla','Bistec de Solomillo de Primera', 'Bistec de Lomo de Primera', 'Bistec de Solomillo de Wagyu']})
    
    bebidas = (
            {'imagen': ['roomservice/img_bebidas/bebidas_6.webp','roomservice/img_bebidas/bebida_9.webp'],
             'titulo' : ['Cocteles y Tragos', 'Whiskeys' ],
             'descripcion': ['Explora nuestra cartilla con los mejores tragos para acompañar la estadía','Apartado dedicado a los amantes del whisky y sus variedades.',],
             'opciones':['Classic Mojito','Royal Martini','Fernet con Coca','Daiquiri','Retro Margarita','Dry Fruit Mojito','Classic Margarita','Manhattan','Whiskey Sour','Bourbon Flip', 'Old Fashioned', 'Paper Plane', 'Gin FIzz']})
    
    cafeteria = (
             {'imagen': ['roomservice/img_cafe/bakery.webp','roomservice/img_cafe/cofee.webp','roomservice/img_cafe/noncofee.webp','roomservice/img_cafe/smoothie.webp'],
             'titulo' : ['Cofee', 'Non-Cofee','Smoothie','Bakery and pastry' ],
             'descripcion': ['En esta categoría encontrarás bebidas calientes que contienen café.','También te podemos ofrecer té, refrescos y agua.','Batidos cremosos elaborados a partir de fruta o vegetal, natural o congelados, con yogur, helado o leche', 'Podés agregar a tu pedido algún producto de panadería y pastelería como tostadas, facturas o tortas.'],
             'opciones':['Pink Smoothie','Banana Smoothie', 'Matcha Cream', 'Lettuce Smoothie', 'Apple smoothie' , 'Berry Smoothie', 'Lemon Smoothie', 'Medialuna', 'Croissant', 'Macaron', 'Pastafrola', 'Apple crumble', 'Lemon Pie', 'Tostadas']})
    

    contexto = {'lista_comida' : comidas,
                'lista_bebida' : bebidas,
                'lista_cafeteria' : cafeteria}


    return render (request, 'servicios/servicios_adic.html', contexto)



def actividades(request):
    model = Eventos
    contexto = {
        "list_eventos": model.objects.all()
    }
    return render (request, 'servicios/actividades.html',contexto)