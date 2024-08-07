from typing import Optional

from pydantic import BaseModel


class TaskRequestSchema(BaseModel):
    title: str
    description: Optional[str] = None
