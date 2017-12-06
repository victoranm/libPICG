import os
import matplotlib.pyplot as mp
import numpy as np

# questao 1
# criar a biblioteca .. OK

# questao 2

# begin
def imgread (n): # recebe o nome da imagem, e retorna a imagem
    img = mp.imread(n)
    # coverte para uint8 caso seja float32
    if img.dtype == 'float32' : img = (img * 255).astype(np.uint8)
    return img
# end

# questao 2.a

# begin
def imgread2a (n):
    imgplot = mp.imshow(imgread (n))
    mp.show()
    return None
# end

# questa 2.b
