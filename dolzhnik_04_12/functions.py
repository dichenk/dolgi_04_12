def get_val(collection = {}, key = 0, default = 'dadibdabdabda', *args):
    try:
        return collection[key]
    except:
        return default

def set_(x, y, z, *args):
    try:   
        for i in list(reversed(y)):
            z = {i: z}
        x[list(z.keys())[0]] = z[list(z.keys())[0]]
        return x
    except:
        return "Error"
