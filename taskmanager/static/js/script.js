// In order for the sidenav to work, we need to initialize the JavaScript functionality from Materialize
document.addEventListener('DOMContentLoaded', function() {
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
  });