import unittest

from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detector(self):
        # test data with sentences and their expected output emotion
        test_data = [
            ['I am glad this happened', 'joy'],
            ['I am really mad about this', 'anger'],
            ['I feel disgusted just hearing about this', 'disgust'],
            ['I am so sad about this', 'sadness'],
            ['I am really afraid that this will happen', 'fear']
        ]

        for test_case in test_data:
            input_sentence = test_case[0]
            expected = test_case[1]
            actual = emotion_detector(input_sentence)['dominant_emotion']
            # check if the generated output is correct by comparing it to the expected output
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
