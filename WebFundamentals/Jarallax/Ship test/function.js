$(document).ready(function(){

})

init = function(){
  var jarallax = new Jarallax();
  jarallax.addAnimation('.ship',[{progress: '0%', top: "0%"},{progress:"100%", top:"75%"}]);
  jarallax.addAnimation('.clouds',[{progress: '0%', top: "100%"},{progress:"100%", top:"-100%"}]);
  jarallax.addAnimation('.clouds1',[{progress: '0%', top: "55%"},{progress:"100%", top:"0%"}]);

}
