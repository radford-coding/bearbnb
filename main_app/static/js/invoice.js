const priceEl = document.querySelector('#price');
const rateEl = document.querySelector('#rate');
const nightsEl = document.querySelector('input[name="nights"]');

nightsEl.addEventListener('change', (e) => {
    priceEl.innerText = e.target.value * Number(rateEl.innerText);
});