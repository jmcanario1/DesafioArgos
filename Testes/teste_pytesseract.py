import pytesseract
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

imagem_teste = cv2.imread('lacta1.png')
boundings_teste = pytesseract.image_to_boxes(imagem_teste, lang="por")
print(boundings_teste)
'''
texto_teste = pytesseract.image_to_string(imagem_teste, lang="por")
texto_teste = texto_teste.replace('|', '')
texto_teste = texto_teste.replace('0', 'o')
#print(texto_teste)

#gray = cv2.cvtColor(imagem_rotulo, cv2.COLOR_BGR2GRAY)
#val, thresh = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)
#cv2.imshow('thresh', thresh)
#cv2.waitKey(0)




indice1 = texto_teste.find("Valor energético")
indice2 = texto_teste.find("* Percentual de valores diários fornecidos pela porção")
nutricional = texto_teste[indice1:indice2]
print(nutricional)


lines = nutricional.strip().split('\n')
table_data = []
for line in lines:
    elements = line.split()
    first_element = " ".join(elements[:-3])
    other_elements = elements[-3:]
    table_data.append([first_element] + other_elements)

numpy_array = np.array(table_data, dtype=object)

print(numpy_array)'''