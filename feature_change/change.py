"""
Module for the main change decorator
"""
from functools import wraps


def change(new, on_diff=None, on_call=None):
    """
    Returns a decorator that will compare the result of a function
    with the result of `new` and call `log` with the results.u
    """

    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_result = func(*args, **kwargs)
            new_result = new(*args, **kwargs)

            payload = {"current": current_result, "new": new_result}

            if on_diff and current_result != new_result:
                on_diff(**payload)

            if on_call:
                on_call(**payload)

            return current_result

        return wrapper

    return decorate
