from pydantic import BaseModel, Field
import os

class Settings(BaseModel):
    debug: bool = Field(default=True)
    api_key: str = Field(default_factory=lambda: os.getenv("API_KEY", ""))

if __name__ == "__main__":
    s = Settings()
    print(s.model_dump())
