class InkLevelException(Exception):
    """ my custom exception class """
    pass


class EmptyCardException(Exception):
    """ my custom exception class """
    pass


class InvalidCardException(Exception):
    """ my custom exception class """
    pass


class PrinterDriver:
    def __init__(self, model: str, dpi: str, card_type: str, card_tray_max: int, card_tray: int):
        self.model = model
        self.dpi = dpi
        self.card_type = card_type
        self.card_tray_max = card_tray_max
        self.card_tray = card_tray
        self.spooler = ["933"]
        self.ink_level = {
            "black": 100,
            "cyan": 100,
            "magenta": 100,
            "yellow": 100
        }

    def get_printer_info(self):
        return {
            "model": self.model,
            "dpi": self.dpi,
            "card_type": self.card_type
        }

    def get_card_tray_status(self):
        return "Full" if self.card_tray > 0 else "Empty"

    def send_card_to_spooler(self, card_number: str):
        for spool in self.spooler:
            if spool == card_number:
                raise InvalidCardException('Card is already in spooler')
        self.spooler.append(card_number)
        return True

    def get_card_in_spooler(self):
        return self.spooler[0]

    def get_spooler(self):
        return self.spooler

    def get_ink_levels(self):
        return self.ink_level

    def print(self):
        # si le spooler est vide sinon on enlève la card
        if not self.spooler:
            return False
        else:
            card = self.spooler[0]
            self.spooler.pop(0)

        # si on enlève 1 papier est ce qu'il en reste
        if self.card_tray - 1 < 0:
            raise EmptyCardException("Empty paper")
        else:
            self.card_tray -= 1

        # si l'encre est à 0
        if self.ink_level["black"] - len(card) < 0 or self.ink_level["cyan"] < 0 or self.ink_level["magenta"] < 0 or \
                self.ink_level["yellow"] < 0:
            raise InkLevelException("Ink level is too low")
        else:
            self.ink_level["black"] -= len(card)
            self.ink_level["cyan"] -= len(card)
            self.ink_level["magenta"] -= len(card)
            self.ink_level["yellow"] -= len(card)

        return True
