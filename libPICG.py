import os
import matplotlib.pyplot as mp
import numpy as np

##! LISTA 1 !##

# questao 1
# criar a biblioteca .. OK

# questao 2 .. OK
# recebe o nome da imagem, e retorna a imagem
# begin
def imread (img) :
    if mp.imread(img).dtype == 'float32' :
        return ((mp.imread(img) * 255).astype(np.uint8))
    else : return (mp.imread(img))
# end

# questao 2.a, 2.b, 2.c .. OK
# recebe uma imagem e a exibe
# begin
def imread2x (img) :
    imgplot = mp.imshow(imread(img))
    mp.show()
    return None
# end

# questao 3 .. OK
# recebe a imagem e retorna o numero de canais
# begin
def nchannels (img) : return (len(img.shape))
# end

# questao 4 .. OK
# recebe uma imagem e retorna um array largura x altura
# begin
def size (img) : return (img.shape[0], img.shape[1])
# end

# questao 5 .. NOT OK
# recebe uma imagem e retorna a imagem convertida em gs
# begin
def rgb2gray (img) :
    return None
# end
