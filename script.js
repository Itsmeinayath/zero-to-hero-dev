// DOM Elements
const navToggle = document.getElementById('nav-toggle');
const navMenu = document.getElementById('nav-menu');
const navLinks = document.querySelectorAll('.nav-link');

// Mobile Navigation Toggle
navToggle.addEventListener('click', () => {
    navMenu.classList.toggle('active');
    
    // Animate hamburger menu
    const spans = navToggle.querySelectorAll('span');
    spans.forEach((span, index) => {
        if (navMenu.classList.contains('active')) {
            if (index === 0) span.style.transform = 'rotate(45deg) translate(5px, 5px)';
            if (index === 1) span.style.opacity = '0';
            if (index === 2) span.style.transform = 'rotate(-45deg) translate(7px, -6px)';
        } else {
            span.style.transform = 'none';
            span.style.opacity = '1';
        }
    });
});

// Close mobile menu when clicking on nav links
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('active');
        const spans = navToggle.querySelectorAll('span');
        spans.forEach(span => {
            span.style.transform = 'none';
            span.style.opacity = '1';
        });
    });
});

// Smooth scrolling for navigation links
navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = link.getAttribute('href');
        const targetSection = document.querySelector(targetId);
        
        if (targetSection) {
            const navHeight = document.querySelector('.navbar').offsetHeight;
            const targetPosition = targetSection.offsetTop - navHeight;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// Navbar background on scroll
let lastScrollY = window.scrollY;
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    const currentScrollY = window.scrollY;
    
    // Add/remove background based on scroll position
    if (currentScrollY > 50) {
        navbar.style.background = 'rgba(15, 15, 35, 0.98)';
    } else {
        navbar.style.background = 'rgba(15, 15, 35, 0.95)';
    }
    
    // Hide/show navbar on scroll direction
    if (currentScrollY > lastScrollY && currentScrollY > 100) {
        navbar.style.transform = 'translateY(-100%)';
    } else {
        navbar.style.transform = 'translateY(0)';
    }
    
    lastScrollY = currentScrollY;
});

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe elements for animation
const animateOnScroll = document.querySelectorAll('.about-card, .track-card, .resource-card, .timeline-item');
animateOnScroll.forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(el);
});

// Code typing animation (restart when section comes into view)
const codeWindow = document.querySelector('.code-window');
const codeAnimation = document.querySelector('.typing-animation');

const codeObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            // Restart typing animation
            codeAnimation.style.animation = 'none';
            void codeAnimation.offsetWidth; // Trigger reflow
            codeAnimation.style.animation = 'typing 4s steps(40, end), blink-caret 0.75s step-end infinite';
        }
    });
}, { threshold: 0.5 });

if (codeWindow) {
    codeObserver.observe(codeWindow);
}

// Progress timeline animation
const timelineItems = document.querySelectorAll('.timeline-item');
const timelineObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateX(0)';
            
            // Animate timeline marker
            const marker = entry.target.querySelector('.timeline-marker');
            marker.style.transform = 'scale(1)';
        }
    });
}, { threshold: 0.3 });

timelineItems.forEach((item, index) => {
    item.style.opacity = '0';
    item.style.transform = 'translateX(-30px)';
    item.style.transition = `opacity 0.6s ease ${index * 0.1}s, transform 0.6s ease ${index * 0.1}s`;
    
    const marker = item.querySelector('.timeline-marker');
    marker.style.transform = 'scale(0.8)';
    marker.style.transition = `transform 0.3s ease ${index * 0.1}s`;
    
    timelineObserver.observe(item);
});

// Stats counter animation
const stats = document.querySelectorAll('.stat-number');
const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const stat = entry.target;
            const finalValue = stat.textContent;
            
            if (finalValue === '∞') return; // Skip infinity symbol
            
            const numericValue = parseInt(finalValue);
            let currentValue = 0;
            const increment = numericValue / 60; // Animation duration
            
            const timer = setInterval(() => {
                currentValue += increment;
                if (currentValue >= numericValue) {
                    stat.textContent = finalValue;
                    clearInterval(timer);
                } else {
                    stat.textContent = Math.floor(currentValue);
                }
            }, 16); // ~60fps
        }
    });
}, { threshold: 0.5 });

