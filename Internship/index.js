var resume = document.querySelectorAll(".resume");
for(var i=0;	i<resume.length;i++)
{
	resume[i].addEventListener("mouseover",function(){
		this.style.backgroundColor='blue';
		this.style.color="white";
	})
	resume[i].addEventListener("mouseout",function(){
		this.style.backgroundColor='white';
		this.style.color="black";
	})
}
var imgjs = document.querySelectorAll(".imgjs");
for(var i=0; i<imgjs.length; i++)
{
	imgjs[i].addEventListener("mouseover",function(){
		this.classList.add("bounce","animated","wow");
	})
	imgjs[i].addEventListener("mouseout",function(){
		this.classList.remove("bounce","animated","wow");
	})
}