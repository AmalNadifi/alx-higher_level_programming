// Use jQuery to toggle the class of the <header> element when the user clicks on DIV#toggle_header
$(document).ready(function() {
  $('#toggle_header').click(function() {
    $('header').toggleClass('red green');
  });
});
