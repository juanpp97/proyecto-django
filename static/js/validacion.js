const dateIn = document.querySelector('#date_in');
const dateOut = document.querySelector('#date_out');
const contador = document.querySelector(".word-counter")
const comentario = document.querySelector("#comment")
const maxLength = 1000;
comentario.maxLength = maxLength;
contador.innerHTML = maxLength
let dateInMax = dateIn.max;
let dateInMin = dateIn.min;


/* Cambio las fechas mínimas y máximas según selección*/
dateIn.addEventListener('change', (e) => {
  console.log(dateIn.value);
  console.log(dateInMax);
  if(dateIn.value > dateInMin && dateIn.value < dateInMax){
    dateOut.value = ""
    let minDateOut = new Date(dateIn.value);
    let maxDateOut = new Date(dateIn.value);
    minDateOut.setDate(minDateOut.getDate() + 1);
    maxDateOut.setMonth(maxDateOut.getMonth() + 2); //Le sumo dos meses como máximo de estadía
    minDateOut = minDateOut.toISOString().split('T')[0];
    maxDateOut = maxDateOut.toISOString().split('T')[0];
    dateOut.min = minDateOut;
    dateOut.max = maxDateOut;
    dateOut.removeAttribute('disabled')
  }else{
    dateOut.setAttribute('disabled', 'true')
    dateOut.value = ""
  }
});
comentario.addEventListener("input", () => {
  /* Si se excede del número máximo de caracteres lo indica en pantalla */
  contador.innerHTML = maxLength - comentario.value.length;
});