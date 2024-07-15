let bioDetailsButtons = document.querySelectorAll('.bio-button');
let bioDetailsElements = document.querySelectorAll('.bio-details');

function toggleBioDetails(index) {
    if (bioDetailsElements[index].style.display === 'block') {
        bioDetailsElements[index].style.display = 'none';
    } else {
        bioDetailsElements[index].style.display = 'block';
    }
}

for (let i = 0; i < bioDetailsButtons.length; i++) {
    bioDetailsButtons[i].addEventListener('click', (function(i) {
        return function() {
            toggleBioDetails(i);
        }
    })(i));
}