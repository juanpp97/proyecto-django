from django.shortcuts import render
from datetime import datetime

def index(request):
    context = {
        "date": datetime.now(),
        "active": "index",
    }
    return render(request, "reservas/inicio.html", context)

def rooms(request):
    rooms = [
        {
        "id": 1,
        "nombre": "Habitación Individual", 
         "capacidad": 1, 
         "Num_camas": "1 cama simple", 
         "vista": "Frente", 
         "AC": "Si",
         "TV": "Si",
         "precio_alta": 30_000, 
         "precio_media": 40_000, 
         "precio_alta": 50_000, 
         "imgs": ["individual1.webp", "individual2.webp", "individual3.webp", "individual4.webp"],
         "range": range(0,4),
         },

         {"id": 2,
          "nombre": "Habitación Doble Clásica", 
         "capacidad": 2, 
         "Num_camas": "2 camas simples", 
         "vista": "Playa",
         "AC": "Si",
         "TV": "Si",
         "precio_alta": 40_000, 
         "precio_media": 50_000, 
         "precio_alta": 60_000, 
         "imgs": ["doble1.webp", "doble2.webp", "doble3.webp"],
         "range": range(0,3),
         },

         {"id": 3,
        "nombre": "Habitación Matrimonial", 
         "capacidad": 2, 
         "Num_camas": "1 cama doble", 
         "vista": "Playa o Frente", 
         "AC": "Si",
         "TV": "Si",
         "precio_alta": 30_000, 
         "precio_media": 40_000, 
         "precio_alta": 50_000, 
         "imgs": ["matrimonial1.webp", "matrimonial2.webp", "matrimonial3.webp"],
         "range": range(0,3),
         },

         {"id": 4,
        "nombre": "Habitación Triple",
         "capacidad": 3, 
         "Num_camas": "3 camas simples", 
         "vista": "Playa o Frente",
         "AC": "Si",
         "TV": "Si",
         "precio_alta": 40_000, 
         "precio_media": 50_000, 
         "precio_alta": 60_000, 
         "imgs": ["triple1.webp", "triple2.webp", "triple3.webp"],
         "range": range(0,3),
         },

         {"id": 5,
        "nombre": "Habitación Familiar", 
         "capacidad": 4, 
         "Num_camas": "1 cama doble - 2 camas simples", 
         "vista": "Frente o Playa",
         "AC": "Si",
         "TV": "Si",
         "precio_alta": 50_000, 
         "precio_media": 60_000, 
         "precio_alta": 70_000, 
         "imgs": ["familiar1.webp", "familiar2.webp", "familiar3.webp", "familiar4.webp"],
         "range": range(0,4),
         },

         {"id": 6,
        "nombre": "Suite", 
         "capacidad": 3, 
         "Num_camas": "1 cama doble - 1 sillón cama", 
         "vista": "Frente o Playa",
         "AC": "Si",
         "TV": "Si",
         "precio_alta": 60_000, 
         "precio_media": 70_000, 
         "precio_alta": 80_000, 
         "imgs": ["suite1.webp", "suite2.webp", "suite3.webp", "suite4.webp"],
         "range": range(0,4),
         },
         
         ]

    context = {
        "date": datetime.now(),
        "active": "rooms",
        "rooms_list": rooms,
    }
    return render(request, 'reservas/habitaciones.html', context)

def facilities(request):
    context = {
        "hero":{"title":"DSH","content":"Queremos que tu estancia en nuestro exuberante hotel sea realmente inolvidable. Por eso prestamos especial atención a todas tus necesidades para que podamos asegurarte una experiencia única. habitaciones exquisitamente diseñadas, piscina y jacuzzi, un restaurante que celebra sabores auténticos, y servicios personalizados, en Django Hotel Suites creamos experiencias inolvidables. Únete a nosotros y sumérgete en un mundo donde la elegancia y la comodidad danzan en armonía."},
        "date": datetime.now(),
        "active": "facilities",
        "imagenes": [
            {"img":"img/facilities/instalacion_general.jpg"},
            {"img":"img/facilities/instalaciones_01.webp"},
            {"img":"img/facilities/instalaciones_02.webp"},
            {"img":"img/facilities/instalaciones_03.webp"},
            {"img":"img/facilities/instalaciones_04.webp"},
            {"img":"img/facilities/instalaciones_05.webp"},
            {"img":"img/facilities/instalaciones_06.webp"},
            ],
        "cards":[
            {"title":"Sevicios nauticos","img":"img/facilities/instalaciones_01.webp","comentario":"¡Explora las maravillas del mar con nuestra gama de servicios náuticos! Desde emocionantes paseos en motos acuáticas hasta relajantes viajes en lancha y barco, tenemos todo lo que necesitas para una experiencia inolvidable en el agua. ¡Prepárate para navegar hacia la diversión y la aventura!"},
            {"title":"Explora ESPA","img":"img/facilities/instalaciones_04.webp","comentario":"Descubre la tranquilidad y el encanto de nuestro oasis ESPA. Un lugar donde el bienestar y la relajación te esperan en cada rincón. ¡Sumérgete en una experiencia rejuvenecedora que te dejará renovado y revitalizado!"},
            {"title":"Habitaciones de Lujo","img":"img/facilities/instalaciones_05.webp","comentario":"Sumérgete en la opulencia y el confort con nuestras Habitaciones de Lujo. Cada detalle ha sido diseñado con elegancia para brindarte una experiencia de alojamiento excepcional. Disfruta de una estancia inolvidable en un entorno de lujo y comodidad incomparables."},
            {"title":"Ambientes Climatizados","img":"img/facilities/instalaciones_05.webp","comentario":"Relájate y sumérgete en la comodidad de nuestros Ambientes Climatizados, donde disfrutarás de la frescura y la relajación constante de una piscina cerrada. Un refugio perfecto para escapar del calor y disfrutar de un ambiente agradable en cualquier época del año. ¡Tu oasis personal de serenidad!"},
            {"title":"Ambientes Climatizados","img":"img/facilities/instalaciones_05.webp","comentario":"Relájate y sumérgete en la comodidad de nuestros Ambientes Climatizados, donde disfrutarás de la frescura y la relajación constante de una piscina cerrada. Un refugio perfecto para escapar del calor y disfrutar de un ambiente agradable en cualquier época del año. ¡Tu oasis personal de serenidad!"},
            {"title":"Habitaciones de Lujo","img":"img/facilities/instalaciones_05.webp","comentario":"Sumérgete en la opulencia y el confort con nuestras Habitaciones de Lujo. Cada detalle ha sido diseñado con elegancia para brindarte una experiencia de alojamiento excepcional. Disfruta de una estancia inolvidable en un entorno de lujo y comodidad incomparables."},
        ]
    }
    return render(request, "./facilities/facilities.html", context)

def contact(request):
    context = {
        "date": datetime.now(),
        "active": "contact",
        }
    return render(request, "reservas/contacto.html", context)
