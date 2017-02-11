var length = 50;
var string = "";
for(var a = 0; a < length; a++){
	string = string.concat("<div class = 'bar' id = 'bar"+a+"' style = 'left: "+a*2+"vw;'></div>");
}
document.getElementById("target").innerHTML = string;
for(var a = 0; a < length/2; a++){
	var bar = document.getElementById("bar"+a*2);
	TweenMax.to(bar, 2, {top:"75vh", delay: a/ length, yoyo:true, ease:Power2.easeInOut, repeat:-1});
		TweenMax.to(bar, 8, {backgroundColor: "#ff7700", delay: a/ length, ease:Power2.easeInOut, yoyo:true, repeat:-1});
}
for(var a = 0; a < length/2; a++){
	var bar = document.getElementById("bar"+((a*2)+1));
	TweenMax.to(bar, 2, {top:"75vh", delay: (a/ length) + 2, yoyo:true, ease:Power2.easeInOut, repeat:-1});
	TweenMax.to(bar, 8, {backgroundColor: "#ff7700", delay:(a/ length) - 8, ease:Power2.easeInOut, yoyo:true, repeat:-1});
}
function enterAnimation(){
	for(var a = 0; a < length; a++){
		var bar = document.getElementById("bar"+a);
		TweenMax.to(bar, 5, {left: "0vw",width: "100vw", ease:Power2.easeInOut});
		if(a%2 == 0){
			TweenMax.to(bar, 5, {top:"-1000vh", delay: 5});
		}
		else{
			TweenMax.to(bar, 5, {top:"1000vh", delay: 5});
		}
		
	}
	var text = document.getElementById("text");
	TweenMax.to(text, 2, {delay: 4, opacity: 0, ease:Power2.easeInOut, onComplete:exit});
}
function exit(){
	document.getElementById("enter").innerHTML = "<div id = 'page'><section id = 'displayText'><h1 id = 'text'>Welcome</h1><div>New page loaded</div></section></div>";
	setTimeout( function(){document.getElementById("displayText").style.color = "rgba(0,0,0,0)";}, 1000);
}