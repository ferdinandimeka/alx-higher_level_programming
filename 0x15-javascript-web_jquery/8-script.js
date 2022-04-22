//a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
$.get('https://swapi.co/api/films/?format=json', function (data) {
  $.each(data.results, function (index, value) {
    $('<li>' + value.title + '</li>').appendTo('UL#list_movies');
  });
});