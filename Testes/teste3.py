import pytesseract
import PyPDF2
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

nutricional = np.array([])
ingredientes = ""
alergenicos = ""
endereco = ""
industria = ""
plr_nutricional = np.array([])
plr_ingredientes = ""
plr_alergenicos = ""
plr_endereco = ""
plr_industria = ""


imagem_rotulo = cv2.imread('lacta1.png')
texto_rotulo = pytesseract.image_to_string(imagem_rotulo, lang="por")

#Manipular o PDF
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
plr_ingredientes = combined_text[indice1:indice2].lower()
plr_ingredientes = plr_ingredientes.replace('\n', ' ')
plr_ingredientes = plr_ingredientes.replace(' -', '-')
plr_ingredientes = plr_ingredientes.replace('  ', ' ')

#Achar alergenicos
indice3 = combined_text.find('ALÉRGICOS:')
indice4 = combined_text.find('Claims-Others:')
plr_alergenicos = combined_text[indice3:indice4].lower()
plr_alergenicos = plr_alergenicos.replace('\n', ' ')

#Achar endereco
indice5 = combined_text.find('Signature Line Text :')
indice6 = combined_text.find('Signature Line Text : Indústria')
plr_endereco = combined_text[indice5:indice6].lower()

#Achar industria
indice7 = combined_text.find('Indústria')
indice8 = combined_text.find('Quality')
plr_industria = combined_text[indice7:indice8].lower()
plr_industria = plr_industria.replace('\n', ' ')

#Achar tabela nutricional
indice9 = combined_text.find('Valor energético')
indice0 = combined_text.find('* Percentual de valores diários fornecidos pela porção')
nutricionalStr = combined_text[indice9:indice0].lower()
nutricionalStr = nutricionalStr.replace('|', '')
nutricionalStr = nutricionalStr.replace('0', 'o')
nutricionalStr = nutricionalStr.replace(',', '')

lines = nutricionalStr.strip().split('\n')
num_columns = max(len(line.split()) for line in lines)

table_data = []
for line in lines:
    elements = line.split()
    first_element = " ".join(elements[:-3])
    other_elements = elements[-3:]
    table_data.append([first_element] + other_elements)

plr_nutricional = np.array(table_data, dtype=object)

#Manipular texto da arte
imagem_arte = cv2.imread('lacta1.png')
texto_arte = pytesseract.image_to_string(imagem_arte, lang="por")

#Achar ingredientes
indice1 = texto_arte.find('INGREDIENTES:')
indice2 = texto_arte.find('.\n\n')
ingredientes = texto_arte[indice1:indice2].lower()
ingredientes = ingredientes.replace('\n', ' ')
ingredientes = ingredientes.replace(' -', '-')
ingredientes = ingredientes.replace('  ', ' ')

#Achar alergenicos
indice3 = texto_arte.find('ALÉRGICOS:')
indice4 = texto_arte.find('FABRICADO POR:')
alergenicos = texto_arte[indice3:indice4].lower()
alergenicos = alergenicos.replace('\n', ' ')

#Achar endereco
indice5 = texto_arte.find('FABRICADO POR:')
indice6 = texto_arte.find('INDÚSTRIA BRASILEIRA')
endereco = texto_arte[indice5:indice6].lower()

#Achar industria
indice7 = texto_arte.find('Indústria')
indice8 = texto_arte.find('Quality')
industria = texto_arte[indice7:indice8].lower()
industria = industria.replace('\n', ' ')

#Achar tabela nutricional
indice9 = texto_rotulo.find("Valor energético")
indice0 = texto_rotulo.find("* Percentual de valores diários fornecidos pela porção")
arte_nutricional = texto_rotulo[indice9:indice0].lower()
arte_nutricional = arte_nutricional.replace('|', '')
arte_nutricional = arte_nutricional.replace('0', 'o')
arte_nutricional = arte_nutricional.replace(',', '')


lines = arte_nutricional.strip().split('\n')
table_data = []
for line in lines:
    elements = line.split()
    first_element = " ".join(elements[:-3])
    other_elements = elements[-3:]
    table_data.append([first_element] + other_elements)

nutricional = np.array(table_data, dtype=object)


#Indice de conformidade
conformidade = 0

comparacaoArrays = nutricional == plr_nutricional
count_true = np.count_nonzero(comparacaoArrays)
porcentagem = (count_true / comparacaoArrays.size)
conformidade += porcentagem

if ingredientes in plr_ingredientes or plr_ingredientes in ingredientes:
    conformidade += 1

if alergenicos in plr_alergenicos or plr_alergenicos in alergenicos:
    conformidade += 1

if endereco in plr_endereco or plr_endereco in endereco:
    conformidade += 1

if industria in plr_industria or plr_industria in industria:
    conformidade += 1

print(str(conformidade) + '/5')