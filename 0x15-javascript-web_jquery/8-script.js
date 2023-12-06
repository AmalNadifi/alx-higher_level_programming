$(document).ready(function() {
  // Make an AJAX request to fetch the movie titles
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    // Iterate through each movie and append its title to UL#list_movies
    $.each(data.results, function(index, movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
