document.addEventListener('DOMContentLoaded', function() {
  $('#btn_translate, #language_code').on('click keypress', function(event) {
    if (event.type === 'click' || (event.type === 'keypress' && event.key === 'Enter')) {
      const languageCode = $('#language_code').val();

      // Make a request to fetch the translation
      $.ajax({
        url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`,
        dataType: 'json',
        success: function(data) {
          $('#hello').text(data.hello);
        },
        error: function() {
          $('#hello').text('Error fetching translation');
        }
      });
    }
  });
});
