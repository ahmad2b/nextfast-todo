from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "Fast TODO API"

    class ConfigDict:
        env_file = ".env"
