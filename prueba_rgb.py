from PIL import Image

def distanciaEuclidiana(n,m):#donde n es un vector y m es otro vector.
    distancia = ((n[0]-m[0])**2+(n[1]-m[1])**2+(n[2]-m[2])**2)**0.5
    return distancia
def porcentaje(n,f):#donde n es distancias y f es farthest point of all
    porcentajes =[]
    for i in n:
        porcentajes.append((i*100)/ f)
    return porcentajes

#im = Image.open(r"C:\Users\A01636706\Pictures\Control1_foto1_ag_centro.jpg") # Can be many different formats.
#pix = im.load()
#print (pix[100,100])  # Get the RGBA Value of the a pixel of an image

def prompixel(n,o,p,q,r): #where n =list of the images; for x-axis: o= start and p=final; for y-axis: q=start and r=final
    allframesprompixels = []
    for i in n:
        pixels = []
        im = Image.open(i)
        pix = im.load()
        for h in range(o,p+5,5):
            for g in range(q,r+10,10):
                pixels.append((pix[h, g]))  # Get the RGBA Value of the a pixel of an image

        #print(pixels)
        #print(len(pixels)) #Es una cuadrícula de x pixeles por imagen.
        suma = [0,0,0]
        for m in range(3):
            for j in range(len(pixels)):
                suma[m-1] += (pixels[j-1][m-1])/len(pixels) #falta redondear bien, later work
            suma[m-1]=(suma[m-1])//1
        allframesprompixels.append(suma)

    #print(allframesprompixels)
    # Empezamos a tratarlos como vectores.
    initialpoint = allframesprompixels[0]

    # Ahora calculamos las distancias de los puntos al punto inicial.
    distanciasa1 = []
    for i in allframesprompixels:
        distanciasa1.append(distanciaEuclidiana(i, initialpoint))
    #print(distanciasa1)
    # Ahora que tenemos las distancias, podemos proceder a calcular el porcentaje de cercanía de cada
    # punto al vector a evaluar considerando el punto más distante.
    print(distanciasa1[-1])
    porcentajea1 = (porcentaje(distanciasa1, distanciasa1[-1])) #La distancia más lejana del SOLO se utiliza para calcular porcentajes.
    return(porcentajea1)


lista_a1 = [r"C:\Users\A01636706\Videos\Proyecto_bioquímica\AA\AA\AA-1.jpeg",
                r"C:\Users\A01636706\Videos\Proyecto_bioquímica\AA\AA\AA-3.jpeg",
                r"C:\Users\A01636706\Videos\Proyecto_bioquímica\AA\AA\AA-4.jpeg",
                r"C:\Users\A01636706\Videos\Proyecto_bioquímica\AA\AA\AA-5.jpeg",
                r"C:\Users\A01636706\Videos\Proyecto_bioquímica\AA\AA\AA-6.jpeg",
                r"C:\Users\A01636706\Videos\Proyecto_bioquímica\AA\AA\AA-7.jpeg",
                r"C:\Users\A01636706\Videos\Proyecto_bioquímica\AA\AA\AA-8.jpeg",
                r"C:\Users\A01636706\Videos\Proyecto_bioquímica\AA\AA\AA-9.jpeg",
                r"C:\Users\A01636706\Videos\Proyecto_bioquímica\AA\AA\AA-10.jpeg",
                r"C:\Users\A01636706\Videos\Proyecto_bioquímica\AA\AA\AA-11.jpeg",
                r"C:\Users\A01636706\Videos\Proyecto_bioquímica\AA\AA\AA-12.jpeg",
                r"C:\Users\A01636706\Videos\Proyecto_bioquímica\AA\AA\AA-13.jpeg",
                r"C:\Users\A01636706\Videos\Proyecto_bioquímica\AA\AA\AA-14.jpeg",
                r"C:\Users\A01636706\Videos\Proyecto_bioquímica\AA\AA\AA-15.jpeg",
                r"C:\Users\A01636706\Videos\Proyecto_bioquímica\AA\AA\AA-16.jpeg",
                r"C:\Users\A01636706\Videos\Proyecto_bioquímica\AA\AA\AA-17.jpeg",
                r"C:\Users\A01636706\Videos\Proyecto_bioquímica\AA\AA\AA-18.jpeg",
                r"C:\Users\A01636706\Videos\Proyecto_bioquímica\AA\AA\AA-19.jpeg",
                r"C:\Users\A01636706\Videos\Proyecto_bioquímica\AA\AA\AA-20.jpeg",
                r"C:\Users\A01636706\Videos\Proyecto_bioquímica\AA\AA\AA-21.jpeg"
                ]

#------------------------------------------------------------------------------------------------------------
#ANALISIS, INTRODUZCA LA CUADRÍCULA A EVALUAR
#------------------------------------------------------------------------------------------------------------

#print("REBANADAS")
#print("MOLIDOS")
#La distancia más lejana del SOLO es  y se utiliza para calcular porcentajes.
print(" - Solo")
print(prompixel(lista_a1,1185,1215,645,1005))
print(" - Limón")
print(prompixel(lista_a1,1475,1505,675,965))
print(" - Solución 1")
print(prompixel(lista_a1,880,925,645,995)) #x_axis: 550-610;  y-axis: 620-900
print(" - Solución 2")
print(prompixel(lista_a1,625,675,760,980))
print(" - Solución 3")
print(prompixel(lista_a1,325,365,730,930))

#Prueba para ver que los estados iniciales sean iguales.
def checkinitial(n,o,p,q,r): #where n =list of the images; for x-axis: o= start and p=final; for y-axis: q=start and r=final
    for i in n:
        pixels = []
        im = Image.open(i)
        pix = im.load()
        for h in range(o,p+5,5):
            for g in range(q,r+10,10):
                pixels.append((pix[h, g]))  # Get the RGBA Value of the a pixel of an image

        #print(pixels)
        #print(len(pixels)) #Es una cuadrícula de x pixeles por imagen.
        suma = [0,0,0]
        for m in range(3):
            for j in range(len(pixels)):
                suma[m-1] += (pixels[j-1][m-1])/len(pixels) #falta redondear bien, later work
            suma[m-1]=(suma[m-1])//1
    return suma

listacheck = [r"C:\Users\A01636706\Videos\Proyecto_bioquímica\Aguacate\A-3-Frames\a3-1.jpeg"]
#print("A-3 - Solo")
#print(checkinitial(listacheck,1080,1100,270,360))
#print("A-3 - Limón")
#print(checkinitial(listacheck,830,880,335,405))
#print("A-3 Rebanadas- Vinagre")
#print(checkinitial(listacheck,565,615,260,320)) #x_axis: 550-610;  y-axis: 620-900
#print("A-3 Rebanadas- Jugo arándano")
#print(checkinitial(listacheck,260,280,260,350))