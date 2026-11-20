import logging
import sys
from app.core.constants import LOG_DIR, LOG_FILE, LOG_FORMAT, DATE_FORMAT, LOG_LEVEL


def _build_logger(name: str = "chatbot") -> logging.Logger:
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    _logger = logging.getLogger(name)
    _logger.setLevel(LOG_LEVEL)

    # Avoid adding duplicate handlers on reload (e.g. uvicorn --reload)
    if _logger.handlers:
        return _logger

    formatter = logging.Formatter(fmt=LOG_FORMAT, datefmt=DATE_FORMAT)

    # Console handler — INFO and above
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # File handler — DEBUG and above (full trace)
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    _logger.addHandler(console_handler)
    _logger.addHandler(file_handler)

    return _logger


logger = _build_logger()