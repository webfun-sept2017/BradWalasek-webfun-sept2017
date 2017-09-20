var daysUntilMyBirthday = 100;

for(var i = daysUntilMyBirthday; i > 0; i--){
  if (i>30) {
    console.log(i + " more days until my Birthday. Time to wait and watch the calander...");
  }
  else if (i<=30 && i >5) {
    console.log(i + " more days until the special day, I can't wait!!");
  }
  else {
    console.log(i +" DAYS UNTIL MY BIRTHDAY!!!");
  }
}
console.log("PARTY TIME!!!")
