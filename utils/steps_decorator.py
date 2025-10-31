import functools
import logging
from typing import Callable, TypeVar, Any


logger = logging.getLogger(__name__)

F = TypeVar("F", bound=Callable[..., Any])


def step(name: str) -> Callable[[F], F]:
    """
    Step decorator:
    - Logs start/finish of each step
    - Wraps with allure.step if allure is available
    """

    def decorator(func: F) -> F:
        wrapped = func
        try:
            # Integration with allure if installed
            import allure  # type: ignore

            @functools.wraps(func)
            def with_allure(*args: Any, **kwargs: Any) -> Any:
                logger.info(f"STEP: {name}")
                with allure.step(name):
                    result = func(*args, **kwargs)
                logger.info(f"DONE: {name}")
                return result

            wrapped = with_allure  # type: ignore
        except Exception:
            # Fallback to standard logging
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


