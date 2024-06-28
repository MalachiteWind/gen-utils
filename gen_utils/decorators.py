import time

def add_clock(f):
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