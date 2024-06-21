from pydantic import BaseModel
from pathlib import Path


class Config(BaseModel):
    random_seed: int
