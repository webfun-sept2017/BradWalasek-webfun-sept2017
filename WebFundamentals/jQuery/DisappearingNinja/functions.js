$(document).ready(function(){
  console.log($('img'));

// Clicking Images and hiding them
  $('img').click(function(){
    $(this).hide();
  });

  $('button').click(function(){
    $('img').show();
  });



});
