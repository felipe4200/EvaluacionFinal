# EvaluacionFinal
evaluación final de herramientas computacionales 



import sys

def get_results(word):
    # Define la lógica para obtener resultados (reemplaza esto según tus necesidades)
    return len(word)

menu = int(input('Menu\n===\n1. Character\n2. Word\n'))

if menu == 1:
    char = input('Enter a character: ')
    word = char
elif menu == 2:
    word = input('Enter a word: ')
else:
    sys.exit()

print('Results\n===')
results = get_results(word)
print('Total: {0}'.format(results))
