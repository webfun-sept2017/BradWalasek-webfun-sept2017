$(document).ready(function(){

var arr = $('img');

for (var i = 0; i < arr.length; i++) {
  arr[i].name = 'CAT';
}

$('img').click(function(){
var i = 0;
  if ((this).name == 'CAT') {
    // alert('It Worked');
    $(this).name = 'NINJA';
    $(this).html('<img src="' + 'img\ninja' + i + '.png>');
    console.log($(this));
  }
  else{
  if ((this).name == 'NINJA') {
    // alert('It Worked');
    $(this).name = 'CAT';
    $(this).html('<img src="' + 'img\cat' + i + '.png>');
    console.log($(this));
  }
}
});







});
