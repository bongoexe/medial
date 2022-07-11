from PIL import Image
import pytesseract
import numpy as np
import shutil 
import os

percorsolista = 'percorso'
listatuttifiles = os.listdir(percorsolista)

listaunopervolta = listatuttifiles

for el in listaunopervolta:

    directoryunoperuno = 'percorso' + "/" + el
    filename = directoryunoperuno
    img1 = np.array(Image.open(filename))
    TestoTiratoDallimmagine = pytesseract.image_to_string(img1)

    #print(TestoTiratoDallimmagine) #per feedback dopo

    testoMaiuscolo = TestoTiratoDallimmagine
    testoMinuscolo = TestoTiratoDallimmagine.lower()
    testodatrovare = testoMinuscolo
    TestoTrovatoVariabile = testodatrovare.find("word to be found")
    #print(TestoTrovatoVariabile)

    originale = directoryunoperuno
    destinazione = 'path of the destination' + "/" + el
    if TestoTrovatoVariabile > -1:
        shutil.copyfile(originale, destinazione)

