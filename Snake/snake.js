var x = 0
var y= 0
var xSpeed=20;
var ySpeed=20;
var rectrandX = Math.floor((Math.random() * 580) + 1);
var rectrandY = Math.floor((Math.random() * 580) + 1);
var food = ["0"];
var totalBlack = 0;
var snakecount= 0;


function makeRect(){
	fill(1,0,0);
	rect(rectrandX,rectrandY,20,20);
}



 function checkColor(pixels,value){
     var count_value = 0;
     for(var l=0;l<=pixels.length;l++){
         if(pixels[l]==value) 
             count_value+=1;
     }
  return count_value;

 }


function setup(){
	background(9,169,209);
	createCanvas(600,600);
	 makeRect();
	 loadPixels();   
     totalBlack = checkColor(pixels, 1);
}



function draw(){
	background(9,169,209);
    fill(1,0,0);
	rect(rectrandX,rectrandY,20,20);

	if (food[0] == "0"){
		fill(0,255,0);
		rect(x,y,20,20);

	}	

	
	
    if (keyCode=="39" && x < 570){
        x += xSpeed;
    }
   
    if(keyCode == "37" && x > 0) {
        x -= xSpeed;
    }
    
    if(keyCode == "38" && y >= 0) {
        y -= ySpeed;
    }
    

    if(keyCode == "40" && y < 570) {
        y += ySpeed;
    }
 	loadPixels();
     if(checkColor(pixels, 1) < totalBlack){
     	alert("Inside");
     	snakecount += 1;
        //adding to tail of snake
        append(food,snakecount);
        //redrawing box
         rectrandX = Math.floor((Math.random() * 580) + 1);
         rectrandY = Math.floor((Math.random() * 580) + 1);
         //fill(1,0,0);
         //rect(rectRandX,rectRandY,25,25)

         


     }
}






// function checkKey(e) {

//     e = e || window.event;

//     if (e.keyCode == '38') {
//         // up arrow
//     }
//     else if (e.keyCode == '40') {
//         // down arrow
//     }
//     else if (e.keyCode == '37') {
//        // left arrow
//     }
//     else if (e.keyCode == '39') {
//        // right arrow
//     }

// }