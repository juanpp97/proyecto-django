from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from .forms import ReservationForm, ContactForm
from django.contrib import messages
from administracion.models import RoomType, Price
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from django.views.generic import View
from django.urls import reverse_lazy
from .forms import  InicioSesionForm, RegistroForm
from django.db.models import Subquery, OuterRef
from django.db.models.functions import Coalesce

def index(request):
    context = {
        "date": datetime.now(),
        "active": "index",
    }
    return render(request, "reservas/inicio.html", context)

def rooms(request):
    
    if request.method == "GET":
        today = datetime.now()
        #Se agrega a cada objeto RoomType el precio que le corresponde
        #Para ello se hace un Subquery que utiliza la clave primaria del queryset externo como room_type. Luego solo se trae el precio y nos quedamos con el primer valor
        room_types = RoomType.objects.annotate(
            price=Coalesce(
                Subquery(
                    Price.objects.filter(
                        room_type=OuterRef('pk'),
                        date_from__lte=today.strftime("%Y-%m-%d"),
                        date_to__gte=today.strftime("%Y-%m-%d")
                    ).values('price')[:1]
                ),
                Subquery(Price.objects.filter(room_type=OuterRef('pk')).values('price')[:1])
            )
        ).order_by('price')
      
    context = {
            "date": today.date,
            "active": "rooms",
            "rooms_list": room_types,
        }
    return render(request, 'reservas/habitaciones.html', context)

def facilities(request):
    context = {
        "hero":{"title":"DSH","content":"Queremos que tu estancia en nuestro  hotel sea realmente inolvidable. Por eso prestamos especial atención a todas tus necesidades para que podamos asegurarte una experiencia única. habitaciones exquisitamente diseñadas, piscina y jacuzzi, un restaurante que celebra sabores auténticos, y servicios personalizados, en Django Hotel Suites creamos experiencias inolvidables. Únete a nosotros y sumérgete en un mundo donde la elegancia y la comodidad danzan en armonía."},
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
            {"title":"Habitaciones","img":"img/facilities/instalaciones_05.webp","comentario":"Sumérgete en la opulencia y el confort con nuestras Habitaciones de Lujo. Cada detalle ha sido diseñado con elegancia para brindarte una experiencia de alojamiento excepcional. Disfruta de una estancia inolvidable en un entorno de lujo y comodidad incomparables."},
            {"title":"Restaurant y Bar exclusivos","img":"img/facilities/instalaciones_RESTAURANTE&BAR.webp","comentario":"Explora una deliciosa variedad de sabores en nuestros exclusivos restaurantes y bares. Desde la cocina gourmet hasta cócteles artesanales, te invitamos a saborear una experiencia culinaria excepcional en un entorno encantador. Descubre un festín para tus sentidos en nuestro hotel."},
            {"title":"PASEOS POR MAR","img":"img/facilities/instalaciones_YATES.webp","comentario":"¡Explora las maravillas del mar con nuestra gama de servicios náuticos! Desde emocionantes paseos en motos acuáticas hasta relajantes viajes en lancha y barco, tenemos todo lo que necesitas para una experiencia inolvidable en el agua. ¡Prepárate para navegar hacia la diversión y la aventura!"},
            {"title":"SPA","img":"img/facilities/instalaciones_ESPA.webp","comentario":"Descubre la tranquilidad y el encanto de nuestro oasis ESPA. Un lugar donde el bienestar y la relajación te esperan en cada rincón. ¡Sumérgete en una experiencia rejuvenecedora que te dejará renovado y revitalizado!"},
            {"title":"Ambientes Climatizados","img":"img/facilities/instalaciones_05.webp","comentario":"Relájate y sumérgete en la comodidad de nuestros ambientes climatizados, donde disfrutarás de la frescura y la relajación constante de una piscina cerrada. Un refugio perfecto para escapar del calor y disfrutar de un ambiente agradable en cualquier época del año. ¡Tu oasis personal de serenidad!"},
            {"title":"GYM","img":"img/facilities/instalaciones_GYM.webp","comentario":"Encuentra el equilibrio perfecto entre relajación y actividad en nuestro moderno gimnasio. Mantén tu rutina de ejercicios, disfruta de equipos de primera calidad y mantente en forma durante tu estancia. En nuestro hotel, el bienestar es una prioridad, incluso cuando estás de viaje."},
            {"title":"Playa privada","img":"img/facilities/instalaciones_PLAYAPRIVADA.webp","comentario":"Disfruta de la serenidad y la exclusividad en nuestro paraíso junto al mar. Nuestra playa privada te ofrece un rincón de tranquilidad y belleza donde puedes relajarte, tomar el sol y sumergirte en las aguas cristalinas. ¡Tu escape perfecto a la orilla del mar te espera!"},
        ]
    }
    return render(request, "reservas/facilities.html", context)

def contact(request):
    if request.method == "GET":
        form = ContactForm()
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            #Enviar mail, si se envia correctamente dar el mensaje de success
            form = ContactForm()
            messages.success(request, "Tu consulta se ha enviado correctamente. En breve un asesor se contactará contigo")
        else:
            messages.error(request, "Revisa los errores del formulario")
    context = {
        "date": datetime.now(),
        "active": "contact",
        'form': form,
        }
    return render(request, "reservas/contacto.html", context)


