var c=document.querySelector('canvas');
var g = c.getContext('2d');


function Point(x,y) { this.x=x;this.y= y;}
Point.prototype = {
  add:function(p) { 
    return new Point(this.x+p.x,
                     this.y+p.y);
  },
   subtract:function(p) { 
    return new Point(this.x-p.x,
                     this.y-p.y);
  },
  fromPolar:function(theta, r) {
    return new Point(r*Math.sin(theta), r*Math.cos(theta));
  },
  normalize:function() {
    var len = Math.pow(this.x*this.x+
                       this.y*this.y,0.5);
    this.x/=len;
    this.y/=len;
    return this;
  },
  scaleBy:function(scalar) { 
    this.x*=scalar;
		this.y*=scalar;
    return this;
  }
}

function RegularPolygon(center, radius,points, offset) {
  var pts = [];
 for(var i =0;i<points;i++) {
   
   var pt = center.add(new Point().fromPolar(i/points*Math.PI*2+offset,radius))
   pts.push(pt);
 }  
  
 this.pts =pts; 
}


function update() {
	c.width = innerWidth;  
  c.height = innerHeight;
  var now = new Date().getTime()/300;
  
  g.translate(innerWidth/2,innerHeight/2);
  g.rotate(Math.PI/4*Math.sin(now/1)+Math.PI/4);
  
  g.translate(-innerWidth/2,-innerHeight/2);
  
  var o = [1,1,0.99];
  for(var i =-1;i<2;i++) {
  var center = new Point(innerWidth/2+i*180, innerHeight/2);
  var rp = new RegularPolygon(center, 103, 40, now*(((i+1)%2)-0.5)+o[i+1]);
 rp.pts.forEach(function(pt,i,pts){
   if(i%4<2) {
     pts[i] = pts[i].subtract(center).scaleBy(0.75).add(center);
   }
   
 }); 
  g.fillStyle = "#383838";
    g.shadowColor = "rgba(255,255,255,0.05)";
    g.shadowBlur = 30;

  g.beginPath();
  rp.pts.forEach(function(pt) {
    g.lineTo(pt.x,pt.y);
  });
  g.lineTo(rp.pts[0].x, rp.pts[0].y);
    g.arc(center.x,center.y, 60, 0,7);
  g.fill();
g.beginPath();
    g.arc(center.x,center.y, 55, 0,7);
    g.arc(center.x,center.y, 40, 0,7);
    g.fill('evenodd');
  
  
  
  
  }
  
  requestAnimationFrame(update);
}


update();