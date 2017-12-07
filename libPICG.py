import os
import matplotlib.pyplot as mp
import numpy as np

# questao 1
# criar a biblioteca .. OK

# questao 2 .. OK
# begin
def imread (img): # recebe o nome da imagem, e retorna a imagem
    if mp.imread(img).dtype == 'float32' :
        return ((mp.imread(img) * 255).astype(np.uint8))
    else : return (mp.imread(img))
# end

# questao 2.a, 2.b, 2.c .. OK
# begin
def imread2x (img): #recebe uma imagem e a exibe
    imgplot = mp.imshow(imread(img))
    mp.show()
    return None
# end

# questao 3 .. OK
# begin
def nchannels (img): # recebe a imagem e retorna o numero de canais
    return (len(imgread(img).shape))
# end

# questao 4 .. OK
# begin
def size (img): # recebe uma imagem e retorna um array largura x altura
    return (imread(img).shape[0], imread(img).shape[1])
# end

# questao 5 .. NOT OK
# begin
def rgb2gray (img) : # recebe uma imagem e retorna a imagem convertida em gs
    return None
# end
