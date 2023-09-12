
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
})