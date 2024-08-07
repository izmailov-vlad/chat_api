from typing import List

from sqlalchemy.orm import Session

from repositories.task_repository import TaskRepository
from schemas.tasks import TaskRequestSchema
from schemas.tasks.response.task_response_schema import TaskResponseSchema


class TaskService:
    def __init__(self, db: Session) -> None:
        self.repository = TaskRepository(db)

    async def get_tasks(self) -> List[TaskResponseSchema]:
        tasks_entity = await self.repository.get_tasks()
        tasks_dto = list(
            map(lambda task: TaskResponseSchema(title=task.title, description=task.description), tasks_entity)
        )
        return tasks_dto

    async def add_task(self, task: TaskRequestSchema) -> TaskResponseSchema:
        task_entity = await self.repository.add_task(task)
        return TaskResponseSchema(
            title=task_entity.title,
            description=task_entity.description
        )
