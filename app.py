from flask import Flask, render_template, request, jsonify
import base64
import cv2
import numpy as np
from collections import Counter
from emotion_detection import detect_emotion
from face_expression import analyze_expression
from weather_detection import get_weather
from music_recommendation import recommend_music
import mediapipe as mp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.json
        if 'images' not in data or not data['images']:
            raise ValueError("No image data received")

        images = [base64.b64decode(img.split(",")[1] if ',' in img else img) for img in data['images']]
        np_arrs = [np.frombuffer(img, np.uint8) for img in images]

        frames = [cv2.imdecode(np_arr, cv2.IMREAD_COLOR) for np_arr in np_arrs if np_arr.size > 0]
        frames = [frame for frame in frames if frame is not None]

        if not frames:
            raise ValueError("No valid frames received")

        # Detect emotions and expressions for all frames
        emotions = [detect_emotion(frame) for frame in frames]
        expressions = [analyze_facial_expression(frame) for frame in frames]

        # Select the most common emotion and expression
        most_common_emotion = Counter(emotions).most_common(1)[0][0]
        most_common_expression = Counter(expressions).most_common(1)[0][0]

        # Combine emotion and expression
        combined_emotion = combine_emotion_expression(most_common_emotion, most_common_expression)

        # Weather information
        weather_info = get_weather()

        # Recommend music based on combined emotion and weather
        recommended_music = recommend_music(combined_emotion, weather_info)

        return jsonify({
            'combined_emotion': combined_emotion,
            'weather': weather_info,
            'playlists': recommended_music
        })
    except ValueError as ve:
        app.logger.error(f"Value Error in recommend endpoint: {ve}")
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        app.logger.error(f"Error in recommend endpoint: {e}")
        return jsonify({'error': str(e)}), 500

def analyze_facial_expression(img):
    mp_face_mesh = mp.solutions.face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, min_detection_confidence=0.5)
    results = mp_face_mesh.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            height, width, _ = img.shape
            expression = analyze_expression(face_landmarks.landmark, width, height)
            return expression
    return "Neutral"

def combine_emotion_expression(emotion, expression):
    if (emotion == "happy" or emotion == "neutral") and expression == "Smiling":
        return "happy"
    elif emotion == "neutral" and expression == "Neutral":
        return "neutral"
    elif (emotion == "angry" or emotion == "neutral") and expression == "Angry":
        return "angry"
    elif emotion == "surprise" and expression == "Surprised":
        return "surprise"
    elif emotion == "sad" and expression == "Neutral":
        return "sad"
    elif emotion == "fear" and expression == "Surprised":
        return "fear"
    elif emotion == "disgust" and expression == "Disgusted":
        return "disgust"
    else:
        return emotion

if __name__ == "__main__":
    app.run(debug=True)
