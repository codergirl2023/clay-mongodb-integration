from pydantic_settings import BaseSettings

__all__ = ("api_settings", "mongo_settings")

# It's good practice to use different Config classes for different settings.
class BaseAPISettings(BaseSettings):
    class Config:
        env_file = ".env.api"
        env_prefix = "API_"

class BaseMongoSettings(BaseSettings):
    class Config:
        env_file = ".env.mongo"
        env_prefix = "MONGO_"


# Then define your settings classes
class APISettings(BaseAPISettings):
    title: str
    host: str
    port: int
    log_level: str


class MongoSettings(BaseMongoSettings):
    uri: str
    database: str
    collection: str


api_settings = APISettings()
mongo_settings = MongoSettings()

print(api_settings.dict())
print(mongo_settings.dict())
