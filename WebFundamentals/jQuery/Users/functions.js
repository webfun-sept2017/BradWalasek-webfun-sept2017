$(document).ready(function(){

  console.log($('#test'));
  $('button').click(function(){
    $('table').append('<tr><td>'+$('#fn').val()+'</td><td>'+$('#ln').val()+'</td><td>'+$('#ea').val()+'</td><td>'+$('#pn').val()+'</td></tr>');
  });
})
