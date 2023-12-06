$(document).ready(function() {
  // Make an AJAX request to fetch the translation
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
    // Update the text content of DIV#hello with the translation
    $('#hello').text(data.hello);
  });
});
