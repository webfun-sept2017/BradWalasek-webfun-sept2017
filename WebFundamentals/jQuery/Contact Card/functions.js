$(document).ready(function(){
  var i = 0;
  $('button').click(function(){

    $('.space').append('<div data-desc='+ $('#desc').val() +' class="card"><h1>' + $('#firstname').val() +" "+ $('#lastname').val() + '</h1>Click here for a description</div>')
    console.log($('.card').attr('data-desc'));
    // console.log($('.space').html());

    $('.card').click(function(){
    var ori=$(this).html();
    console.log(ori);
    $(this).html($(this).attr('data-desc'));
    $(this).attr('data-desc', ori)
    });
  });
})
