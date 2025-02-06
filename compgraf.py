import tkinter as tk

def analitico(x1, y1, x2, y2, cor="black"):
    if x1 == x2:
        for y in range(y1, y2 + 1):
            pintar(x1, y,cor)
        return

    if x2 < x1:
        x1, x2, y1, y2 = x2, x1, y2, y1

    m = (y2 - y1) / (x2 - x1)
    b = y2 - m * x2

    for x in range(x1, x2 + 1):
        y = round(m * x + b)
        pintar(x, y,cor)


def dda(x1, y1, x2, y2, cor="black"):
    if x2 < x1:
        x1, x2, y1, y2 = x2, x1, y2, y1

    dx = x2 - x1
    dy = y2 - y1
    if (abs(dx) > abs(dy)):
        incremento = dy / dx
        y = y1
        for x in range(x1, x2 + 1):
            pintar(x, round(y),cor)
            y += incremento

    else:
        incremento = dx / dy
        x = x1
        for y in range(y1, y2 + 1):
            pintar(round(x), y,cor)
            x += incremento


def bresenham(x1, y1, x2, y2, cor="black"):
    deltax = abs(x2 - x1)
    deltay = abs(y2 - y1)
    eixo = deltay > deltax

    if eixo:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        deltax, deltay = deltay, deltax

    if x1 > x2:
        x1, y1, x2, y2 = x2, y2, x1, y1

    p = 2 * deltay - deltax
    y = y1
    y_inc = 1 if y2 > y1 else -1

    for x in range(x1, x2 + 1):
        if eixo:
            pintar(y, x,cor)
        else:
            pintar(x, y,cor)
        if p >= 0:
            y += y_inc
            p -= 2 * deltax 
        p += 2 * deltay


import math


def parametrica(xc, yc, r, cor="black"):
    x = xc + r
    y = yc
    for t in range(1, 360):
        pintar(round(x), round(y),cor)
        x = xc + r * math.cos((math.pi * t) / 180)
        y = yc + r * math.sin((math.pi * t) / 180)


def incremental_simetria(xc, yc, r, cor="black"):
    theta = 1 / r
    ct = math.cos(theta)
    st = math.sin(theta)
    x = 0
    y = r

    while y >= x:
        pintar(round(xc + x), round(yc + y), cor)
        pintar(round(xc - x), round(yc + y), cor)
        pintar(round(xc + x), round(yc - y), cor)
        pintar(round(xc - x), round(yc - y), cor)
        pintar(round(yc + y), round(xc + x), cor)
        pintar(round(yc + y), round(xc - x), cor)
        pintar(round(yc - y), round(xc + x), cor)
        pintar(round(yc - y), round(xc - x), cor)
        x_novo = x * ct - y * st
        y_novo = x * st + y * ct
        x, y = x_novo, y_novo


def circ_bresenham(xc, yc, r, cor="black"):
    x = 0
    y = r
    p = 1 - r
    while y>=x:    
        pintar(round(xc + x), round(yc + y), cor)
        pintar(round(xc - x), round(yc + y), cor)
        pintar(round(xc + x), round(yc - y), cor)
        pintar(round(xc - x), round(yc - y), cor)
        pintar(round(yc + y), round(xc + x), cor)
        pintar(round(yc + y), round(xc - x), cor)
        pintar(round(yc - y), round(xc + x), cor)
        pintar(round(yc - y), round(xc - x), cor)
        if (p >= 0):
            y = y - 1
            p = p + (2 * x) - (2 * y) + 5
            x = x + 1
        else:
            p = p + (2 * x) + 3
            x = x + 1

def getPixel(x,y):
    return canvas.find_overlapping(
        x * PIXEL_SIZE, y * PIXEL_SIZE, (x + 1) * PIXEL_SIZE, (y + 1) * PIXEL_SIZE
    )

def flood_fill( x, y, cor_alvo, nova_cor = "black"):
    objetos = getPixel(x,y)

    if not objetos:
        return
    cor_atual = canvas.itemcget(objetos[-1], "fill")

    if cor_atual != cor_alvo:
        return

    pintar(x, y, nova_cor)

    flood_fill( x + 1, y, cor_alvo, nova_cor)
    flood_fill(x - 1, y, cor_alvo, nova_cor)
    flood_fill( x, y + 1, cor_alvo, nova_cor)
    flood_fill(x, y - 1, cor_alvo, nova_cor)

def varredura_retangulo(x1,y1,x2,y2,cor="black"):
    objetos = getPixel(x1, y1)

    if not objetos:
        return

    cor_borda = canvas.itemcget(objetos[-1], "fill")

    for y in range(y1 + 1, y2):
        for x in range(x1 + 1, x2):
            cor_atual = canvas.itemcget(getPixel(x, y)[-1], "fill")
            if cor_atual != cor_borda:
                pintar(x, y, cor)
                
