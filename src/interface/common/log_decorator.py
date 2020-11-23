from src.common.log import logger


class LogDecorator:
    def __call__(self, func):
        def wrapped_function(*args, **kwargs):
            if func.__doc__:
                desc = func.__doc__
            else:
                desc = func.__name__
            log_string = "【{}】开始执行".format(desc)
            print(log_string)
            logger.info(log_string)
            return func(*args, **kwargs)

        return wrapped_function
