def get_val(*args, collection = {}, key = 0, default = 'dadibdabdabda'):
    try:
        return collection[key]
    except:
        return default
