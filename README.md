# EmoTunes

## Tune into Your Emotions

EmoTunes is a web application that integrates emotion detection, weather classification, and personalized music recommendations to provide a unique and engaging experience. It uses a combination of OpenCV, TensorFlow, Flask, and various web technologies to deliver a seamless interaction between detecting your emotions, understanding the current weather, and recommending music that matches your mood and environment.

## Features
- **Emotion Detection**: Detects facial emotions in real-time using a webcam and a pre-trained model.
- **Weather Classification**: Fetches the current weather based on the user's location and classifies it.
- **Music Recommendations**: Recommends music playlists based on the detected emotion and current weather.
- **Voice Notes**: Plays specific voice notes based on the combination of detected emotions and weather conditions.

## Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/<your-username>/EmoTunes.git
   cd EmoTunes
   ```

2. **Install Dependencies**:
   Make sure you have Python and pip installed. Then run:
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```sh
   python app.py
   ```

4. **Open in Browser**:
   Open your browser and go to `http://localhost:5000`.

## Files Structure
- **app.py**: Main Flask application file.
- **emotion_detection.py**: Contains the function to detect emotions using OpenCV and TensorFlow.
- **weather_detection.py**: Fetches and classifies the current weather.
- **music_recommendation.py**: Recommends music playlists based on emotion and weather.
- **templates/**: Contains the HTML files.
  - `index.html`: Main interface of the application.
- **static/**: Contains static files like CSS, JavaScript, and images.
  - `css/style.css`: Custom styles for the application.
  - `js/script.js`: JavaScript for handling video and emotion detection.
  - `images/background.jpg`: Background image.

## Usage

1. **Start Emotion Detection**:
   - Open the application in your browser.
   - Allow access to your webcam.
   - Click the "Get Recommendation" button to start detecting your emotion.

2. **Get Music Recommendations**:
   - The app will display the most commonly detected emotion.
   - It will fetch the current weather and recommend music playlists based on both the emotion and the weather.

## Deployment

### Using GitHub Pages
1. **Push your repository** to GitHub.
2. **Enable GitHub Pages** in the repository settings.

## Acknowledgements
- Thanks to [Font Awesome](https://fontawesome.com/) for icons.
- Inspired by the power of integrating technology with everyday experiences.

```
