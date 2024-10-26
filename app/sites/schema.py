from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


# Схемы для таблицы `sites`
class SiteBase(BaseModel):
    name: str

class SiteCreate(SiteBase):
    pass

class Site(SiteBase):
    smi_id: int

    class Config:
        orm_mode = True
