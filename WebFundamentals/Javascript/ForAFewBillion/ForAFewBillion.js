var n = .01
var x = false;
var z = false;
var k = 0;
var d = 0;
for(var i = 0; i < 30; i++){
  k += n;
  console.log("Day "+ (i + 1) + "   " + n + "  " + k);
  n*= 2;
  if(k>=10000 && x == false){
    var j = i + 1;
    x = true;
  }
  if(k>=1000000000 && z == false){
    var l = i + 1;
    z = true;
  }
}
n=.01;
var i = 1;
while (d <+ 1000000000){
  d += n;
  n *= 2;
  i++;

}
console.log("Day " + (j) + " is the day we have made 10,000$");
console.log("Day " + (i) + " is the day we have made 1,000,000,000$");
