import logging
import functools
import time

def log_action(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        finish_time = time.time()
        process_time = (finish_time - start_time) * 1000
        logging.info(f"[ДІЯ] {func.__name__} | {args} | {process_time:.2f} ms")
        return result
    

    return wrapper

def validate_price(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        price = args[2]

        if isinstance(price,(int, float)) and price >= 0:
            result = func(*args, **kwargs)
            return result
        else:
            logging.warning(f"validate_price: price must be >= 0, got {price}")
            return None

    return wrapper

def notify_client(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.debug(
            f"[notify_client] Сповіщення клієнта після "
            f"{func.__name__}: ще не реалізовано (Заняття 25)"
        )
        return result
    return wrapper
