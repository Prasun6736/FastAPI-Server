from pydantic_settings import BaseSettings , SettingsConfigDict

class Settings(BaseSettings):
    DB_URL:str
    model_config=SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

Config=Settings() 
## This is a object for settings class
