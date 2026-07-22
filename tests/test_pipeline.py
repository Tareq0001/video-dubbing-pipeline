import unittest
from src.pipeline import DubbingPipeline

class TestDubbingPipeline(unittest.TestCase):
    def setUp(self):
        self.pipeline = DubbingPipeline("es")
        
    def test_pipeline_initialization(self):
        self.assertIsNotNone(self.pipeline.audio)
        self.assertIsNotNone(self.pipeline.video)
        self.assertEqual(self.pipeline.translator.target_language, "es")

if __name__ == "__main__":
    unittest.main()
