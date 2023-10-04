document.addEventListener('DOMContentLoaded', function () {
    var navbar = document.querySelector('.navbar');
  
    window.addEventListener('scroll', function () {
      if (window.scrollY > 10) {
        navbar.style.backgroundColor = 'white';
      } else {
        navbar.style.backgroundColor = 'transparent';
      }
    });
  });
  