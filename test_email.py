import time
import unittest
from email import este_valid


class TestValidareEmail(unittest.TestCase):
    def test_fara_insemnatate(self):
        self.assertEqual(2, 2, "Cele doua trebuie sa fie egale...!!!")

    def test_de_test(self):
        time.sleep(1)
        self.assertNotEqual(2, 3, "Cele 2 nu trebuie sa fie egale..!!!")

    def test_contine_coada_de_maimuta(seld):
        # seld.assertTrue(este_valid("@."), "Trebuie sa contina @")
        seld.assertFalse(este_valid("asdsadasds"), "Trebuie sa contina @")


    def test_contine_punct(self):
        # self.assertTrue(este_valid("@."), "trebuie sa contina .")
        self.assertFalse(este_valid("dasdas@com"), "trebuie sa contina .")

    def test_are_ceva_inainte_de_coada_de_maimuta(self):
        self.assertFalse(este_valid("ceva.ro"), "trebuie sa contina ceva inainte de @")

    def caractere_neobisnuite(self):
        self.assertEqual(este_valid("$@ceva.ro"), "Trebuie sa nu contina caractere speciale")
        self.assertEqual(este_valid("!@ceva.ro"), "Trebuie sa nu contina caractere speciale")
        self.assertEqual(este_valid("#@ceva.ro"), "Trebuie sa nu contina caractere speciale")
        self.assertEqual(este_valid("%@ceva.ro"), "Trebuie sa nu contina caractere speciale")
        self.assertEqual(este_valid("^@ceva.ro"), "Trebuie sa nu contina caractere speciale")
        self.assertEqual(este_valid("&@ceva.ro"), "Trebuie sa nu contina caractere speciale")
        self.assertEqual(este_valid("*@ceva.ro"), "Trebuie sa nu contina caractere speciale")
        self.assertEqual(este_valid("<@ceva.ro"), "Trebuie sa nu contina caractere speciale")


    def test_numar_caractere(self):
        self.assertFalse(este_valid("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasaa@ceva.ro"), "Numarul maxim este de 64 de caractere")


    def test_are_ceva_dupa_punct(self):
        self.assertFalse(este_valid("a@."), "Trebuie sa aibe 2 caractere cel putin")
        self.assertFalse(este_valid("a@.--"))

        self.assertFalse(este_valid("a@.tt."))
    
    
    def test_minim_intre_puncte(self):
        # TODO:
        self.assertFalse(este_valid("a@..tt."))

    def test_1_coada_de_maimuta(self):
        self.assertFalse(este_valid("a@@.tt"))

        # TODO:
        self.assertFalse(este_valid("a@-.tt"))

if __name__ == "__main__":
    unittest.main()