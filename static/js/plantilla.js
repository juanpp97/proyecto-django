let botton = document.querySelector('#panel-users-switch')
let panel = document.querySelector('.panel-users-list')
botton.addEventListener('click',()=>{
    if(panel.classList.contains('panel-close')){
        botton.classList.add('rotate-button')
    } else {
        botton.classList.remove('rotate-button')
    }
    panel.classList.toggle('panel-close')

})
