
window.addEventListener('load',()=>{
    var swiper = new Swiper('.swiper-container', {
        pagination: {
            el: '.swiper-pagination', // Indicador de paginación
        },
        loop: true,
        speed: 1000,
        autoplay: {
            delay: 3000,
            disableOnInteraction: false,
        },
        effect: 'fade',
        crossFade: false,
    });

    const elementosObservables = document.querySelectorAll('.facilities_card');

    const opcionesDeObservacion = {
        root: null, 
        rootMargin: '0px',
        threshold: 0.2, 
    };
    
    const observer = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                console.log("PASO")
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target); // Dejar de observar el elemento una vez que se hace visible
            }
        });
    }, opcionesDeObservacion);
    
    elementosObservables.forEach(elemento => {
        observer.observe(elemento);
    });



})