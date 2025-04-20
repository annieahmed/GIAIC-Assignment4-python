def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True
    return False

def main():
    n = int(input("Enter a number: "))
    low = int(input("Enter the low value: "))
    high = int(input("Enter the high value: "))
    
    if in_range(n, low, high):
        print(f"{n} is within the range {low} to {high}.")
    else:
        print(f"{n} is NOT within the range {low} to {high}.")

if __name__ == '__main__':
    main()
