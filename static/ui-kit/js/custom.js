const loadingScreen = document.getElementById('loading');
const minimumLoadingTime = 2000;
const startTime = Date.now();

window.onload = function () {
    const elapsedTime = Date.now() - startTime;
    const remainingTime = minimumLoadingTime - elapsedTime;

    setTimeout(() => {
        loadingScreen.style.display = 'none';
    }, Math.max(remainingTime, 0));

    document.getElementById('current-year').textContent = new Date().getFullYear();
};
