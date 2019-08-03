// script.js

// navbar collapse logic
  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {});
 
    var elems = document.querySelectorAll('.parallax');
    var instances = M.Parallax.init(elems, {});
  });


  
   // $(document).ready(function(){
   // $('.parallax').parallax();
   //  }); 