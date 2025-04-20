def main():

    fahrenhiet = float(input("\033[1;3m Enter temperature in fehrenhiet: \033[0m"))
                       
    celsius = (fahrenhiet - 32) + 5.0/9.0

    print(f"temprature : {fahrenhiet}F = {celsius}C")

if __name__ == "__main__":
     main()