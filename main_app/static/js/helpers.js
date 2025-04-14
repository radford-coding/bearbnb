const uploadEl = document.querySelector('#file-upload');
const displayUploadEl = document.querySelector('#uploaded-file-name');

uploadEl.addEventListener('change', (e) => {
    let path = e.target.value.split('\\');
    displayUploadEl.innerText = path[path.length - 1];
});