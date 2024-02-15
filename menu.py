import json
import requests

url_printer = "http://127.0.0.1:8081/v1/printer"
url_print_spooler = "http://127.0.0.1:8081/v1/printer/print"
url_print_ink = "http://127.0.0.1:8081/v1/printer/ink"
url_spooler = "http://127.0.0.1:8081/v1/printer/spooler"
url_spooler_first = "http://127.0.0.1:8081/v1/printer/spooler/first"
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
        return {
            "error": "Erreur de réponse"
        }


def menu():
    values = 0
    while values != 7:
        print(" __________ \n|   MENU   |\n")
        print(
            "1. Get Printer \n2. Add to a spooler and print\n3. Print a card \n4. Add to spooler \n5. Get first card "
            "in spooler \n6. Print Ink Level \n"
            "7. Quitter le menu \n\n")
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
                url_student_id = url_print_spooler + f"/{id_edit}"
                rep = post(url_student_id)
                if rep is None:
                    print(f'\n{rep}')
                else:
                    print(f'\n{rep}')
            case 3:
                rep = post(url_print)
                if rep is None:
                    print(f'\n{rep}')
                else:
                    print(f'\n{rep}')
            case 4:
                id_edit = str(input("Enter la carte : "))
                url_student_id = url_spooler + f"/{id_edit}"
                rep = post(url_student_id)
                if rep is None:
                    print(f'\n{rep}')
                else:
                    print(f'\n{rep}')
            case 5:
                rep = request(url_spooler_first)
                if rep is None:
                    print(f'\n{rep}')
                else:
                    print(f'\n{rep}')
            case 6:
                rep = request(url_print_ink)
                if rep is None:
                    print(f'\n{rep}')
                else:
                    print(f'\n{rep}')
            case 7:
                break
            case _:
                print("Rentrer une bonne valeur !")


menu()
