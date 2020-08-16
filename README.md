# Feature Change

``` python
from feature_change import change

def log_diff(**kwargs):
    # This will be called if the results of
    # `new_function` and `current_function` differ

def log_call(**kwargs):
    # This will be called on every call to `current_function`

def new_function():
    # This is a new function we want to check if
    # it *really* behaves like the current

@change(new=new_function, on_diff=log_diff, on_call=log_call)
def current_function():
    # The current function. Just decorate it with `change` and everything
    # will work! No need to change the code!

```

A Python decorator that helps you run two different versions of a function at
the same time and track differences _without_ breaking the current behavior.

It is based on Auth0's [feature-change](https://github.com/dschenkelman/feature-change)
for Node.js. [Original article](https://auth0.com/blog/feature-changes-at-auth0/)

## Usage

1. Install with pip or your favorite package manager `pip install feature-change`

    a. If you can't or don't want to add a new dependency, feel free to just
       copy the current code from `change.py`. It is pretty straightforward.

2. Define the functions you want to be called. They will receive two keyword
   arguments `current` and `new`, with the current and the new result.

    ```python
    def log_diff(current, new):
        print(f"The current value is {current} but the new one is {new})
    ```

3. Decorate your current function with `@change`, passing the new implementation
   that you want to test and any logging function you have defined. Currently
   you can define logging on two occasions ― `on_diff` will be called if the
   results are different and `on_call` will always be called

    ```python
    @change(new=new_func, on_diff=log_diff)
    def current_function():
        ...
    ```

## Warnings

1. **Both functions will be called** ― be aware of side effects like database
   writes. If both functions writes to a database, they will both be executed,
   leading to possible inconsistencies.

2. **Be aware of slow logs** ― the callables you define for `on_diff` and `on_call`
   should not be very expensive. You could, by example, just counti how many times
   `on_diff` was called using some fast db like redis.

3. **Equality is simple** ― currently the results are checked using simply the
   `==` operator. Keep that in mind if your results are complex objects whose
   equality is not well defined. An optional argument for a custom equality
   checker will be add on the future.

## Other Libs

Auth0's `feature-change` is based on GitHub's [scientist](https://github.com/github/scientist).

`scientist` itself has a lot more features than this lib and it
also has implementations on [different languages](https://github.com/github/scientist#alternatives)
