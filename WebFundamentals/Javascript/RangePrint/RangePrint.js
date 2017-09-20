printRange(2,10,2);




function printRange(s,e,n) {

if (e == 0){
  e = s;
  s = 0;
}
if (n == 0){
  n = 1;
}




  if (e > s){
    for(var i = s; i < e; i += n){
      console.log(i);
    }
  }
  else if (s > e){
    for(var i = s; i > e; i -= n){
      console.log(i);
    }
  }

}
