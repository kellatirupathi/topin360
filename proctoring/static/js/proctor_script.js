const USER_ID_KEY = "user_id="
const ASSESSMENT_ID_KEY = "assessment_id="

const socket = new WebSocket('ws://127.0.0.1:8000/ws/live-proctoring?uid=user-1&testId=test-1');

//GETTING IDS FROM URL
const urlString = document.location.href;
const url = new URL(urlString)
const USER_ID = url.searchParams.get('student-id');
const ASSESSMENT_ID = url.searchParams.get('assessment-id');

const videoPreview = document.getElementById("videoPreview");
const startRecordingButton = document.getElementById("startRecording");
const stopRecordingButton = document.getElementById("stopRecording");
const downloadLink = document.getElementById("downloadLink");

let mediaRecorder;
let recordedChunks = [];

//startRecordingButton.addEventListener("click", startRecording);
stopRecordingButton.addEventListener("click", stopRecording);

startRecording();

async function startRecording() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({video:{ width: 1280, height: 720, audioBitsPerSecond: 128000,
        videoBitsPerSecond: 2500000, mimeType: "video/mp4", }, audio:true});
        sendIds(USER_ID, ASSESSMENT_ID);
        videoPreview.srcObject = stream;
        mediaRecorder = new MediaRecorder(stream);
        mediaRecorder.ondataavailable = (event) => {
            if (event.data.size > 0 || true) {
                recordedChunks.push(event.data);
                socket.send(event.data)
            }
        };

        mediaRecorder.onstop = () => {
            const videoBlob = new Blob(recordedChunks, { type: "video/mp4" });
            recordedChunks = [];
            socket.send(videoBlob);
            socket.close();
            const videoURL = URL.createObjectURL(videoBlob);
            downloadLink.href = videoURL;
            downloadLink.style.display = "block";
            downloadLink.download = "recorded-video.webm";
        };

        mediaRecorder.start(1000);
//        startRecordingButton.disabled = true;
        stopRecordingButton.disabled = false;
    } catch (error) {
        console.error("Error starting recording:", error);
    }
}

function stopRecording() {
    if(confirm("Are you sure?")){
        if (mediaRecorder && mediaRecorder.state === "recording") {
            videoPreview.srcObject = null;
            mediaRecorder.stop();
//            startRecordingButton.disabled = false;
            stopRecordingButton.disabled = true;
        }
        close();
    }
}

function sendIds(uid, aid){
    socket.send(
        JSON.stringify({
            'uid': uid,
            'aid': aid
        })
    );
}
