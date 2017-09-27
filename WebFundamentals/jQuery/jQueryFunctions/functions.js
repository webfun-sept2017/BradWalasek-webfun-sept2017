
var arr = document.getElementsByClassName('centerwindow');
console.log(arr);
$(document).ready(function(){

  console.log($("#button1"));
  $("#button1").click(function(){
    $(this).hide();
    $("#win1").html("<p>The button to the left has been clicked!</p>")
  });
  $("#button2").click(function(){
    $(this).hide();
    $('#win2').hide();
  });

  $('#win3').hide();

  $("#button3").click(function(){
    $('#win3').show();
  });
  $("#button4").click(function(){
    $('#togglesegment').toggle();
  });
  $('#win5').hide();
  $("#button5").click(function(){
    $('#win5').slideDown(2000);
  });
  $("#button6").click(function(){
    $('#win6').slideUp();
  });
  $("#button7").click(function(){
    $('#win7').slideToggle();
  });
  $('#win8').hide();
  $("#button8").click(function(){
    $('#win8').fadeIn();
  });
  $("#button9").click(function(){
    $('#win9').fadeOut();
  });
  $("#button10").click(function(){
    $('#win10').addClass('addedclass');
  });
  $("#button11").click(function(){
    $('.bpara').before(" this was added before the paragraph");
  });
  $("#button12").click(function(){
    $('.apara').after("this was added after the paragraph");
  });
  $("#button13").click(function(){
    $('.appended').append(" this was appended to the end of this <p>")
  });
  $("#button14").click(function(){
    $('#win14').html("<style> #win14 p{font-size: 10px;} </style><p>The Test text was changed to this with .html")
  });
  $("#button15").click(function(){
    var title = $('#win15').attr("title");
    $('#win15').html("the title of this window is " + title);
  });
  $("#button16").click(function(){
    // $('#button16:textContent').val("val");
  });

  // console.log($('#win16'));
  var text = $("h1:first").text();
  $("#button17").click(function(){
    $("#win17").html(text + '<style> #win17 p{font-size: 12px;</style> <p>This was added by pulling the text in the header via .text, stored in a variable and added to a paragraph with .html</p>');
  });

  $('body').data("randominformation", 1);

  $("#button18").click(function(){
    console.log($('body').data);
    console.log($('body'));
  });
});
