<style>
  .carousel {
    overflow: hidden;
    position: relative;
    width: 600px;
    height: 400px;
    margin: auto;
  }
  .carousel-container {
    display: flex;
    width: calc(100% * 3); /* 3 images */
    position: relative;
    transition: transform 0.5s ease-in-out;
  }
  .carousel img {
    width: calc(100% / 3); /* 3 images */
    height: 100%;
    flex-shrink: 0;
  }
  #prevBtn, #nextBtn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background-color: rgba(0, 0, 0, 0.5);
    color: white;
    padding: 10px;
    cursor: pointer;
    border: none;
  }
  #prevBtn {
    left: 10px;
  }
  #nextBtn {
    right: 10px;
  }
</style>
</head>
<body>

<div class="carousel">
  <div class="carousel-container">
    <img src="吾王.jpg" alt="Image 1">
    <img src="素晴日2.jpg" alt="Image 2">
    <img src="美咲.jpg" alt="Image 3">
    <img src="吾王.jpg" alt="Image 1"> <!-- Duplicate of the first image for seamless loop -->
  </div>
  <button id="prevBtn">Prev</button>
  <button id="nextBtn">Next</button>
</div>

<script>
  let currentSlide = 0;
  const slides = document.querySelectorAll('.carousel img');
  const totalSlides = slides.length - 1; // Exclude the duplicate image
  const carouselContainer = document.querySelector('.carousel-container');

  function showSlide(index) {
    if (index >= totalSlides) {
      // Reset to the first slide
      index = 0;
    }
    carouselContainer.style.transform = `translateX(-${index * 100 / totalSlides}%)`;
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
</script>

</body>