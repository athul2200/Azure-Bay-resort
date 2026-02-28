// Header Sticky Logic
const header = document.getElementById('header');
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        header.classList.add('sticky');
    } else {
        header.classList.remove('sticky');
    }
});

// Hero Slider logic
const slides = document.querySelectorAll('.hero-slide');
let currentSlide = 0;

function nextSlide() {
    if (slides.length === 0) return;
    slides[currentSlide].classList.remove('active');
    currentSlide = (currentSlide + 1) % slides.length;
    slides[currentSlide].classList.add('active');
}

if (slides.length > 0) {
    setInterval(nextSlide, 5000);
}

// Mobile Menu Toggle
const menuToggle = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');

if (menuToggle) {
    menuToggle.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });
}

// Close menu when a link is clicked
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        navLinks.classList.remove('active');
    });
});

// Smooth Scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const targetId = this.getAttribute('href');
        if (targetId === '#') return;
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            e.preventDefault();
            targetElement.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});
// Gallery Lightbox Logic
const lightbox = document.querySelector('.lightbox');
const lightboxImg = document.querySelector('.lightbox-img');
const lightboxClose = document.querySelector('.lightbox-close');
const lightboxPrev = document.querySelector('.lightbox-prev');
const lightboxNext = document.querySelector('.lightbox-next');
const galleryItems = document.querySelectorAll('.gallery-detail-item img');

let currentGalleryIndex = 0;

if (lightbox && galleryItems.length > 0) {
    // Open Lightbox
    galleryItems.forEach((item, index) => {
        item.addEventListener('click', () => {
            currentGalleryIndex = index;
            showLightboxImage();
            lightbox.classList.add('active');
            document.body.style.overflow = 'hidden'; // Prevent scrolling
        });
    });

    // Show Image
    function showLightboxImage() {
        lightboxImg.src = galleryItems[currentGalleryIndex].src;
    }

    // Next Image
    function nextGalleryImage() {
        currentGalleryIndex = (currentGalleryIndex + 1) % galleryItems.length;
        showLightboxImage();
    }

    // Previous Image
    function prevGalleryImage() {
        currentGalleryIndex = (currentGalleryIndex - 1 + galleryItems.length) % galleryItems.length;
        showLightboxImage();
    }

    // Event Listeners
    lightboxNext.addEventListener('click', (e) => {
        e.stopPropagation();
        nextGalleryImage();
    });

    lightboxPrev.addEventListener('click', (e) => {
        e.stopPropagation();
        prevGalleryImage();
    });

    lightboxClose.addEventListener('click', () => {
        lightbox.classList.remove('active');
        document.body.style.overflow = 'auto';
    });

    // Close on overlay click
    lightbox.addEventListener('click', (e) => {
        if (e.target === lightbox || e.target.classList.contains('lightbox-content')) {
            lightbox.classList.remove('active');
            document.body.style.overflow = 'auto';
        }
    });

    // Keyboard Navigation
    window.addEventListener('keydown', (e) => {
        if (!lightbox.classList.contains('active')) return;

        if (e.key === 'ArrowRight') {
            nextGalleryImage();
        } else if (e.key === 'ArrowLeft') {
            prevGalleryImage();
        } else if (e.key === 'Escape') {
            lightbox.classList.remove('active');
            document.body.style.overflow = 'auto';
        }
    });
}

// Resort Showcase Slider (About Page)
const resortSlides = document.querySelectorAll('.resort-slide');
const resortDotBtns = document.querySelectorAll('.resort-dot');
let currentResortSlide = 0;
let resortSliderInterval;

function showResortSlide(index) {
    resortSlides.forEach(s => s.classList.remove('active'));
    resortDotBtns.forEach(d => d.classList.remove('active'));
    currentResortSlide = (index + resortSlides.length) % resortSlides.length;
    resortSlides[currentResortSlide].classList.add('active');
    resortDotBtns[currentResortSlide].classList.add('active');
}

function startResortSlider() {
    resortSliderInterval = setInterval(() => {
        showResortSlide(currentResortSlide + 1);
    }, 3500);
}

if (resortSlides.length > 0) {
    resortDotBtns.forEach(dot => {
        dot.addEventListener('click', () => {
            clearInterval(resortSliderInterval);
            showResortSlide(parseInt(dot.dataset.index));
            startResortSlider();
        });
    });

    startResortSlider();
}
