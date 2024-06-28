import time
import numpy as np

def add_clock(f):
    """
    Decorator to print the name and time taken to compute a function.

    Example:
    --------
    >>> import time
    >>> from gen_util.decorators import add_clock

    >>> @add_clock
    >>> def f(x):
    ...     time.sleep(1)
    ...     return x

    >>> f(1)
    'apply f: [1.0000s]'
    1
    """

    def _remove_underscore(name):
        return name.replace('_',' ')

    def _rename_f_sting(f_name):
        if f_name.startswith('apply'):
            return _remove_underscore(f_name)
        return 'apply '+ _remove_underscore(f_name)
        
    def clocked_f(*args,**kwargs):
        f_name = _rename_f_sting(f.__name__)
        print(f_name+":", end='')
        t0 = time.perf_counter()
        result = f(*args,**kwargs)
        elapsed_time = time.perf_counter()-t0
        print("[%0.4fs]" % elapsed_time)
        return result
    
    return clocked_f

def mesh_func(f):
    """
    vectorize a function in a stupid way.
    """
    def _np_or_list(var):
        if isinstance(var,np.ndarray) or isinstance(var,list):
            return True
        return False
    
    def _shape(arg):
        if _np_or_list(arg):
            return len(arg)
        return 1

    def _mesh_f_shape(*args):
        return tuple([_shape(arg_i) for arg_i in args])

    def _mesh_f(*args):
        mesh_args = np.meshgrid(*args)
        mesh_args = [arr.reshape(-1) for arr in mesh_args]
        
        sol = []
        for arg_i in zip(*mesh_args):
            sol.append(f(*arg_i))
        return np.array(sol).reshape(_mesh_f_shape(*args))
    
    def wrapper(*args):
        elements = [_np_or_list(arg) for arg in args]
        if True in elements:
            return _mesh_f(*args)
        return f(*args)
    
    return wrapper