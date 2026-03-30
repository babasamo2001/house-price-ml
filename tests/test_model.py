import os


def test_pipeline_exists():
    model_path = os.path.join("models", "pipeline.pkl")

    assert os.path.exists(model_path), f"Pipeline file not found at {model_path}"