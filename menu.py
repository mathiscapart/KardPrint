import json
import requests

url_printer = "http://127.0.0.1:8081/v1/printer"
url_print = "http://127.0.0.1:8081/v1/printer/print"


def request(url):
    rep = requests.get(url)
    if rep.status_code == 200:
        data = rep.json()
        return data
    else:
        return None


def post(url):
    rep = requests.post(url)
    if rep.status_code == 200:
        data = rep.json()
        return data
    else:
        data = rep.json()
        return data


def menu():
    values = 0
    while values != 3:
        print(" __________ \n|   MENU   |\n")
        print(
            "1. Get Printer \n2. Add to a spooler and print\n3. Print a card \n4. Quitter le menu \n\n")
        values = int(input("Rentrer votre choix : "))
        match values:
            case 1:
                rep = request(url_printer)
                if rep is None:
                    print(f'\n{rep}')
                else:
                    print(f'\n{rep}')
            case 2:
                id_edit = str(input("Enter la carte : "))
                url_student_id = url_print + f"/{id_edit}"
                rep = post(url_student_id)
                if rep is None:
                    print(f'\n{rep}')
                else:
                    print(f'\n{rep}')
            case 3:
                rep = post(url_student_id)
                if rep is None:
                    print(f'\n{rep}')
                else:
                    print(f'\n{rep}')
            case 4:
                break


menu()
