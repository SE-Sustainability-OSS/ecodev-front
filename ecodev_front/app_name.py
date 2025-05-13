from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class AppNameConf(BaseSettings):
    """
    Simple authentication configuration class
    """
    app_name: str = ''
    model_config = SettingsConfigDict(env_file='.env')


APP_NAME = AppNameConf().app_name
