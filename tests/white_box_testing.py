import unittest
from emotion_training import model

class TestModelArchitecture(unittest.TestCase):
    
    def test_model_layers(self):
        self.assertEqual(len(model.layers), 10, "Model should have 10 layers")
        self.assertEqual(model.layers[0].input_shape, (None, 48, 48, 1), "Input shape should be (48, 48, 1)")

if __name__ == '__main__':
    unittest.main()
