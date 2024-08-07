from typing import Optional

from pydantic import BaseModel


class TaskResponseSchema(BaseModel):
    title: str
    description: Optional[str] = None
