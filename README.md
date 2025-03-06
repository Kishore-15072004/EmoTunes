
# EmoTunes

## Tune into Your Emotions 🎶

EmoTunes is an innovative web application that combines **emotion detection**, **weather classification**, and **personalized music recommendations** to deliver a unique, mood-based musical experience. Using technologies like OpenCV, TensorFlow, Flask, and modern web frameworks, EmoTunes bridges the gap between emotion, environment, and music!

---

## ✨ Features
- **Real-Time Emotion Detection**: Recognizes facial emotions using a webcam and a pre-trained model.
- **Weather Awareness**: Retrieves and classifies the current weather for a personalized touch.
- **Curated Music Recommendations**: Suggests playlists that align with your emotions and the weather.
- **Dynamic Voice Notes**: Plays customized voice notes based on emotion and weather combinations.

---

## 🚀 Installation

Follow these steps to get started:

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/<your-username>/EmoTunes.git
   cd EmoTunes
   ```

2. **Install Dependencies**:
   Ensure Python and pip are installed on your system, then run:
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```sh
   python app.py
   ```

4. **Access the App**:
   Open your browser and navigate to `http://localhost:5000`.

---

## 📂 Folder Structure
- **app.py**: Main backend logic of the application.
- **emotion_detection.py**: Module for detecting facial emotions using OpenCV and TensorFlow.
- **weather_detection.py**: Retrieves and analyzes real-time weather data.
- **music_recommendation.py**: Generates mood-based music suggestions.
- **templates/**: Contains HTML files.
  - `index.html`: Core user interface.
- **static/**: Stores static resources like CSS, JavaScript, and images.
  - `css/style.css`: Stylesheets for the app interface.
  - `js/script.js`: JavaScript logic for interactivity.
  - `images/background.jpg`: Default background for the app.

---

## 🎯 How to Use

1. **Start the App**:
   - Run the app and open it in your browser.
   - Grant permission to access your webcam.

2. **Detect Emotions**:
   - Press "Get Recommendation" to capture your emotion in real-time.

3. **Music Recommendations**:
   - Based on your emotion and the current weather, the app will suggest playlists to match your mood.

---

## 📊 Dataset

To train or improve the emotion detection model, download the [Face Expression Recognition Dataset](https://www.kaggle.com/datasets/jonathanoheix/face-expression-recognition-dataset) from Kaggle.

---

## 🌐 Deployment Options

### Hosting Locally
Run the application on your local machine by following the installation steps.

### GitHub Pages
1. Push your repository to GitHub.
2. Enable **GitHub Pages** in the repository settings for easy deployment.

---

## 🙏 Acknowledgements
- **Frameworks & Tools**: [TensorFlow](https://www.tensorflow.org/), [OpenCV](https://opencv.org/), [Flask](https://flask.palletsprojects.com/).
- **Icons**: Courtesy of [Font Awesome](https://fontawesome.com/).
- Inspired by the integration of emotions, technology, and music!

---
