var mainNav = document.getElementById('js-nav-menu');
var navBarToggle = document.getElementById('navbar-toggle');
var cus_btn = document.getElementById("customers");
var trans_btn = document.getElementById("transactions");
var trans_amt = document.getElementById("transfer");

navBarToggle.addEventListener('click', function () {
    mainNav.classList.toggle('active');
});

function  show_cus() {
    trans_btn.style.display = "none";
    cus_btn.style.display = "block";
    trans_amt.style.display = "none";
}

function show_trans() {
    cus_btn.style.display = "none";
    trans_btn.style.display="block";
    trans_amt.style.display = "none";
}

function trans() {
    cus_btn.style.display = "none";
    trans_btn.style.display = "none";
    trans_amt.style.display = "block";
}