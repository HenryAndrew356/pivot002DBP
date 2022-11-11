
function getData(){
    console.log("Ingreso al COnaol.el")
    const name=document.getElementById('firstNameF').value;
    const lastName=document.getElementById('lastNameF').value;
    const username=document.getElementById('usernameF').value;
    const email=document.getElementById('emailF').value;
    const ocupation=document.getElementById('ocupationF').value;
    const telefono=document.getElementById('telefonoF').value;
    // Get Data form Select [Options]
    var country=document.getElementById('countryA');
    var index=country.value;
    var textCountry=country.options[country.selectedIndex].text;
    console.log(index);
    console.log(textCountry);
    console.log("Lol")
}