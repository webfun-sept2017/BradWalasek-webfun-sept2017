$(document).ready(function(){

  $('img').hover(function(){
    var a = $(this).attr('data-alt');
    var b = $(this).attr('src')
    $(this).attr('src', a);
    $(this).attr('data-alt', b);
    console.log($(this).attr('data-alt'));
    console.log($(this).attr('src'));
  }, function(){
    var a = $(this).attr('data-alt');
    var b = $(this).attr('src')
    $(this).attr('src', a);
    $(this).attr('data-alt', b);
  });

})
