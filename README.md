# Emotion and Weather-Based Music Recommender System Using Live Video Feed

## Overview

This project, **EmoTunes**, is a web application that recommends music playlists based on the user's detected emotion (from a live video feed) and the current weather. It leverages deep learning for emotion recognition, weather APIs for real-time weather data, and integrates with Spotify for playlist recommendations. The system is built using Python (Flask), JavaScript, and popular machine learning libraries.

---

## Features

- **Real-Time Emotion Detection:** Uses your webcam to detect facial emotions.
- **Weather Integration:** Fetches current weather data for your location.
- **Personalized Music Recommendations:** Suggests Spotify playlists tailored to your emotion and weather.
- **Voice Feedback:** Plays a voice note corresponding to the detected emotion.
- **Interactive Web Interface:** User-friendly UI for seamless interaction.

---

## Directory Structure

```
Emotion and Weather-Based Music Recommender System Using Live Video Feed/
├── app.py                       # Main Flask application
├── emotion_detection.py         # Emotion detection logic
├── emotion_training.py          # Model training script (correct)
├── emtion_training.py           # (Typo, duplicate of above)
├── face_expression.py           # Face expression utilities
├── music_recommendation.py      # Music recommendation logic
├── weather_detection.py         # Weather data fetching logic
├── static/
│   ├── js/
│   │   └── script.js            # Frontend JS for webcam, audio, and UI
│   └── css/
│       └── style.css            # (If present) Styles
├── templates/
│   └── index.html               # Main HTML template
├── tests/
│   ├── functional_testing.py    # Selenium-based functional tests
│   └── image_to_base64.py       # Utility for image encoding
├── train_dataset.csv            # Training data (images/labels)
├── test_dataset.csv             # Test data (images/labels)
├── emotiondetector.h5           # Trained model weights
├── emotiondetector.json         # Trained model architecture
├── requirments.txt              # Python dependencies
├── CSVgeneration.ipynb          # Notebook for dataset CSV generation
├── emotion_training.ipynb       # Notebook for model training
├── unit_testing.py              # (If present) Unit tests
└── ...
```

---

## Setup Instructions

### 1. Clone the Repository

```sh
git clone <repo-url>
cd "Emotion and Weather-Based Music Recommender System Using Live Video Feed"
```

### 2. Install Dependencies

Create a virtual environment (recommended):

```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install required packages:

```sh
pip install -r requirments.txt
```

### 3. Download/Prepare Model

- The trained model files (`emotiondetector.h5`, `emotiondetector.json`) should be present in the root directory.
- If you want to retrain the model, use `emotion_training.py` or the provided Jupyter notebook.

### 4. Run the Application

```sh
python app.py
```

- The app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## Usage

1. Open the web app in your browser.
2. Allow camera access when prompted.
3. Click **Get Recommendation**.
4. The app will:
    - Capture frames from your webcam.
    - Detect your emotion.
    - Fetch current weather.
    - Recommend Spotify playlists.
    - Play a voice note for your emotion.

---

## File Descriptions

- [`app.py`](app.py): Flask server, routes, and integration logic.
- [`emotion_detection.py`](emotion_detection.py): Loads the model, processes images, predicts emotions.
- [`music_recommendation.py`](music_recommendation.py): Maps emotion/weather to Spotify playlists.
- [`weather_detection.py`](weather_detection.py): Fetches weather data using an API.
- [`static/js/script.js`](static/js/script.js): Handles webcam, frame capture, AJAX, and audio playback.
- [`templates/index.html`](templates/index.html): Main web interface.
- [`emotion_training.py`](emotion_training.py): Model training script.
- [`CSVgeneration.ipynb`](CSVgeneration.ipynb): Generates CSVs for training/testing.
- [`tests/functional_testing.py`](tests/functional_testing.py): Selenium-based UI tests.
- [`tests/image_to_base64.py`](tests/image_to_base64.py): Utility for converting images to base64 for testing.

---

## Testing

- **Unit Tests:** (If present) Run with:
  ```sh
  python -m unittest unit_testing.py
  ```
- **Functional Tests:** Requires ChromeDriver and Selenium:
  ```sh
  python tests/functional_testing.py
  ```

---

## Notes

- Make sure your webcam is connected and accessible.
- For Spotify integration, you may need to update playlist IDs in [`music_recommendation.py`](music_recommendation.py).
- The `static/audio/` directory should contain voice notes named after each emotion (e.g., `happy.mp3`).

---

## Requirements

See [`requirments.txt`](requirments.txt) for all dependencies. Main libraries include:
- Flask
- TensorFlow / Keras
- OpenCV
- Pandas, NumPy
- Selenium (for testing)

---

## License

This project is for educational purposes.

---

## Authors

- Kishore Tadepalli — [@Kishore-15072004](https://github.com/Kishore-15072004)
- Srinithya Reddy Yelti — [Nithya-Reddy01](https://github.com/Nithya-Reddy01)
- Vanja Abhilash Reddy
- T Narendra

---

##
