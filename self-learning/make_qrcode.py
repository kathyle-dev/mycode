import qrcode
import validators


def confirmation(msg, thing):
    confirm = ""
    answer = ""
    while confirm != "Y":
        answer = input(msg)
        confirm = input(f"You have put in {answer} as the {thing}. Continue? (Y/N) ").upper()
    return answer


def main():
    count = 0
    link = ""
    valid = ""
    while not valid:
        if count > 0:
            print("Invalid url. Try again.")

        link = input("What link would you like to make into a qr code? ")
        valid = validators.url(link)
        count += 1

    img = qrcode.make(link)
    location = confirmation("Where would you like to save it? ", "location")
    name = confirmation("What would you like to name your qrcode? ", "name")
    img.save(f"{location}/{name}.png")
    print(f"Your qrcode has saved! ")


if __name__ == "__main__":
    main()
