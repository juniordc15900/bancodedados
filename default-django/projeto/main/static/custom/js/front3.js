$(document).ready(function () {
	$('.header__mobile-bars').on('click', function (e) {
		$('.header__mobile-bars a span').toggleClass('active');
		$('header').toggleClass('active');
	});
	$('#close-cookie').on('click', function (e) {
		document.getElementById('cookie').style.display ="none";
	});
	$('#accepted-cookie').on('click', function (e) {
		document.getElementById('cookie').style.display ="none";
		document.cookie = "NOME_COOKIE=accepted;expires=Thu, 18 Dec 2022 12:00:00 UTC;max_age = 365*24*60*60";
	});
	
});

$(function () {
	$('.loader-a').click(function(evt){
		evt.preventDefault();
		document.getElementById('main-id').style.display ="none";
		document.getElementById('mob').style.display ="none";
		if($(window).width() < 768){
			document.getElementById('loading-mob').style.display ="flex";
		}else{
			document.getElementById('loading').style.display ="flex";
		}
		var link=$(this).attr('href');
		setTimeout(function(){
			window.location.href=link;
		},750);
	});
});







