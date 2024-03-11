from typing import Optional
from pydantic import BaseModel

class Site(BaseModel):
  id: Optional[int] | None = None
  nome: str | None = None
  url: str | None = None
  objetivo: str | None = None