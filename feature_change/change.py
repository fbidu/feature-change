from functools import wraps


def change(func, *, new, log):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_result = func(*args, **kwargs)
            new_result = new(*args, **kwargs)
            log(f"current = {current_result}, new = {new_result}")
            return current_result

        return wrapper

    return decorate


# class change:
#     def __init__(self, wrapped, *, new, log=None) -> None:
#         self.wrapped = wrapped
#         self.log = log
#         self.new = new

#     def __call__(self, *args, **kwargs):
#         self.new()
#         self.log()
#         return self.wrapped(*args, **kwargs)