def varredura_circulo(xc,yc,r,cor="black"):
    y =  yc-r
    while(yc-r<=y<=yc+r):
        x1 = round(xc - math.sqrt(r**2 - (y - yc)**2))
        x2 = round(xc + math.sqrt(r**2 - (y - yc)**2))
        for x in range(x1+1,x2):
            pintar(x,y,cor)
        y+= 1
    


def calcular_intersecoes(poligono, y_scan):
    intersecoes = []
    for linha in poligono:
        x1, y1, x2, y2 = linha 

        if y1 != y2 and min(y1, y2) <= y_scan < max(y1, y2):
            x_intersecao = x1 + (y_scan - y1) * (x2 - x1) / (y2 - y1)
            intersecoes.append(round(x_intersecao)) 
    
    return sorted(intersecoes)


def varredura(poligono,cor = "black"):
    ymin = min(y for _, y, _, _ in poligono)
    ymin2 = min(y for _, _,_,y in poligono)
    ymax = max(y for _, y, _, _ in poligono)
    ymax2 = max(y for _, _, _, y in poligono)
    
    if(ymax2>ymax):
        ymax = ymax2
    if(ymin2<ymin):
        ymin = ymin2
        
        
    for y_scan in range(ymin, ymax + 1):
        intersecoes = calcular_intersecoes(poligono, y_scan)
        
        if len(intersecoes) % 2 != 0:
            continue
        
        for i in range(0, len(intersecoes), 2):
            x_inicio = int(min(intersecoes[i], intersecoes[i + 1]))
            x_fim = int(max(intersecoes[i], intersecoes[i + 1]))
            
            for x in range(x_inicio, x_fim + 1):
                pintar(x, y_scan,cor)


                

def pintar(x, y, cor='black'):
    canvas.create_rectangle(x * PIXEL_SIZE,
                            y * PIXEL_SIZE, (x + 1) * PIXEL_SIZE,
                            (y + 1) * PIXEL_SIZE,
                            fill=cor,
                            outline="")

GRID_SIZE = 40
PIXEL_SIZE = 10

root = tk.Tk()
root.title("Grid")

canvas = tk.Canvas(root,
                   width=GRID_SIZE * PIXEL_SIZE,
                   height=GRID_SIZE * PIXEL_SIZE)
canvas.pack()

for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        x1 = col * PIXEL_SIZE
        y1 = row * PIXEL_SIZE
        x2 = x1 + PIXEL_SIZE
        y2 = y1 + PIXEL_SIZE
        canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")

# analitico(2, 3, 18, 15, "red")
# analitico(2, 10, 25, 10, "red")
# analitico(5, 17, 5, 30, "red")
# analitico(2, 3, 5, 30, "red")


# dda(2, 3, 18, 15, "red")
# dda(2, 10, 25, 10, "red")
# dda(5, 17, 5, 30, "red")
# dda(2, 3, 5, 30, "red")

# bresenham(2, 3, 18, 15, "blue")
# bresenham(2, 10, 25, 10, "blue")
# bresenham(5, 17, 5, 30, "blue")
# bresenham(2, 3, 5, 30, "blue")


# incremental_simetria( 8, 8, 6, "blue")
# parametrica( 15, 22, 9, "red")

# Círculo
# flood_fill(19, 19, "white", "blue")
# circ_bresenham(19, 19, 17, "green")
# varredura_circulo(19, 19, 17,"black")


# Retângulo
# bresenham(5, 5, 15, 5, "black")
# bresenham( 5, 10, 15, 10, "black")
# bresenham( 5, 5, 5, 10, "black")
# bresenham( 15, 5, 15, 10, "black")
# varredura_retangulo(5,5,15,10,'red')
# flood_fill(6,6,"white","blue")

# Forma a)
# bresenham( 10, 10, 28, 18)
# bresenham( 10, 10, 2, 15)
# bresenham( 9, 18, 2, 15)
# bresenham(9, 18, 3, 24)
# bresenham( 25, 21, 28, 18)
# bresenham( 25, 21, 3, 24)
# flood_fill(4,15,"white","blue")
# poligono1 = [(10, 10, 28, 18), (10, 10, 2, 15), (9, 18, 2, 15), (9, 18, 3, 24), (25, 21, 28, 18), (25, 21, 3, 24)]
# varredura(poligono1)


# Forma b)
# bresenham(3,10,7,20)
# bresenham(23,19,7,20)
# bresenham(23,19,23,15)
# bresenham(17,16,23,15)
# bresenham(17,16,18,23)
# bresenham(33,18,18,23)
# bresenham(33,18,32,9)
# bresenham(17,5,32,9)
# bresenham(17,5,3,10)
# flood_fill(4,11,"white","blue")
# poligono2 = [ (3,10,7,20), (23,19,7,20), (23,19,23,15), (17,16,23,15), (17,16,18,23), (33,18,18,23),
#                      (33,18,32,9), (17,5,32,9), (17,5,3,10)]
# varredura(poligono2)


root.mainloop()