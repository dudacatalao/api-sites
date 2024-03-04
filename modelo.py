from typing import Optional
from pydantic import BaseModel

class Site(BaseModel):
  id: Optional[int] = None
  nome: str
  url: str
  objetivo: str