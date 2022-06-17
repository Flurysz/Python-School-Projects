#!/usr/bin/env python3

def log_and_count(*args, **kwargs):
    def decorator(func):
        def inner(*args_2, **kwargs_2):
            if "key" in kwargs:
                kwargs["counts"][kwargs["key"]] += 1
            elif args:
                kwargs["counts"][list(args)[0]] += 1
            else:
                kwargs["counts"][func.__name__] += 1
            print("called {0} with {1} and {2}".format(func.__name__, args_2, kwargs_2))
        return inner
    return decorator