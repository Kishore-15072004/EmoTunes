const video = document.querySelector("#videoElement");

if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true })
        .then((stream) => {
            video.srcObject = stream;
        })
        .catch((error) => {
            console.error("Error accessing camera:", error);
        });
}

class AudioManager {
    constructor() {
        if (AudioManager.instance) {
            return AudioManager.instance;
        }
        this.audio = null;
        AudioManager.instance = this;
    }

    async playVoiceNote(emotion) {
        console.log(`Attempting to play voice note for emotion: ${emotion}`);
        const audioPath = `/static/audio/${emotion}.mp3`;

        if (this.audio !== null && !this.audio.paused) {
            this.audio.pause();
            this.audio.currentTime = 0;
            this.audio.removeEventListener('ended', this.onEnded);
        }

        this.audio = new Audio(audioPath);

        try {
            this.audio.addEventListener('canplaythrough', async () => {
                try {
                    await this.audio.play();
                    console.log(`Playing voice note for emotion: ${emotion}`);
                } catch (error) {
                    console.error(`Error playing audio file (${audioPath}):`, error);
                    this.audio = null;
                }
            }, { once: true });

            this.audio.load();

            this.onEnded = () => {
                console.log(`Voice note for emotion: ${emotion} has ended`);
                this.audio = null;
            };
            this.audio.addEventListener('ended', this.onEnded, { once: true });

        } catch (error) {
            console.error(`Error setting up audio file (${audioPath}):`, error);
            this.audio = null;
        }
    }
}

const audioManager = new AudioManager();

async function captureFrames(count = 3) {  // Reduce frame count
    const frames = [];
    const interval = 100;  // Reduce interval to 100 milliseconds

    for (let i = 0; i < count; i++) {
        const canvas = document.createElement('canvas');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        const context = canvas.getContext('2d');

        context.translate(canvas.width, 0);
        context.scale(-1, 1);
        context.drawImage(video, 0, 0, canvas.width, canvas.height);

        frames.push(canvas.toDataURL('image/png'));
        await new Promise(resolve => setTimeout(resolve, interval));
    }

    return frames;
}

async function startEmotionDetection() {
    const button = document.getElementById('recommendButton');
    const spinner = document.getElementById('loadingSpinner');
    spinner.style.display = 'block';
    button.disabled = true;

    const combinedEmotionResult = document.getElementById('combinedEmotionResult');
    const weatherResult = document.getElementById('weatherResult');

    if (combinedEmotionResult) combinedEmotionResult.textContent = "Detecting emotion...";
    if (weatherResult) weatherResult.textContent = "Fetching weather...";

    const framesData = await captureFrames();

    try {
        const response = await fetch('/recommend', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ images: framesData })
        });

        const data = await response.json();
        if (data.error) {
            alert(`Error: ${data.error}`);
            button.disabled = false;
            spinner.style.display = 'none';
            return;
        }

        if (combinedEmotionResult) combinedEmotionResult.textContent = `Emotion: ${data.combined_emotion}`;
        if (weatherResult) weatherResult.textContent = `Weather: ${data.weather}`;

        await audioManager.playVoiceNote(data.combined_emotion);

        const playlistsDiv = document.getElementById('playlists');
        playlistsDiv.innerHTML = '';
        data.playlists.forEach(playlist => {
            const iframe = document.createElement('iframe');
            iframe.src = `https://open.spotify.com/embed/playlist/${playlist.split('/').pop()}`;
            iframe.frameBorder = '0';
            iframe.allow = 'encrypted-media';
            playlistsDiv.appendChild(iframe);
        });
    } catch (error) {
        console.error("Error detecting emotion:", error);
    } finally {
        spinner.style.display = 'none';
        button.disabled = false;
    }
}

window.addEventListener('beforeunload', (event) => {
    if (audioManager.audio !== null) {
        audioManager.audio.pause();
        audioManager.audio.currentTime = 0;
        audioManager.audio = null;
    }
});

document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'hidden' && audioManager.audio !== null) {
        audioManager.audio.pause();
        audioManager.audio.currentTime = 0;
        audioManager.audio = null;
    }
});
