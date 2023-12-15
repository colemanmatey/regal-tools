"""
Logger
"""

import logging
import threading
from pathlib import Path


class Logger:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Logger, cls).__new__(cls)
                cls._instance.log_level = logging.DEBUG
                cls._instance.logger = cls._instance._create_logger()
            return cls._instance
          
    def _create_logger(self):
        # Create logger
        logger = logging.getLogger(__name__)
        logger.setLevel(self.log_level)

        # Add a file handler if one does not exist
        if not self._get_file_handlers(logger):
            path = self._get_or_create_path('logs/app.log')
            file_handler = logging.FileHandler(filename=path, mode='a')
            file_handler.setLevel(self.log_level)

            # Create a formatter for handlers
            formatter = logging.Formatter('%(asctime)s [%(levelname)s] [%(module)s:%(lineno)d] - %(message)s')
            file_handler.setFormatter(formatter)

            # Add handlers to the logger
            logger.addHandler(file_handler)

        return logger
    
    @staticmethod
    def _get_file_handlers(logger):
        return [handler for handler in logger.handlers if isinstance(handler, logging.FileHandler)]
    
    @staticmethod
    def _get_or_create_path(filename):
        base_dir = Path(__file__).resolve().parent.parent.parent
        path = base_dir / filename

        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch(exist_ok=True)

        return path
