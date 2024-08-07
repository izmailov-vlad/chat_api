from typing import List
from pydantic import BaseModel

from schemas.tasks.response.task_response_schema import TaskResponseSchema


class TasksResponseSchema(BaseModel):
    tasks: List[TaskResponseSchema]
