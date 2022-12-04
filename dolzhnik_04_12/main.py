import functions

def main():
    print(functions.get_val({'hello': 'world'}, 'hello'))
    print(functions.get_val({'hello': 'world'}, 'hello', 'python'))
    print(functions.get_val({}, 'hello', 'python'))
    print()
    coll = {"a": {"b": {"c": 3}}}
    print(coll)
    print(functions.set_(coll, ['a', 'b', 'c'], 4))
    print(functions.set_(coll, ['x', 'y', 'z'], 5))

main()
