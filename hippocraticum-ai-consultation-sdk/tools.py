def safe_call(fn):
    """Decorator for safe API calls with error handling"""
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            raise e
            # raise translate(e) from e #TODO add right exc handling
    return wrapper


def safe_call_async(fn):
    """Decorator for safe async API calls with error handling"""
    async def wrapper(*args, **kwargs):
        try:
            return await fn(*args, **kwargs)
        except Exception as e:
            raise e
            # raise translate(e) from e #TODO add right exc handling
    return wrapper
