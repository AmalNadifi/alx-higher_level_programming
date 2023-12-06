// Use jQuery to add the class 'red' to the <header> element when the user clicks on DIV#red_header
$(document).ready(function() {
  $('#red_header').click(function() {
    $('header').addClass('red');
  });
});
