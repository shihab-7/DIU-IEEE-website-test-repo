// mobile view navbar control 
document.addEventListener('DOMContentLoaded', () => {
    const menuButton = document.querySelector('[aria-controls="mobile-menu"]');
    const mobileMenu = document.getElementById('mobile-menu');
    const menuLinks = mobileMenu.querySelectorAll('a');

    menuButton.setAttribute('aria-expanded',false);
    mobileMenu.classList.add('hidden');

    menuButton.addEventListener('click', () => {
        const isExpanded = menuButton.getAttribute('aria-expanded') === 'true';
        menuButton.setAttribute('aria-expanded', !isExpanded);
        mobileMenu.classList.toggle('hidden');
    });

    menuLinks.forEach(link => {
        link.addEventListener('click', () => {
            menuButton.setAttribute('aria-expanded', false);
            mobileMenu.classList.add('hidden');
        });
    });
});

// carousel control
document.addEventListener('DOMContentLoaded', () => {
    const carousel = document.getElementById('carousel');
    const slides = carousel.children;
    const totalSlides = slides.length;
    let currentIndex = 0;

    function moveToNextSlide() {
        currentIndex = (currentIndex + 1) % totalSlides;
        const offset = -currentIndex * 100
        carousel.style.transform = `translateX(${offset}%)`;
    }
    setInterval(moveToNextSlide, 5000);
});

