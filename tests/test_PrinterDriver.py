from projet.PrinterDriver import PrinterDriver as Pr, EmptyCardException, InkLevelException, InvalidCardException
import pytest

printer = Pr("Xerox Printer", "1200", "plastic", 50, 30)


def test_get_return_driver():
    assert printer.get_printer_info() == {
        "model": "Xerox Printer",
        "dpi": "1200",
        "card_type": "plastic"
    }


def test_get_card_tray_status_full():
    assert printer.get_card_tray_status() == "Full"


def test_get_card_tray_status_empty():
    printer_test = Pr("Xerox Printer", "1200", "plastic", 10, 0)
    assert printer_test.get_card_tray_status() == "Empty"


def test_spooler():
    assert printer.send_card_to_spooler("21345")
    with pytest.raises(InvalidCardException):
        printer.send_card_to_spooler("933")


def test_ink_level():
    assert printer.get_ink_levels() == {
        "black": 100,
        "cyan": 100,
        "magenta": 100,
        "yellow": 100
    }


def test_print():
    assert printer.print()


def test_spooler_nothing():
    printer.print()
    assert not printer.print()


def test_ink():
    printer.print()
    assert printer.get_ink_levels() == {
        "black": 92,
        "cyan": 92,
        "magenta": 92,
        "yellow": 92
    }


def test_print_Empty_card():
    printer_test = Pr("Xerox Printer", "1200", "plastic", 10, 0)

    with pytest.raises(EmptyCardException):
        printer_test.print()


def test_print_Ink_Level_at_zero():
    printer_test = Pr("Xerox Printer", "1200", "plastic", 10, 4)
    printer_test.send_card_to_spooler(
        "99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")
    printer_test.print()
    with pytest.raises(InkLevelException):
        printer_test.print()


def test_print_spooler_null():
    printer.print()
    assert not printer.print()


def test_get_card_in_spooler_zero():
    printer_test = Pr("Xerox Printer", "1200", "plastic", 10, 2)
    assert printer_test.get_card_in_spooler() == "933"


def test_get_spooler():
    printer_test = Pr("Xerox Printer", "1200", "plastic", 10, 2)
    assert printer_test.get_spooler() == ["933"]
