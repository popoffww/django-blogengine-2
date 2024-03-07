document.addEventListener('DOMContentLoaded', function() {
     let elems = document.querySelectorAll('.sidenav')
     M.AutoInit();
 })

//document.addEventListener('DOMContentLoaded', function() {
//     let elems = document.querySelectorAll('.dropdown-trigger')
//     M.AutoInit();
// })

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.dropdown-trigger');
    var instances = M.Dropdown.init(elems, {
        coverTrigger: false,
        closeOnClick: true,
        hover: false,
        inDuration: 200,
        outDuration: 1000,
    });
  });
