var oldArr = [1,"apple",-3,"orange",0.5];
var newArr = [];
numberOnly(oldArr);
function numberOnly(arr){
  for (var i = 0; i < arr.length; i++) {
    // console.log(arr[i]);
    // console.log(typeof arr[i]);
    if (typeof arr[i] === 'number') {
      // console.log("test worked");
      newArr.push(arr[i]);

    }
  }
}
console.log(newArr);
