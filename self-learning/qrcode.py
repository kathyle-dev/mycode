import qrcode
import validators


def confirmation(msg, thing):
    confirm = ""
    while confirm != "Y":
        answer = input(msg)
        confirm = input(f"You have put in {answer} as the {thing}. Continue? (Y/N) ").upper()
    return answer


def main():
    link = input("What link would you like to make into a qr code? ")
    valid = validators.url(link)
    if valid == "False":
        print("Invalid url. Try again.")
    else:
        img = qrcode.make(link)
        location = confirmation("Where would you like to save it? ", "location")
        name = confirmation("What would you like to name your qrcode? ", "name")
        img.save(f"{location}/{name}.png")
        print(f"Your qrcode has saved! Here's where it's located: {location}/{name}")


if __name__ == "__main__":
    main()
