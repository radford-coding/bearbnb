let slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
    showSlides(slideIndex += n);
}

function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("slide");
    if (n > slides.length) { slideIndex = 1 }
    if (n < 1) { slideIndex = slides.length }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slides[slideIndex - 1].style.display = "block";
}

const priceEl = document.querySelector('#price');
const rateEl = document.querySelector('#rate');
const nightsEl = document.querySelector('input[name="nights"]');

nightsEl.addEventListener('change', (e) => {
    priceEl.innerText = e.target.value * Number(rateEl.innerText);
});