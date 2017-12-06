import os
import matplotlib.pyplot as mp
import numpy as np

# questao 1
# criar a biblioteca .. OK

# questao 2 .. OK

# begin
def imgread (n): # recebe o nome da imagem, e retorna a imagem
    img = mp.imread(n)
    # coverte para uint8 caso seja float32
    if img.dtype == 'float32' : img = (img * 255).astype(np.uint8)
    return img
# end

# questao 2.a, 2.b, 2.c .. OK

# begin
def imgread2x (n):
    imgplot = mp.imshow(imgread (n))
    mp.show()
    return None
# end

# questao 3 .. OK

# begin
def nchannels (n): # recebe a imagem e retorna o numero de canais
    nc = len(n.shape)
    return nc
# end

# questao 4

# begin
def size (n): # recebe uma imagem e retorna um array altura x largura
    return None
# end
