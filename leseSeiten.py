from PIL import Image
import pytesseract
img = Image.open("007.png")
# img = "007.png"
text = pytesseract.image_to_string(img, lang="deu")
print(text)
fh = open('./texte/007.txt', 'w')
fh.write(text)
fh.close()

