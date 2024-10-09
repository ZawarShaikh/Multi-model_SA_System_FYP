// Text Script
var formsSection = document.getElementById('forms-section');
formsSection.style.display = 'none'


// Get all image elements and add event listener
var images = document.querySelectorAll('.analysis-image');
//const pidInput = document.getElementById('selected-pid');
const pidTextInput = document.getElementById('pid-text');
const pidAudioInput = document.getElementById('pid-audio');
const pidVideoInput = document.getElementById('pid-video');


// Function to show forms when click event occurs 
function showForms(event) {
    formsSection.style.display = 'block';

    // Get the pid from the clicked image
    //const pid = event.currentTarget.getAttribute('data-pid');
    //pidInput.value = pid;  // Set the hidden field with the selected pid

    const selectedPid = this.getAttribute('data-pid'); // Get the pid from the clicked image
    pidTextInput.value = selectedPid; // Set the pid for the text review
    pidAudioInput.value = selectedPid; // Set the pid for the audio review
    pidVideoInput.value = selectedPid; // Set the pid for the video review
}

// Attach event listeners to each image
images.forEach(function(image) {
    image.addEventListener('click', showForms);
});



// Audio script
let mediaRecorder;
let audioChunks = [];
const recordButton = document.getElementById('record-audio');
const stopButton = document.getElementById('stop-audio');
const audioPlayback = document.getElementById('audio-playback');
const recordedAudioInput = document.getElementById('recorded-audio');

recordButton.addEventListener('click', () => {
    navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
        mediaRecorder = new MediaRecorder(stream);
        mediaRecorder.start();
        audioChunks = [];

        mediaRecorder.ondataavailable = event => {
            audioChunks.push(event.data);
        };

        mediaRecorder.onstop = () => {
            const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
            const audioUrl = URL.createObjectURL(audioBlob);
            audioPlayback.src = audioUrl;

            // Convert to base64 and set to hidden input
            const reader = new FileReader();
            reader.readAsDataURL(audioBlob);
            reader.onloadend = function() {
                recordedAudioInput.value = reader.result;
            };
        };

        recordButton.disabled = true;
        stopButton.disabled = false;
    });
});

stopButton.addEventListener('click', () => {
    mediaRecorder.stop();
    recordButton.disabled = false;
    stopButton.disabled = true;

    console.log(recordedAudioInput.value);  // Print Base64 string for verification
});
  
