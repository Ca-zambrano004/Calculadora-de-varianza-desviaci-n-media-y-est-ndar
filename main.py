# main.py
from mean_var_std import calculate
import unittest
import test_module

def ejecutar_calculos():
    datos = [0,1,2,3,4,5,6,7,8]
    resultado = calculate(datos)
    print("Resultados de la función calculate():")
    for clave, valor in resultado.items():
        print(f"{clave}: {valor}")

def ejecutar_pruebas():
    print("\nEjecutando pruebas unitarias...\n")
    suite = unittest.TestLoader().loadTestsFromModule(test_module)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    # Primero ejecuta la función con datos de ejemplo
    ejecutar_calculos()
    # Luego corre las pruebas unitarias
    ejecutar_pruebas()
