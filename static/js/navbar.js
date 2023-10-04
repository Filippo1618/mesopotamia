document.addEventListener('DOMContentLoaded', function () {
  var navbar = document.querySelector('.navbar');
  var sections = document.querySelectorAll('section'); // Seleziona tutte le sezioni
  var threshold = 70; // Soglia in pixel

  
  window.addEventListener('scroll', function () {
      var currentSection = null; // Inizializza la sezione corrente come nulla
      
      // Determina la sezione attualmente visibile
      sections.forEach(function (section) {
          var sectionTop = section.getBoundingClientRect().top - threshold;
          var sectionBottom = section.getBoundingClientRect().bottom;
          
          if (sectionTop <= 0 && sectionBottom > 0) {
              console.log('prova');
              currentSection = section; // Imposta la sezione corrente
          }
      });
      
      // Rimuovi la classe "active-link" da tutti i link nella navbar
      var links = navbar.querySelectorAll('a');
      links.forEach(function (link) {
          link.classList.remove('active-link');
      });
      
      // Se c'è una sezione attualmente visibile, applica la classe "active-link" al link corrispondente
      if (currentSection) {
          var sectionId = currentSection.getAttribute('id');
          var activeLink = navbar.querySelector('a[data-section="' + sectionId + '"]');
          if (activeLink) {
              activeLink.classList.add('active-link');
          }
      }
      
      // Cambia lo stile della navbar in base allo scrolling, come hai già fatto
      if (window.scrollY > 5) {
          navbar.style.backgroundColor = 'grey';
      } else {
          navbar.style.backgroundColor = 'transparent';
      }
  });
});
