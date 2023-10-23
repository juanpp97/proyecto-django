function cargar_producto(elemento){
    let lista = JSON.parse(localStorage.getItem('lista_productos'))
    localStorage.setItem('lista_productos',JSON.stringify(lista))
    if(JSON.parse(localStorage.getItem('lista_productos')) == false) localStorage.setItem('lista_productos',JSON.stringify([]))
    lista.push(elemento)
    localStorage.setItem('lista_productos',JSON.stringify(lista))
  }



  let listener_buttons = document.querySelectorAll('.datita')

  listener_buttons.forEach((e)=>{
    e.addEventListener('click',function(event){
      alertify.success('Agregado');
      cargar_producto(this.dataset)
    })
  })
