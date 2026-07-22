"""Main pipeline for video dubbing."""
import logging
from src.modules.audio import AudioProcessor
from src.modules.video import VideoProcessor
from src.modules.translate import Translator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DubbingPipeline:
    def __init__(self, target_language: str):
        self.audio = AudioProcessor()
        self.video = VideoProcessor()
        self.translator = Translator(target_language)
        
    def run(self, video_path: str, output_path: str):
        """Runs the dubbing pipeline."""
        logger.info(f"Starting dubbing pipeline for {video_path}")
        try:
            # Pipeline steps
            self.audio.extract_audio(video_path, "temp_audio.wav")
            # Translation and TTS would happen here
            self.audio.merge_audio(video_path, "temp_audio_translated.wav", output_path)
            logger.info("Pipeline completed successfully")
        except Exception as e:
            logger.error(f"Pipeline failed: {e}")
            raise

if __name__ == "__main__":
    pipeline = DubbingPipeline(target_language="es")
    pipeline.run("input.mp4", "output.mp4")
