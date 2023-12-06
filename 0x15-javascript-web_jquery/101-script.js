$(document).ready(function() {
  // Click event for adding a new item to the list
  $('#add_item').click(function() {
    $('<li>Item</li>').appendTo('ul.my_list');
  });

  // Click event for removing the last item from the list
  $('#remove_item').click(function() {
    $('ul.my_list li:last-child').remove();
  });

  // Click event for clearing all items from the list
  $('#clear_list').click(function() {
    $('ul.my_list').empty();
  });
});
