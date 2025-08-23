def safe_call(fn):
    """Decorator for safe API calls with error handling"""
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            raise e
            # raise translate(e) from e #TODO add right exc handling
    return wrapper
