$(document).ready(function() {
	$('#btn_translate').click(function() {
	  // Get the language code entered by the user
	  const languageCode = $('#language_code').val();
  
	  // Make an AJAX request to the API
	  $.ajax({
		url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`,
		success: function(data) {
		  // Display the translation in the DIV#hello element
		  $('#hello').text(data.hello);
		},
		error: function() {
		  // Display an error message if the request fails
		  $('#hello').text('Error fetching translation');
		}
	  });
	});
  });
