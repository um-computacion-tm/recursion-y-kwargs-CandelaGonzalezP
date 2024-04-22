import unittest

"""def buscar_datos(*args, **kwargs):
  for arg in args:
        for key, value in kwargs.items():
            for k, v in value.items():
                if arg == v:
                    return True
        return False"""
  
def buscar_datos(*args, **kwargs):
    for key, value in kwargs.items():
        datos_persona = list(value.values())              
        if all(arg in datos_persona for arg in args):
            return key
    return None

  
database = {
    "persona_1": {
        "primer_nombre": "Candela",
        "segundo_nombre": "Agustina",
        "primer_apellido": "Gonzalez",
        "segundo_apellido": "Privtera"
        },
    "persona_2": {
        "primer_nombre": "Marina",
        "segundo_nombre": "",
        "primer_apellido": "Rivadeneira",
        "segundo_apellido": ""
        },
    "persona_3": {
        "primer_nombre": "Rocio",
        "segundo_nombre": "Pilar",
        "primer_apellido": "Portal",
        "segundo_apellido": "Romano"
        },
    "persona_4": {
        "primer_nombre": "Melina",
        "segundo_nombre": "",
        "primer_apellido": "Gomez",
        "segundo_apellido": ""
        }
}

buscar_datos("Candela", "Agustina", "Gonzalez", "Privitera", **database)
buscar_datos("Marina", "Rivadeneira", **database)
buscar_datos("Rocio", "Pilar", "Portal","Romano", **database)
buscar_datos("Melina", "Gomez", **database)

class test_busqueda_persona(unittest.TestCase):

    def test_0(self):
        self.assertIsNone(buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database), False)

    def test_1(self):
        self.assertEqual(buscar_datos("Candela", "Agustina","Gonzalez", "Privtera", **database), "persona_1")

    def test_2(self):
        self.assertEqual(buscar_datos("Marina", "Rivadeneira", **database), "persona_2")

    def test_3(self):
        self.assertEqual(buscar_datos("Rocio","Pilar","Portal", "Romano", **database), "persona_3")

    def test_4(self):
        self.assertEqual(buscar_datos("Melina", "Gomez",**database), "persona_4")

    def test_5(self):
        self.assertIsNone(buscar_datos("Andres", "Mauro","Perez", **database), False)


if __name__ == '__main__':
    unittest.main()  



