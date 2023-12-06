$(document).ready(function() {
  // Make an AJAX request to fetch the character name
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
    // Update the text content of DIV#character with the character name
    $('#character').text(data.name);
  });
});
