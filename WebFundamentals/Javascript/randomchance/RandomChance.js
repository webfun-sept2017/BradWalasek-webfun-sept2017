var quarters = 100;
var remain = randomChance(quarters);
if (remain >0 ){
console.log("the number remaining after winning is " + remain);
}
else{
  console.log("there is nothing left, you've lost!");
}
function randomChance(n) {


for (var i = 0; i < n; n--) {
  var chance = Math.trunc(100*(Math.random()))
    // console.log(chance);
    if(chance == 50){
      n += 50 + (Math.floor(Math.random() * 51))
      return n;
    }
  }
  return 0;
}
