from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "inicio.html")

def facilities(request):
    context = {
        "imagenes": [
            {"img":"img/facilities/instalaciones_01.webp","titulo":"example 1"},
            {"img":"img/facilities/instalaciones_02.webp","titulo":"example 2"},
            {"img":"img/facilities/instalaciones_03.webp","titulo":"example 3"},
            {"img":"img/facilities/instalaciones_04.webp","titulo":"example 4"},
            {"img":"img/facilities/instalaciones_05.webp","titulo":"example 5"},
            {"img":"img/facilities/instalaciones_06.webp","titulo":"example 5"},
            ],
        "cards":[
            {"title":"sevicios nauticos","img":"img/facilities/instalaciones_01.webp","comentario":"¡Explora las maravillas del mar con nuestra gama de servicios náuticos! Desde emocionantes paseos en motos acuáticas hasta relajantes viajes en lancha y barco, tenemos todo lo que necesitas para una experiencia inolvidable en el agua. ¡Prepárate para navegar hacia la diversión y la aventura!"},
            {"title":"Explora ESPA","img":"img/facilities/instalaciones_04.webp","comentario":"Descubre la tranquilidad y el encanto de nuestro oasis ESPA. Un lugar donde el bienestar y la relajación te esperan en cada rincón. ¡Sumérgete en una experiencia rejuvenecedora que te dejará renovado y revitalizado!"},
            {"title":"Habitaciones de Lujo","img":"img/facilities/instalaciones_05.webp","comentario":"Sumérgete en la opulencia y el confort con nuestras Habitaciones de Lujo. Cada detalle ha sido diseñado con elegancia para brindarte una experiencia de alojamiento excepcional. Disfruta de una estancia inolvidable en un entorno de lujo y comodidad incomparables."},
            {"title":"Ambientes Climatizados","img":"img/facilities/instalaciones_05.webp","comentario":"Relájate y sumérgete en la comodidad de nuestros Ambientes Climatizados, donde disfrutarás de la frescura y la relajación constante de una piscina cerrada. Un refugio perfecto para escapar del calor y disfrutar de un ambiente agradable en cualquier época del año. ¡Tu oasis personal de serenidad!"},
            {"title":"Ambientes Climatizados","img":"img/facilities/instalaciones_05.webp","comentario":"Relájate y sumérgete en la comodidad de nuestros Ambientes Climatizados, donde disfrutarás de la frescura y la relajación constante de una piscina cerrada. Un refugio perfecto para escapar del calor y disfrutar de un ambiente agradable en cualquier época del año. ¡Tu oasis personal de serenidad!"},
            {"title":"Habitaciones de Lujo","img":"img/facilities/instalaciones_05.webp","comentario":"Sumérgete en la opulencia y el confort con nuestras Habitaciones de Lujo. Cada detalle ha sido diseñado con elegancia para brindarte una experiencia de alojamiento excepcional. Disfruta de una estancia inolvidable en un entorno de lujo y comodidad incomparables."},
        ]
    }



    return render(request, "./facilities/facilities.html", context)