stats.forEach(stat => {
    statsObserver.observe(stat);
});

// Button hover effects
const buttons = document.querySelectorAll('.btn');
buttons.forEach(btn => {
    btn.addEventListener('mouseenter', () => {
        btn.style.transform = 'translateY(-2px) scale(1.02)';
    });
    
    btn.addEventListener('mouseleave', () => {
        btn.style.transform = 'translateY(0) scale(1)';
    });
});

// Track card hover effects
const trackCards = document.querySelectorAll('.track-card');
trackCards.forEach(card => {
    card.addEventListener('mouseenter', () => {
        card.style.transform = 'translateY(-8px) scale(1.02)';
    });
    
    card.addEventListener('mouseleave', () => {
        card.style.transform = 'translateY(0) scale(1)';
    });
});

// Parallax effect for hero section
const heroSection = document.querySelector('.hero');
const heroGrid = document.querySelector('.hero-grid');

window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const rate = scrolled * -0.5;
    
    if (heroGrid && scrolled < window.innerHeight) {
        heroGrid.style.transform = `translate3d(0, ${rate}px, 0)`;
    }
});

// Add loading class to body when page loads
document.addEventListener('DOMContentLoaded', () => {
    document.body.classList.add('loading');
    
    // Remove loading class after a short delay
    setTimeout(() => {
        document.body.classList.remove('loading');
    }, 300);
});

// Easter egg: Konami code
let konamiCode = '';
const konamiSequence = 'ArrowUpArrowUpArrowDownArrowDownArrowLeftArrowRightArrowLeftArrowRightKeyBKeyA';

document.addEventListener('keydown', (e) => {
    konamiCode += e.code;
    
    if (konamiSequence.indexOf(konamiCode) !== 0) {
        konamiCode = '';
    }
    
    if (konamiCode === konamiSequence) {
        // Easter egg effect
        document.body.style.animation = 'rainbow 2s ease-in-out';
        setTimeout(() => {
            document.body.style.animation = '';
        }, 2000);
        konamiCode = '';
    }
});

// Add rainbow animation keyframes
const rainbowKeyframes = `
@keyframes rainbow {
    0%, 100% { filter: hue-rotate(0deg); }
    25% { filter: hue-rotate(90deg); }
    50% { filter: hue-rotate(180deg); }
    75% { filter: hue-rotate(270deg); }
}
`;

const style = document.createElement('style');
style.textContent = rainbowKeyframes;
document.head.appendChild(style);

// Performance monitoring
if ('performance' in window) {
    window.addEventListener('load', () => {
        const loadTime = performance.now();
        console.log(`Page loaded in ${Math.round(loadTime)}ms`);
        
        // Log performance metrics for optimization
        const navigation = performance.getEntriesByType('navigation')[0];
        if (navigation) {
            console.log('Performance metrics:', {
                domContentLoaded: Math.round(navigation.domContentLoadedEventEnd - navigation.domContentLoadedEventStart),
                loadComplete: Math.round(navigation.loadEventEnd - navigation.loadEventStart),
                totalTime: Math.round(navigation.loadEventEnd - navigation.navigationStart)
            });
        }
    });
}

// Handle reduced motion preference
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

function handleReducedMotion(e) {
    if (e.matches) {
        // Disable animations for users who prefer reduced motion
        document.documentElement.style.setProperty('--transition-fast', '0s');
        document.documentElement.style.setProperty('--transition-normal', '0s');
        document.documentElement.style.setProperty('--transition-slow', '0s');
    } else {
        // Re-enable animations
        document.documentElement.style.removeProperty('--transition-fast');
        document.documentElement.style.removeProperty('--transition-normal');
        document.documentElement.style.removeProperty('--transition-slow');
    }
}

prefersReducedMotion.addEventListener('change', handleReducedMotion);
handleReducedMotion(prefersReducedMotion);

// Utility function to debounce scroll events
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Apply debouncing to scroll events
const debouncedScrollHandler = debounce(() => {
    // Additional scroll handling can go here
}, 16);

window.addEventListener('scroll', debouncedScrollHandler);

console.log('🚀 Zero to Hero Developer Journey - Landing Page Loaded Successfully!');
console.log('💡 Tip: Try the Konami code for a surprise!');
console.log('📧 Built with modern web technologies and best practices');