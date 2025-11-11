from loguru import logger


def log_request(method: str, path: str) -> None:
    """Log incoming requests."""
    logger.info("Request: {method} {path}", method=method, path=path)


def log_error(error: str, method: str, path: str) -> None:
    """Log errors during request processing."""
    logger.error("Error in {method} {path}: {error}", method=method, path=path, error=error)
