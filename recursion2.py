def apply(lst, func, filter_func):
    return [func(ele) for ele in lst if filter_func(ele)]


