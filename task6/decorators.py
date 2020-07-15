import inspect
from server_logger import LOG


def log(f):
    def wrapper(*args):
        f(*args)
        LOG.info(f'Отработала фуккция {f.__name__} with {args} called by {inspect.stack()[1][3]}')

    return wrapper
