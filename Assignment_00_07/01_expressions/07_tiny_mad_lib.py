SENTENCE_START: str = "Panaversity is fun. I learned to program and used python to make my"

def main():
    adjective: str = input("Please type an adjective and pree enter.")
    noun: str = input("Please type a noun and press enter.")
    verb: str = input("Please type a verb and press enter.")

    print(SENTENCE_START + adjective + " " + noun + " " +verb + "!")

if __name__ == '__main__':
    main()