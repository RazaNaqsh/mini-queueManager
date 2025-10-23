from fastapi import FastAPI
from pydantic import BaseModel
from .tasks import process_data_task
from .celery_app import celery_app

app = FastAPI()

class TaskRequest(BaseModel):
    text: str

@app.post("/task")
async def submit_task(req: TaskRequest):
    # send task to Celery asynchronously
    task = process_data_task.delay(req.text)
    return {"task_id": task.id}


@app.get("/result/{task_id}")
async def get_result(task_id: str):
    task_result = celery_app.AsyncResult(task_id)
    response = {
        "task_id": task_id,
        "status": task_result.status
    }
    if task_result.status == "SUCCESS":
        response["result"] = task_result.result
    elif task_result.status == "FAILURE":
        response["error"] = str(task_result.result)
    return response