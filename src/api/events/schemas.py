from pydantic import BaseModel, Field, field_validator
from datetime import datetime, time
from typing import Optional
from uuid import UUID, uuid4


class EventResponseSchema(BaseModel):
    id:int
    title:str
    description:str
    date_: datetime = Field(default_factory=datetime.now)
    time_: time = Field(default_factory=lambda: datetime.now().time())
    location:str
    isvirtual:bool = Field(default=False)
    capacity:int = Field(default=0, ge=0)
    tags:list[str] = Field(default_factory=list)

    @field_validator("tags")
    @classmethod
    def clean_tags(cls, v:list[str]) -> list[str]:
        return list(set(tag.lower().strip() for tag in v))

class EventCreateModel(BaseModel):
    id:int = Field(default=0)
    title:str
    description:str
    location:str
    isvirtual:bool = Field(default=False)
    capacity:int = Field(default=0, ge=0)
    tags:list[str] = Field(default_factory=list)

class EventUpdateModel(BaseModel):
    title:Optional[str] = None
    description:Optional[str] = None
    location:Optional[str] = None
    isvirtual:Optional[bool] = Field(default=False)
    capacity:Optional[int] = Field(default=0, ge=0)
    tags:Optional[list[str]] = Field(default_factory=list)

