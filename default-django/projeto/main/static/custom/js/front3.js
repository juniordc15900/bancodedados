$(document).ready(function () {
	$('#accepted-cookie').on('click', function (e) {
		document.getElementById('cookie').style.display ="none";
		document.cookie = "NOME_COOKIE=accepted;expires=Thu, 18 Dec 2022 12:00:00 UTC;max_age = 365*24*60*60";
	});
});






