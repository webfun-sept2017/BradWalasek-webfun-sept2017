var testArray = ["James", "Jill", "Jane", "Jack"];
var sign = "-->"
var extra = true;
var falseExtra = false;
fancyArray(testArray,sign, extra);
fancyArray(testArray,sign, falseExtra);

function fancyArray(arr, sym, reversed) {
  if (reversed == false){
    for (var i = 0; i < testArray.length; i++) {
      console.log(i + " " + sym + " " + testArray[i]);
    }
  }  else {
      for (var i = testArray.length; i > 0; i--) {
        console.log((i-1) + " " + sym + " " + testArray[i - 1]);
      }
    }
}
