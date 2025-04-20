Days_Per_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOURS: int = 60
SEC_PER_MIN: int = 60

def main():

    print("There are " + str(Days_Per_YEAR * HOURS_PER_DAY * MIN_PER_HOURS * SEC_PER_MIN) + "second in a year!")

if __name__ == "__main__":
    main()
