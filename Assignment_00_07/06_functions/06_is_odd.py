def main():
    for i in range(10, 20):  # 10 se 19 tak
        if is_odd(i):
            print(i, 'odd', end=' ')
        else:
            print(i, 'even', end=' ')
            
def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns true.
    """
    return value % 2 == 1

if __name__ == '__main__':
    main()
