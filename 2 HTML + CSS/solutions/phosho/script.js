// script.js

document.addEventListener('DOMContentLoaded', function() {
// navbar collapse logic
  var sidenavElem = document.querySelectorAll('.sidenav');
  var sidenav = M.Sidenav.init(sidenavElem, {});

// parallax logic
  var parallaxElems = document.querySelectorAll('.parallax');
  var parallax = M.Parallax.init(parallaxElems, {});
});