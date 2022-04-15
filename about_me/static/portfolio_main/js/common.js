$(function() {

	var
	images = document.images,
	images_total_count = images.length,
	images_loaded_count = 0,
	preloader = document.getElementById('page-preloader'),
	prec_display = document.getElementById('load_prec');

	for( var i = 0; i < images_total_count; i++){
		image_clone = new Image();
		image_clone.onload = image_loaded;
		image_clone.onerror = image_loaded;
		image_clone.src = images[i].src;
	}
	function image_loaded() {
		images_loaded_count++;
		prec_display.innerHTML = (((100 / images_total_count) * images_loaded_count) << 0) + '%';

		if( images_loaded_count >= images_total_count)
		{
			setTimeout(function(){
				if( !preloader.classList.contains('done'))
				{
					preloader.classList.add('done');
				}
			}), 1000;
		}
	}

});

$(document).ready(function(){
	var head = $('header');

	scrollLink('.menu a');
	scrollLink('.banner-a');

	$('.mob-menu').click(function(){
		head.toggleClass('open');
	});
	
	function scrollLink(link){
		$(link).click(function(e){
			e.preventDefault();
			var id  = $(this).attr('href'),
				top = $(id).offset().top;
			$('html,body').animate({scrollTop: top - head.height()},900);
			head.removeClass('open');
		});
	}

	if ($(window).width() > 768) {
	   (function($) {
	        $.fn.animated = function(inEffect, outEffect) {
	                $(this).css("opacity", "0").addClass("animated").waypoint(function(dir) {
	                        if (dir === "down") {
	                                $(this).removeClass(outEffect).addClass(inEffect).css("opacity", "1");
	                        } else {
	                                $(this).removeClass(inEffect).addClass(outEffect).css("opacity", "1");
	                        };
	                }, {
	                        offset: "90%"
	                }).waypoint(function(dir) {
	                        if (dir === "down") {
	                                $(this).removeClass(inEffect).addClass(outEffect).css("opacity", "1");
	                        } else {
	                                $(this).removeClass(outEffect).addClass(inEffect).css("opacity", "1");
	                        };
	                }, {
	                        offset: -$(window).height()
	                });
	        };
	    })(jQuery);

		$(".banner-text p,.banner-text a").animated("fadeInUp", "fadeOutUp");
	    $(".section-text h2").animated("flipInY", "fadeOutDown");

	    $(".about-photo").animated("fadeInLeft", "fadeOutLeft");
	    $(".about-text").animated("fadeInRight", "fadeOutRight");

	    $(".services-column").animated("fadeInDown", "fadeOutDown");

	    $(".portfolio-post").animated("zoomIn", "zoomOut");

	    $(".steps-1,.steps-3").animated("rotateInDownLeft", "rotateOutDownLeft");
	    $(".steps-2,.steps-4").animated("rotateInDownRight", "rotateOutDownRight");

	    $(".skills-column").animated("fadeInDown", "fadeOutDown");
	}
});