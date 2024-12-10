// Get the form element
var form = document.getElementById('my-form');

// Add a submit event listener to the form
form.addEventListener('submit', function(event) {    
    let preloader = document.getElementById("cs-loader");
    preloader.style.display= 'flex';
});
