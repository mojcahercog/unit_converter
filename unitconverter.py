name = "Mojca"

print("Hello {0}! Let's convert kilometres to miles!".format(name))
while True:
    km = input("Kilometres: ")
    km = float(km.replace(",", "."))
    mi = (km * 0.6)
    print("{0} kilometers equals {1} miles.".format(km, mi))
    print("Would you like to do another conversion?")
    choice = input("y/n ").strip().lower()
    if choice != "y":
        print("See you later!")
        break
