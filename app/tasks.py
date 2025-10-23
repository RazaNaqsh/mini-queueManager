from .celery_app import celery_app
import time, random

@celery_app.task(bind=True, max_retries=3, default_retry_delay=5)
def process_data_task(self, text: str):
    """Simulate a time-consuming and error-prone task"""
    try:
        print(f"Worker received: {text}")
        time.sleep(2)
        # Simulate random failure
        if random.random() < 0.7:
            raise ValueError("Random failure occurred!")
        return {"original": text, "upper": text.upper(), "length": len(text)}
    except Exception as exc:
        raise self.retry(exc=exc)
