def obtener_representacion_en_byte(caracter):
  codigo_ascii = ord(caracter)
  representacion_binaria = bin(codigo_ascii)[2:].zfill(8)  
  return codigo_ascii, representacion_binaria

def main():
  while True:
      print("\n--- Menú ---")
      print("1. Generar representación en byte y ASCII de un carácter")
      print("2. Generar representación en byte y ASCII de una palabra")
      print("3. Salir")

      opcion = input("Seleccione una opción (1, 2, o 3): ")

      if opcion == "1":
          caracter = input("Ingrese un carácter: ")
          if len(caracter) == 1:
              codigo_ascii, representacion_binaria = obtener_representacion_en_byte(caracter)
              print(f"Carácter: '{caracter}'")
              print(f"Código ASCII: {codigo_ascii}")
              print(f"Representación en byte: {representacion_binaria}")
          else:
              print("Por favor, ingrese solo un carácter.")
      elif opcion == "2":
          palabra = input("Ingrese una palabra: ")
          resultados = [obtener_representacion_en_byte(c) for c in palabra]

          print(f"Palabra: '{palabra}'")
          for resultado in resultados:
              caracter, representacion_binaria = resultado
              print(f"Carácter: '{chr(caracter)}', Código ASCII: {caracter}, Representación en byte: {representacion_binaria}")
      elif opcion == "3":
          print("Saliendo del programa. ¡Hasta luego!")
          break
      else:
          print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "_main_":
  main()