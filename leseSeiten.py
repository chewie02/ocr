from PIL import Image
import pytesseract


# img = Image.open("007.png")
# img = "007.png"
# text = pytesseract.image_to_string(img, lang="deu")
# print(text)
# fh = open('./texte/007.txt', 'w')
# fh.write(text)
# fh.close()


counter = open('liste.txt', 'r')
files = counter.readlines()
counter.close()
pufferstring = []

for i in files:
    img = Image.open(i[0:-1])
    text = pytesseract.image_to_string(img, lang="deu")
    pufferstring.append(text)

return pufferstring
f = open('texte/seiten.txt', 'w')
f.write(str( pufferstring ))
f.close()
print(pufferstring)
text = str(pufferstring)
text
text.replace('-\n', '')
text.replace("\\n", " $ ")

satz = ''
for i in pufferstring:
    ' '.join(satz, i)
