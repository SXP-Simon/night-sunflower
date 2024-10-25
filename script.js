let currentSlide = 0;
const slides = document.querySelectorAll('.carousel img');
const totalSlides = slides.length; // Include the duplicate image for seamless loop
const carouselContainer = document.querySelector('.carousel-container');

function showSlide(index) {
  // Normalize the index to be within the range of slides
  if (index >= totalSlides) {
    index = 0; // Reset to the first slide
  } else if (index < 0) {
    index = totalSlides - 1; // Go to the last slide
  }
  carouselContainer.style.transform = `translateX(-${index * 25}%)`;
  currentSlide = index;
}

function nextSlide() {
  showSlide(currentSlide + 1);
}

function prevSlide() {
  showSlide(currentSlide - 1);
}

document.getElementById('nextBtn').addEventListener('click', nextSlide);
document.getElementById('prevBtn').addEventListener('click', prevSlide);

// Automatically change slide every 6 seconds
setInterval(nextSlide, 6000);

// Initially show the first slide
showSlide(0);