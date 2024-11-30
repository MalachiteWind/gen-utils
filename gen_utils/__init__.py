import inspect

def _get_default_args(func):
    """
    return dict of default args values of a function
    """
    signature = inspect.signature(func)
    return {
        k: v.default
        for k, v in signature.parameters.items()
        if v.default is not inspect.Parameter.empty
    }