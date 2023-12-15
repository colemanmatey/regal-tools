"""
Configuration Manager
"""

from pathlib import Path
from regal.logger import Logger


class ConfigManager:
    """A manager for configuring settings"""
    _instance = None

    def __new__(cls, filename=None):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance._filename = cls._instance._base_dir() / filename
            cls._instance.logger = Logger().logger
            cls._instance._env_vars = cls._instance._load_env_vars()
        return cls._instance

    def _load_env_vars(self):
        env_vars = dict()
        try:
            with open(self._filename, 'r') as file:
                for line in file:
                    key, value = line.strip().split("=")
                    env_vars[key] = value
        except (FileNotFoundError, ValueError) as e:
            self.logger.error(f'Error loading environment variables: {e}')
        else:
            self.logger.info("Environment variables loaded successfully!")
            return env_vars
    
    def _base_dir(self):
        return Path(__file__).resolve().parent.parent.parent
    
    def get_var(self, key, default=None):
        return self._instance._env_vars.get(key, default)
