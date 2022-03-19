$(document).ready(function() {
    $('.slider').slick({
        arrows: true,
        dots: true,
        adaptiveHeight: true,
        speed: 500,
        autoplay: true,
        autoplaySpeed: 4000,
        responsive: [{
                breakpoint: 768,
                settings: {}
            }]

    });
});