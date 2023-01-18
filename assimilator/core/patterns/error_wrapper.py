from functools import wraps
from typing import Dict, Type, Optional, Callable


class ErrorWrapper:
    def __init__(
        self,
        error_mappings: Dict[Type[Exception], Type[Exception]] = None,
        default_error: Optional[Type[Exception]] = None,
    ):
        self.error_mappings = error_mappings or {}
        self.default_error = default_error

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is None:
            return

        wrapped_error = self.error_mappings.get(exc_type)

        if wrapped_error is not None:
            raise wrapped_error(exc_val)
        elif self.default_error is not None:
            raise self.default_error(exc_val)

        raise exc_val   # No wrapping error was found

    def decorate(self, func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs):
            with self:
                return func(*args, **kwargs)

        return wrapper


__all__ = ['ErrorWrapper']
