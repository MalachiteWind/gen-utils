from tabulate import tabulate
from functools import wraps
from typing import Optional


def tabulatex(save_path: Optional[str] = None, *args, **kwargs):
    """
    Save tabular tables as tex documents.
    """
    if save_path:
        ...

    @wraps(tabulate)
    def tabulate_table(*args,**kwargs):
        return tabulate(*args, **kwargs)
    
    tabulatex.__doc__ = (tabulate.__doc__ ) + "\n" + (tabulatex.__doc__)
    return  tabulate_table(*args, **kwargs)

