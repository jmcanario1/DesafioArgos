import numpy as np

data = """
Valor energético (kcal) 507 127 6
Carboidratos (g) 65 16 5
Açúcares totais (g) 55 14 0
Açúcares adicionados (g)| 52 13 26
Proteínas (g) 5,1 18 3
Gorduras totais (g) 25 6,2 10
Gorduras saturadas (g) 12 3 15
Gorduras trans (g) 0,2 o o
Fibras alimentares (g) 2,7 07 3
Sódio (mg) 30 7,6 0
"""

lines = data.strip().split('\n')
# Extracting data into the desired format
table_data = []
for line in lines:
    elements = line.split()
    first_element = " ".join(elements[:-3])
    other_elements = elements[-3:]
    table_data.append([first_element] + other_elements)

# Creating a NumPy array from the extracted data
numpy_array = np.array(table_data, dtype=object)

print(numpy_array)
