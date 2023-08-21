import PyPDF2
import numpy as np

pdf_file = open('plr_desafio.pdf', 'rb')
reader = PyPDF2.PdfReader(pdf_file)
numPages = len(reader.pages)

combined_text = ""

for page_index in range(numPages):
    page = reader.pages[page_index]
    combined_text += page.extract_text()

indice1 = combined_text.find('Valor energético')
indice2 = combined_text.find('* Percentual de valores diários fornecidos pela porção')
plr_nutricional = combined_text[indice1:indice2]
print(plr_nutricional)
print('-------------------')

lines = plr_nutricional.strip().split('\n')
num_columns = max(len(line.split()) for line in lines)

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