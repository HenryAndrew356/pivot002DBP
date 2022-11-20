
function getData(){
    const name=document.getElementById('firstNameF').value;
    const lastName=document.getElementById('lastNameF').value;
    const username=document.getElementById('usernameF').value;
    const email=document.getElementById('emailF').value;
    const ocupation=document.getElementById('ocupationF').value;
    const telefono=document.getElementById('telefonoF').value;
    
    // Get Data form Country
    // var country=document.getElementById('countryA');
    // var index=country.value;
    // var textCountry=country.options[country.selectedIndex].text;
    // console.log(country);
    // console.log(index);
    // console.log(textCountry);
    // console.log(textCountry);
}
// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
    'use strict'
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')
    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }
        form.classList.add('was-validated')
        
      }, false)
    })
  })()


    // Problemas para reconocer "$" <-- "Its nod defined"


var your_data = {
  name:"AndrewFieldName"
}
fetch(`${window.origin}/cvOfForm`, {
  method: "POST",
  credentials: "include",
  body: JSON.stringify(your_data),
  cache: "no-cache",
  headers: new Headers({
    "content-type": "application/json"
  })
})