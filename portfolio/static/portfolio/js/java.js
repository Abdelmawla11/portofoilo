// start add and remove active classes
const Links = document.querySelectorAll('.btn');
function handleNavClick(event) {
  Links.forEach(link => {
    link.classList.remove('active');
  });
  event.target.classList.add('active');}

Links.forEach(link => {link.addEventListener('click', handleNavClick);});
// end add and remove active classes
let slideIndex = 0;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n - 1); // Adjust index to start from 0
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");

  if (n >= slides.length) {
    slideIndex = 0;
  }
  if (n < 0) {
    slideIndex = slides.length - 1;
  }

  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }

  slides[slideIndex].style.display = "block";  
  dots[slideIndex].className += " active";
}