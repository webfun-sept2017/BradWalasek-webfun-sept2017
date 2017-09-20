  var hour = 7;
  var min = 15;
  var period = "PM";
  var k;
  var j;
  if (min < 30){
    k = "It's just after " + hour + " in the "
  }
  else {
    hour ++;
    k = "It is almost " + hour + " in the "
  }
  if(period == "AM"){
    j = "morning.";
  }
  else {
    j = "evening."
  }
  console.log(k + j);
