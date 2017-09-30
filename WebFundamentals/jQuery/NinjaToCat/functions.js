$(document).ready(function(){
//  $('img') grabs an object, not an array, look into this further
// .attr
// var obj = $('img');
// console.log(obj);
// for (var i = 0; i < arr.length; i++) {
//   obj[i].name = 'CAT';
// }





$('img').click(function(){
  var source = $(this).attr('src');
  $(this).attr('src', $(this).attr('data-alt'));
  $(this).attr('data-alt', source);

});






//garbage code
// $('img').click(function(){
// var i = 0;
//   if ((this).name == 'CAT') {
//     $(this).name = 'NINJA';
//     $(this).html('<img src="' + 'img\ninja' + i + '.png>');
//     console.log($(this.name));
//     console.log('it worked!');
//   }
//   else{
//   if ((this).name == 'NINJA') {
//     alert('It Worked');
//     $(this).name = 'CAT';
//     $(this).html('<img src="' + 'img\cat' + i + '.png>');
//     console.log($(this));
//   }
// }
// });







});
