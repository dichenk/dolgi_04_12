import functions

def main():
    print(functions.get_val({'hello': 'world'}, 'hello'))
    print(functions.get_val({'hello': 'world'}, 'hello', 'python'))
    print(functions.get_val({}, 'hello', 'python'))

main()
