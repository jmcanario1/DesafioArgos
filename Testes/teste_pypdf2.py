import PyPDF2
import numpy as np

pdf_file = open('plr_desafio.pdf', 'rb')
reader = PyPDF2.PdfReader(pdf_file)
numPages = len(reader.pages)

combined_text = ""

for page_index in range(numPages):
    page = reader.pages[page_index]
    combined_text += page.extract_text()


#Achar ingredientes
indice1 = combined_text.find('Ingredientes:')
indice2 = combined_text.find('ALÉRGICOS:')
plr_ingredientes = combined_text[indice1:indice2]

#Achar alergenicos
indice3 = combined_text.find('ALÉRGICOS:')
indice4 = combined_text.find('Claims-Others:')
plr_alergenicos = combined_text[indice3:indice4]

#Achar endereco
indice5 = combined_text.find('Signature Line Text :')
indice6 = combined_text.find('Signature Line Text : Indústria')
plr_endereco = combined_text[indice5:indice6]

#Achar industria
indice7 = combined_text.find('Indústria')
indice8 = combined_text.find('Quality')
plr_industria = combined_text[indice7:indice8]

#Achar tabela nutricional
indice9 = combined_text.find('Valor energético')
indice0 = combined_text.find('* Percentual de valores diários fornecidos pela porção')
nutricionalStr = combined_text[indice9:indice0]

lines = nutricionalStr.strip().split('\n')
num_columns = max(len(line.split()) for line in lines)

table_data = []
for line in lines:
    elements = line.split()
    first_element = " ".join(elements[:-3])
    other_elements = elements[-3:]
    table_data.append([first_element] + other_elements)

plr_nutricional = np.array(table_data, dtype=object)



print('-----------------------------------')
print(plr_ingredientes)
print('-----------------------------------')
print(plr_alergenicos)
print('-----------------------------------')
print(plr_endereco)
print('-----------------------------------')
print(plr_industria)
print('-----------------------------------')
print(plr_nutricional)