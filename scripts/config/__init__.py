import os
import pathlib
import shutil
import sys
from typing import Annotated, Any, Optional
from urllib.parse import urlparse

from dotenv import load_dotenv
from pydantic.functional_validators import BeforeValidator
from pydantic.v1 import BaseSettings, Field, root_validator

load_dotenv()

PROJECT_NAME = "Mini-Event-Management-services"


class _Service(BaseSettings):
    MODULE_NAME: str = Field(default="event-management-services")
    HOST: str = Field(default="0.0.0.0", env="service_host")
    PORT: int = Field(default=8000, env="service_port")
    WORKERS: int = Field(default=1)
    ENABLE_CORS: bool = True
    CORS_URLS: str = Field(default="")
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: list[str] = ["GET", "POST", "DELETE", "PUT"]
    CORS_ALLOW_HEADERS: list[str] = ["*"]
    LOG_LEVEL: str = "DEBUG"
    ENABLE_FILE_LOG: Optional[Any] = False
    ENABLE_CONSOLE_LOG: Optional[Any] = True

    @root_validator(allow_reuse=True)
    def validate_values(cls, values):
        values["LOG_LEVEL"] = values["LOG_LEVEL"] or "INFO"
        print(f"Logging Level set to: {values['LOG_LEVEL']}")
        return values


class _Databases(BaseSettings):
    POSTGRES_URI: Optional[str]
    PG_REMOVE_PREFIX: bool = False
    PG_POOL_SIZE: str = Field(default="20")
    PG_MAX_OVERFLOW: str = Field(default="10")

    @root_validator(allow_reuse=True)
    def validate_values(cls, values):
        if not values["POSTGRES_URI"]:
            print("Environment variable POSTGRES_URI not set, proceeding without Postgres Support")
            sys.exit(1)
        return values

class _PathToStorage(BaseSettings):
    BASE_PATH: pathlib.Path = Field(None, env="BASE_PATH")
    MOUNT_DIR: pathlib.Path = Field(default="workflow-management", env="MOUNT_DIR")
    LOGS_MODULE_PATH: Optional[pathlib.Path]

    @root_validator(allow_reuse=True)
    def assign_values(cls, values):
        values["LOGS_MODULE_PATH"] = os.path.join(values.get("BASE_PATH"), "logs", values.get("MOUNT_DIR"))
        return values

    @root_validator(allow_reuse=True)
    def validate_values(cls, values):
        if not values["BASE_PATH"]:
            print("Error, environment variable BASE_PATH not set")
            sys.exit(1)
        if not values["MOUNT_DIR"]:
            print("Error, environment variable MOUNT_DIR not set")
            sys.exit(1)
        return values


Service = _Service()
DBConf = _Databases()
PathToStorage = _PathToStorage()



__all__ = [
    "PROJECT_NAME",
    "Service",
    "DBConf",
    "PathToStorage",
]
