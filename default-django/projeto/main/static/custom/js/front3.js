$(document).ready(function () {
	$('#accepted-cookie').on('click', function (e) {
		document.getElementById('cookie').style.display ="none";
		document.cookie = "NOME_COOKIE=accepted;expires=Thu, 18 Dec 2022 12:00:00 UTC;max_age = 365*24*60*60";
	});
});

var swiper = new Swiper('.swiper-container.banner', {
	cssMode: true,
	navigation: {
	  nextEl: '.swiper-button-next.banner',
	  prevEl: '.swiper-button-prev.banner',
	},
	pagination: {
	  el: '.swiper-pagination.banner'
	},
	mousewheel: true,
	keyboard: true,
  });

var swiper = new Swiper('.swiper-container.product', {
	slidesPerView: 4,
	spaceBetween: 20,
	loop: true,
	centeredSlides: true,
	navigation: {
		nextEl: '.swiper-button-next.product',
		prevEl: '.swiper-button-prev.product',
	},
	pagination: {
		el: '.swiper-pagination.product',
		clickable: true,
	},
});






