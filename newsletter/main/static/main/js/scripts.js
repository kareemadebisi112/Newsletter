//var form = document.getElementById('form')
// var button = document.getElementById('submitButton')
// var shipping = '{{shipping}}'
// var total = '{{order.get_cart_total|floatformat:2}}'
// button.addEventListener("click", submit);
var email = document.getElementById('email')
var form = document.getElementById('form')

document.querySelector('form.contactForm').addEventListener('submit', function (e) {
    //prevent the normal submission of the form
    e.preventDefault();
    console.log("Email:",email.value);
    submitFormData()    
});

function submitFormData(){
    var visitor = {
        'email': null,
    }
    visitor.email = email.value;

    var url ='sendToDatabase/'
    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'visitor':visitor}),
    })
    .then((response) => response.json())
    .then((data) =>{
        console.log('Success:', data);
        alert('Transaction completed');
    })
}