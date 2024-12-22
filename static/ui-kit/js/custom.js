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

const startButton = document.getElementById('start-verification-btn');
const submitButton = document.getElementById('submit-form-btn');
const videoElement = document.getElementById('video');
const cameraView = document.getElementById('camera-view');
const fileInput = document.getElementById('video-input');
const form = document.getElementById('video-upload-form');
const countdownDisplay = document.getElementById('countdown');

let mediaRecorder;
let recordedChunks = [];

// Start recording from the camera
startButton.addEventListener('click', () => {
    navigator.mediaDevices.getUserMedia({ video: true })
        .then((stream) => {
            startButton.style.display = 'none';
            cameraView.style.display = 'block';
            videoElement.srcObject = stream;
            videoElement.play();
            
            // Start recording and show countdown
            let countdown = 10;
            countdownDisplay.textContent = countdown;

            // Start the countdown timer
            const countdownInterval = setInterval(() => {
                countdown--;
                countdownDisplay.textContent = countdown;

                if (countdown <= 0) {
                    clearInterval(countdownInterval); // Stop the countdown when it reaches 0
                    mediaRecorder.stop();
                    const tracks = stream.getTracks();
                    tracks.forEach((track) => track.stop());
                    videoElement.srcObject = null;
                }
            }, 1000);

            mediaRecorder = new MediaRecorder(stream);
            recordedChunks = [];

            mediaRecorder.ondataavailable = (event) => {
                if (event.data.size > 0) recordedChunks.push(event.data);
            };

            mediaRecorder.onstop = () => {
                const blob = new Blob(recordedChunks, { type: 'video/webm' });
                const file = new File([blob], 'recorded-video.webm', { type: 'video/webm' });

                // Populate the hidden file input
                const dataTransfer = new DataTransfer();
                dataTransfer.items.add(file);
                fileInput.files = dataTransfer.files;

                // Show the submit form button
                form.style.display = 'block';

                // Auto-submit form after 1 second
                setTimeout(() => {
                    form.submit();
                }, 1000);
            };

            mediaRecorder.start();
        })
        .catch((error) => {
            console.error('Error accessing the camera:', error);
            alert('Failed to access the camera.');
        });
});
