import unittest
from emotion_detection import preprocess_image, detect_emotion
import numpy as np
import cv2

class TestEmotionDetection(unittest.TestCase):
    
    def setUp(self):
        # Create a dummy image for testing
        self.image = np.zeros((48, 48), dtype=np.uint8)
    
    def test_preprocess_image(self):
        processed_image = preprocess_image(self.image)
        self.assertEqual(processed_image.shape, (1, 48, 48, 1))

    def test_detect_emotion(self):
        # Load a test image
        test_image_path = 'tests/test_image.jpg'
        image = cv2.imread(test_image_path)
        emotion = detect_emotion(image)
        self.assertIn(emotion, ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise'])

if __name__ == '__main__':
    unittest.main()
