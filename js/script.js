$(document).ready(function() {
    $('.slider').slick({
        arrows: true,
        dots: true,
        adaptiveHeight: true,
        // slidesToShow:3, == показывает три слайда 19#22
        // slidesToScroll:3
        speed: 500,
        // скорость(300 дефолт)
        // infinite:false, == вырубить бесконечность 22#50
        autoplay: true,
        autoplaySpeed: 4000,
        // autoplaySpeed:3000 == Дефолт == 3сек
        // centerMode:true, ==слай по центру(удобно приятно например при 3х сладах 3121)
        // variableWidth:true, == огр по ширине 3358
        // rows:2 == два этажа нужно будет в этом случае сделать 2 скролла
        // slidesperRow:2 == количество слайдов в ряду 3628
        // вертикал 37 
        // дабл 39 +связка
        responsive: [{
                breakpoint: 768,
                settings: {}
            }]
            // брэйкпоинт 4429

        // перненос кнопок в  другой класс 4837
        // 57 создание сладера текста меню и тп и пр фичи

    });
});