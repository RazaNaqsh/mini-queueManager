from .celery_app import celery_app
import time

@celery_app.task(bind=True)
def process_data_task(self, text: str):
    """Simulate a time-consuming task"""
    print(f"Worker received: {text}")
    time.sleep(10)  # simulate work
    return {"original": text, "upper": text.upper(), "length": len(text)}
