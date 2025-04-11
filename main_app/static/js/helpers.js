const priceEl = document.querySelector('#price');
const rateEl = document.querySelector('#rate');
const nightsEl = document.querySelector('input[name="nights"]');

nightsEl.addEventListener('change', (e) => {
    priceEl.innerText = e.target.value * Number(rateEl.innerText);
});

const uploadEl = document.querySelector('#file-upload');
const displayUploadEl = document.querySelector('#uploaded-file-name');

uploadEl.addEventListener('change', (e) => {
    let path = e.target.value.split('\\');
    displayUploadEl.innerText = path[path.length - 1];
});