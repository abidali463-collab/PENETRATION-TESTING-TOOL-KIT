from banner import show_banner
from website_checker import check_website
from port_scanner import scan_ports

show_banner()

while True:

    print("\n1. Website Checker")
    print("2. Port Scanner")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        check_website()

    elif choice == "2":
        scan_ports()

    elif choice == "3":
        print("Goodbye")
        break

    else:
        print("Invalid option")