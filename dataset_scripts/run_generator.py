import os
import sys

# Add root directory to PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from generator.content_generator import KPSSContentPipeline

if __name__ == "__main__":
    pipeline = KPSSContentPipeline()
    input_file = os.path.join("inputs", "yazim_kurallari.txt")
    output_file = pipeline.run_pipeline_from_file(input_file)
    print(f"Çıktı Kontrol Ediliyor: {output_file}")
