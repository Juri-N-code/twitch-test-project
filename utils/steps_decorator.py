import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)


def step(name: str) -> Callable:
    """
    Step decorator:
    - Logs start/finish of each step
    """

    def decorator(func):
        wrapped = func

        @functools.wraps(func)
        def with_logging(*args: Any, **kwargs: Any) -> Any:
            logger.info(f"STEP: {name}")
            try:
                return func(*args, **kwargs)
            finally:
                logger.info(f"DONE: {name}")

        wrapped = with_logging  # type: ignore

        return wrapped  # type: ignore

    return decorator
