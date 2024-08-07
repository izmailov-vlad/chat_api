from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from db.engine import AsyncSessionLocal
from db.models.task import Task
from dependencies import get_db
from schemas.tasks import TaskRequestSchema


class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    async def add_task(self, task: TaskRequestSchema) -> Task:
        task_dict = task.model_dump()
        task = Task(**task_dict)
        self.db.add(task)
        self.db.flush()
        self.db.commit()
        return task

    # async def edit_task(self, task: TaskRequestSchema, task_id: str) -> Task:
    #     task_dict = task.model_dump()
    #     task = Task(**task_dict)
    #     task_db = self.db.execute(select(Task).where(Task.id == task_id))
    #     task_db.scalar_one_or_none()

    async def get_tasks(self) -> List[Task]:
        query = select(Task)
        result = self.db.execute(query)
        task_models = result.scalars().all()
        return list(task_models)
