import cv2
import numpy as np
from tensorflow.keras.models import model_from_json
from collections import Counter
import mediapipe as mp

# Load the emotion detection model
def load_model():
    json_file = open("models/emotiondetector.json", "r")
    model_json = json_file.read()
    json_file.close()
    model = model_from_json(model_json)
    model.load_weights("models/emotiondetector.h5")
    return model

model = load_model()

# Load the Haar cascade for face detection
haar_file = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_file)

def preprocess_image(image):
    """
    Preprocess the image for emotion detection model.
    :param image: Grayscale image of a face
    :return: Preprocessed image ready for the model input
    """
    image = cv2.resize(image, (48, 48))  # Resize to 48x48 pixels
    image = image.astype('float32') / 255  # Normalize to [0, 1]
    image = np.expand_dims(image, axis=-1)  # Expand dims for channel
    image = np.expand_dims(image, axis=0)  # Expand dims for batch
    return image

def detect_emotion(frame):
    """
    Detect emotion from the input frame.
    :param frame: Input frame from the video feed
    :return: Most common detected emotion
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # Detect faces
    emotion_list = []  # List to store detected emotions
    labels = {0: 'angry', 1: 'disgust', 2: 'fear', 3: 'happy', 4: 'neutral', 5: 'sad', 6: 'surprise'}

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]  # Extract face region
        face = preprocess_image(face)  # Preprocess face
        prediction = model.predict(face)  # Predict emotion
        emotion_label = labels[np.argmax(prediction)]  # Get emotion label
        emotion_list.append(emotion_label)  # Append to emotion list

    # Determine the most common emotion if any faces are detected
    if emotion_list:
        most_common_emotion = Counter(emotion_list).most_common(1)[0][0]
    else:
        most_common_emotion = 'neutral'  # Default to 'neutral' if no faces

    return most_common_emotion

def analyze_facial_expression(img):
    mp_face_mesh = mp.solutions.face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, min_detection_confidence=0.5)
    results = mp_face_mesh.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            height, width, _ = img.shape
            expression = analyze_expression(face_landmarks.landmark, width, height)
            return expression
    return "Neutral"

def analyze_expression(landmarks, width, height):
    # Extract key points for expression detection
    left_eye_inner = landmarks[133]  # Inner corner of left eye
    right_eye_inner = landmarks[362]  # Inner corner of right eye
    mouth_left = landmarks[61]  # Left corner of mouth
    mouth_right = landmarks[291]  # Right corner of mouth
    upper_lip = landmarks[13]  # Upper lip center
    lower_lip = landmarks[14]  # Lower lip center

    # Convert normalized coordinates to pixel coordinates
    def denormalize(point):
        return int(point.x * width), int(point.y * height)

    left_eye = denormalize(left_eye_inner)
    right_eye = denormalize(right_eye_inner)
    mouth_left = denormalize(mouth_left)
    mouth_right = denormalize(mouth_right)
    upper_lip = denormalize(upper_lip)
    lower_lip = denormalize(lower_lip)

    # Calculate distances
    eye_distance = calculate_distance(left_eye, right_eye)
    mouth_width = calculate_distance(mouth_left, mouth_right)
    mouth_height = calculate_distance(upper_lip, lower_lip)

    # Detect expressions based on distances
    if mouth_height / mouth_width > 0.5:
        return "Surprised"
    elif mouth_width / eye_distance > 1.8:
        return "Smiling"
    elif mouth_height / mouth_width < 0.15 and mouth_width / eye_distance < 1.5:
        return "Neutral"
    else:
        return "Angry"

def calculate_distance(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))

# Example usage for testing
if __name__ == "__main__":
    cap = cv2.VideoCapture(0)  # Open webcam

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        emotion = detect_emotion(frame)  # Detect emotion
        expression = analyze_facial_expression(frame)  # Analyze facial expression
        combined_emotion = f'{emotion} ({expression})'  # Combine emotion and expression
        cv2.putText(frame, f'Emotion: {combined_emotion}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Emotion and Expression Detection', frame)
        
        # Break loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