def reservation(request, id_hab):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para acceder")
        return redirect('accounts_handler')
    rooms = [
        {
        "id": 1,
        "name": "Habitación Individual", 
         "capacity": 1, 
         "num_beds": "1 cama simple", 
         "view": "Frente", 
         "AC": "Si",
         "TV": "Si",
         "price_low": 30_000, 
         "price_med": 40_000, 
         "price_high": 50_000, 
         "imgs": ["individual1.webp", "individual2.webp", "individual3.webp", "individual4.webp"],
         "range": range(0,4),
         },

         {"id": 2,
          "name": "Habitación Doble Clásica", 
         "capacity": 2, 
         "num_beds": "2 camas simples", 
         "view": "Playa",
         "AC": "Si",
         "TV": "Si",
         "price_low": 40_000, 
         "price_med": 50_000, 
         "price_high": 60_000, 
         "imgs": ["doble1.webp", "doble2.webp", "doble3.webp"],
         "range": range(0,3),
         },

         {"id": 3,
        "name": "Habitación Matrimonial", 
         "capacity": 2, 
         "num_beds": "1 cama doble", 
         "view": "Ambas", 
         "AC": "Si",
         "TV": "Si",
         "price_low": 30_000, 
         "price_med": 40_000, 
         "price_high": 50_000, 
         "imgs": ["matrimonial1.webp", "matrimonial2.webp", "matrimonial3.webp"],
         "range": range(0,3),
         },

         {"id": 4,
        "name": "Habitación Triple",
         "capacity": 3, 
         "num_beds": "3 camas simples", 
         "view": "Ambas",
         "AC": "Si",
         "TV": "Si",
         "price_low": 40_000, 
         "price_med": 50_000, 
         "price_high": 60_000, 
         "imgs": ["triple1.webp", "triple2.webp", "triple3.webp"],
         "range": range(0,3),
         },

         {"id": 5,
        "name": "Habitación Familiar", 
         "capacity": 4, 
         "num_beds": "1 cama doble - 2 camas simples", 
         "view": "Ambas",
         "AC": "Si",
         "TV": "Si",
         "price_low": 50_000, 
         "price_med": 60_000, 
         "price_high": 70_000, 
         "imgs": ["familiar1.webp", "familiar2.webp", "familiar3.webp", "familiar4.webp"],
         "range": range(0,4),
         },

         {"id": 6,
        "name": "Suite", 
         "capacity": 3, 
         "num_beds": "1 cama doble - 1 sillón cama", 
         "view": "Ambas",
         "AC": "Si",
         "TV": "Si",
         "price_low": 60_000, 
         "price_med": 70_000, 
         "price_high": 80_000, 
         "imgs": ["suite1.webp", "suite2.webp", "suite3.webp", "suite4.webp"],
         "range": range(0,4),
         },
         
         ]
    room = list(filter(lambda room: room["id"] == id_hab, rooms))[0]
    min_date_check_in = datetime.now() + timedelta(days=1)
    max_date_check_in = datetime.now() + relativedelta(years=1)
    available = None

    if request.method == "GET":

        if room["view"].lower() == "ambas":
            form = ReservationForm(id_hab = id_hab, capacity = room["capacity"], min_date_in = min_date_check_in.date(), max_date_in = max_date_check_in.date())
        else:
            form = ReservationForm(id_hab = id_hab, capacity = room["capacity"], room_view = room["view"], min_date_in = min_date_check_in.date(), max_date_in = max_date_check_in.date())
        

    elif request.method == "POST":

        if room["view"].lower() == "ambas":
            form = ReservationForm(request.POST, id_hab = id_hab, capacity = room["capacity"], min_date_in = min_date_check_in.date(), max_date_in = max_date_check_in.date())
        else:
            form = ReservationForm(request.POST, id_hab = id_hab, capacity = room["capacity"], room_view = room["view"], min_date_in = min_date_check_in.date(), max_date_in = max_date_check_in.date())
        
        if form.is_valid():    
            available = False
            messages.success(request, "Datos validados correctamente")
        else:
            messages.error(request, "Verifica los errores en el formulario")

    context = {
        "date": datetime.now(),
        "form": form,
        "available": available,
        "room": room,
        "active": "reservation",
    }
    
    return render(request, "reservas/reserva.html", context)



class Login_RegistrationView(View):
    template_name = 'reservas/combined_registration_login.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('index'))
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        panel = False
        if request.GET.get('panel') == 'True':
            panel = True
        login_form = InicioSesionForm()
        registration_form = RegistroForm()
        return render(request, self.template_name, {'registration_form': registration_form, 'login_form': login_form, "LoginOrRegister": panel })

    def post(self, request):
        panel=False
        if 'login_form' in request.POST:
            login_form = InicioSesionForm(request, data = request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None: 
                    login(request,user)
                    if 'next' in request.POST:
                        return redirect(request.POST['next'])
                    return redirect('index')
                else:
                    messages.error(request, "Error al iniciar sesión")
            else:
                messages.error(request, "Error al iniciar sesión")
        else:
            login_form = InicioSesionForm()
        if 'registration_form' in request.POST:
            registration_form = RegistroForm(request.POST)
            if registration_form.is_valid():
                registration_form.save()
                panel = False
                messages.success(request, "Usuario creado correctamente")
                return redirect('accounts_handler')
            else:
                panel = True
                messages.error(request, "Se ha producido un error al crear el usuario")
        else:
            registration_form = RegistroForm()
        
        return render(request, self.template_name, {'registration_form': registration_form, 'login_form': login_form,"LoginOrRegister": panel })


