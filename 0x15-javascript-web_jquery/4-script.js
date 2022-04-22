//a JavaScript script that toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header
$('DIV#toggle_header').click(function()
{
  if ($('HEADER').hasClass('red')) {
    $('HEADER').removeClass('red');
    $('HEADER').addClass('green');
  } else if ($('HEADER').hasClass('green')) {
    $('HEADER').removeClass('green');
    $('HEADER').addClass('red');
  }
});