{
  document.querySelector(".envelope").addEventListener("click", function () {
   this.classList.toggle("fold");
 });
 
 setTimeout(function () {
   document.querySelector(".envelope").classList.add("fold");
 }, 2000);
 }