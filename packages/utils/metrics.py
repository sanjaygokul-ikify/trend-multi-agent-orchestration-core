import time
from .logging import configure_logging

class Metrics:
    def __init__(self) -> None:
        self.start_time = time.time()
    
    def get_elapsed_time(self) -> float:
        return time.time() - self.start_time

    def log_metrics(self) -> None:
        configure_logging()
        logging.info(f'Elapsed time: {self.get_elapsed_time()} seconds')