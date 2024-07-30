$(document).ready(function () {
	$.getJSON(
		"https://swapi-api.hbtn.io/api/films/?format=json",
		function (data) {
			data.results.forEach(function (film) {
				$("<li>").text(film.title).appendTo("ul#list_movies");
			});
		}
	);
});
