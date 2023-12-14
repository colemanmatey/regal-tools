"""
Configuration Manager
"""

from pathlib import Path

from regal.logger import Logger


class ConfigManager:
    """A manager for configuring settings"""
    _instance = None

    def __new__(cls, filename=None):
        if not cls._instance:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance._filename = cls._instance._base_dir() / filename

            # Initialize logger
            cls._instance.logger = Logger().get_logger()

            # Load environment variables
            cls._instance._env_vars = cls._instance._load_env_vars()

        return cls._instance

    def _load_env_vars(self):
        env_vars = dict()
        self.logger.debug("Loading environment variables from file.")
        try:
            with open(self._filename, 'r') as file:
                for line in file:
                    key, value = line.strip().split("=")
                    env_vars[key] = value
        except (FileNotFoundError, ValueError) as e:
            self.logger.exception(f'Error loading environment variables: {e}')
        else:
            self.logger.info("Environment variables loaded successfully!")
            return env_vars
    
    def _base_dir(self):
        return Path(__file__).resolve().parent.parent.parent
    
    def get_var(self, key, default=None):
        return self._instance._env_vars.get(key, default)
