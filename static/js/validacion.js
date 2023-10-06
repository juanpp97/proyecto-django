const dateIn = document.querySelector('#id_date_in');
const dateOut = document.getElementById('id_date_out');

console.log(dateOut)
let dateInMax = dateIn.max;
let dateInMin = dateIn.min;

function update_date_out(){
    if(dateIn.value > dateInMin && dateIn.value < dateInMax){
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
}
if(dateIn.value){
    update_date_out()
}
if(!dateOut.value){
    dateOut.setAttribute('disabled', 'true')
}

/* Cambio las fechas mínimas y máximas según selección*/
dateIn.addEventListener('change', (e) => {
    dateOut.value = ""
    update_date_out()
  
});
