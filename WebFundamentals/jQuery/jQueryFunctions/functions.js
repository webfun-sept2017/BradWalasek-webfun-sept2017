
var arr = document.getElementsByClassName('centerwindow');
console.log(arr);
$(document).ready(function(){

  console.log($("#button1"));
  $("#button1").click(function(){
    $(this).hide();
    $("#win1").html("<p>The button to the left has been clicked!</p>")
  });
});
