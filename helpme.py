import numpy as np
import cv2
import imutils
from imutils import contours
from imutils import perspective
from scipy.spatial import distance as dist
from PIL import Image, ImageEnhance
from matplotlib import pyplot as plt
#from keras.preprocessing import image
from itertools import product
import os
def findpixels(path):
 with Image.open(path) as im: #knipie.PNG
    # px = im.load()
    # print(px[250, 400])
    #590 435
    """img = cv2.imread('./images/iets.png',0)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])

    for i in range(0,256):
        #print("hist[0],i",hist[i],i)
        producthist =hist[i]*i
        i+=1
    """
    """i=0
    ja = []
    for x in range(0,59):
        for y in range(0,30):
            mimi = im.getpixel((x, y))
            ja += mimi


    #print("ja,i",ja,i)
    ja.sort()
    #print("ja",ja)
    #print("ja[79]",ja[79])
    average = sum(ja)/len(ja)
    print("average",average)
    tellll = 0
    """

    width = im.size[0]-23
    height = im.size[1]-23

    for x in range(1, width):
        #print("x", x)
        for y in range(1, height):
            iets  = im.getpixel((x,y))
            iets2 = im.getpixel((x+1,y+1))
            iets3 = im.getpixel((x-1,y-1))
            iets4 = im.getpixel((x+1,y-1))
            iets5 = im.getpixel((x-1,y+1))
            iets6 = im.getpixel((x,y+1))
            iets7 = im.getpixel((x,y-1))
            iets8 = im.getpixel((x-1, y))
            iets9 = im.getpixel((x+1, y))

            aftrek2 = iets[0]-iets2[0]
            aftrek3 = iets[0]-iets3[0]
            aftrek4 = iets[0]-iets4[0]
            aftrek5 = iets[0] -iets5[0]
            aftrek6 = iets[0] -iets6[0]
            aftrek7 = iets[0] -iets7[0]
            aftrek8 = iets[0] - iets8[0]
            aftrek9 = iets[0] -iets9[0]

            #print(aftrek2,aftrek3,aftrek4,aftrek5,aftrek6,aftrek7,aftrek8)
            #print(abs(aftrek2),abs(aftrek3),abs(aftrek4),abs(aftrek5),abs(aftrek6),abs(aftrek7),abs(aftrek8))
            absaftrek2 = abs(aftrek2)
            absaftrek3 = abs(aftrek3)
            absaftrek4 = abs(aftrek4)
            absaftrek5 = abs(aftrek5)
            absaftrek6 = abs(aftrek6)
            absaftrek7 = abs(aftrek7)
            absaftrek8 = abs(aftrek8)
            absaftrek9 = abs(aftrek9)
            #print(" pixelwaarde, x , y ", iets, x, y)
            #if( iets[0]!=255 and iets[1]!=255 and iets[2]!=255):
                #print(" pixelwaarde, x , y ", iets, x, y)
                #im.putpixel((x,y),(237,28,36)) #rood
            help1 =im.getpixel((x + 2, y - 1))
            help2 =im.getpixel((x-2,y-1))
            help3 = im.getpixel((x - 2, y + 1))
            help4 = im.getpixel((x + 2, y + 1))
            help5 = im.getpixel((x + 2, y ))
            absaftrek62 =abs(iets[0]-help5[0])
            absaftrek67 =abs(iets6[0]-iets7[0])
            help12 = im.getpixel((x , y + 2))
            help22 = im.getpixel((x , y - 2))
            help32 = im.getpixel((x+2, y ))
            help42 = im.getpixel((x-2, y ))
            help121 = im.getpixel((x , y + 4))
            help221 = im.getpixel((x , y - 4))
            help31 = im.getpixel((x +4, y ))
            help33 = im.getpixel((x-4, y ))
            helpme1 = im.getpixel((x+4 , y + 4))
            helpme2 =im.getpixel((x-4 , y + 4))
            helpme3 =im.getpixel((x+4, y - 4))
            helpme4 =im.getpixel((x-4, y + 4))
            """helpme5
            helpme6 
            helpme7
            helpme8"""
            help1222= abs(help12[0]-help22[0])
            help121221=abs(help121[0]-help221[0])
            help3133=abs(help31[0]-help33[0])
            help3242 =abs(help32[0]-help42[0])
            naburig1= help1[0]-help2[0]
            naburig2 = help1[0]-help3[0]
            naburig3 =  help1[0] -help4[0]
            naburig4 = help4[0]-help3[0]
            absnaburig1 =abs(naburig1)
            absnaburig2 = abs(naburig2)
            absnaburig3 = abs(naburig3)
            absnaburig4 = abs(naburig4)
            naburig34 =abs(help12[0]-help22[0])


            def tellen():
                xii = 1
                neen=1
                for xi in range(x,x+4):
                    for yi in range(y,y+4):
                        sum = im.getpixel((xi, yi))
                        neen = sum[0]
                        neen += neen
                        xii += 1 #hier gaat er wrs iets fout
                        if(neen==0): neen=1
                return neen / xii


            def tellen2():
                xii = 1
                neen=1
                for xi in range(x+18,x+22):
                    for yi in range(y+18,y+22):
                        sum = im.getpixel((xi, yi))
                        neen = sum[0]
                        neen += neen
                        xii += 1
                        if (neen == 0): neen = 1
                return neen / xii


            tellertje1 = tellen()
            #print("tellertje1",tellertje1)
            tellertje2 = tellen2()
            #print("tellertje2", tellertje2)
            verschiltellertjes= abs(tellertje1 -tellertje2)
            #print("verschiltellertjes",verschiltellertjes)
            if(5< absaftrek4<90 and im.getpixel((x,y)) <(140,140,140) and im.getpixel((x + 4, y ))<(140,140,140) and im.getpixel((x - 2, y )) <(140,140,140)
                and im.getpixel((x+1,y-1))<(120,120,120) ):
                # and absnaburig1>2 and absnaburig2>2 and absnaburig3>2 and absnaburig4>2  and
                #abs heeft hier veel nut en 90 niet verkleinen en 180 niet vergroten
                im.putpixel((x, y), (237, 28, 36))  # rood # interesanntttt

            #elif( 10< absaftrek2<90 and im.getpixel((x,y)) <(170,170,170)):
              #im.putpixel((x,y),(34,174,76)) #groen""" # ook interesanttt
                #geen roze dat werkt niet donkerblauw wel
            #if(10 < absaftrek3 < 20 and im.getpixel((x, y)) < (180, 180, 180)):  # waar vleesje zit
                #im.putpixel((x, y), (255, 242, 0) )  # geel
            elif (10 < absaftrek7 < 20 and im.getpixel((x, y)) < (180, 180, 180) ):
                im.putpixel((x, y), (128, 255, 254))  # felblauw #interessanntttttttt
                #print("x,y", x, y) #joepie dat klopt
            elif (12< absaftrek9 < 30 and help12<(205, 205, 205) and help22<(205, 205, 205) and help32< (205, 205, 205) and help42<(205, 205, 205)):
                im.putpixel((x, y), (185, 122, 87))  # bruin # ook interessant
            elif (9 < absaftrek6 < 90 and im.getpixel((x, y)) < (175, 175, 175)):
                im.putpixel((x, y), (0, 255, 0) )  # felgroen
            elif(im.getpixel((x,y)) <(112,112,112)):
                im.putpixel((x, y), (255, 128, 0))  # feloranje #beetje interessant
            elif(10<naburig34<30 and im.getpixel((x,y)) <(145,145,145) and help12[0]<145 and help22[0]<145 and help121[0] <140 and help221[0]<140 ):
                im.putpixel((x, y), (255, 128, 255) )  # roze
                #nog proberen tss rechts en links zoveel tss en minimum zoveel als pixelwaarde voor x+2

            elif (verschiltellertjes>0.8 and iets[0]<115 and help32[0] <115 ): #and help221[0]<113 and help121[0]<113 and help2[0]<113):
                im.putpixel((x, y),(0, 162, 232)) #blauw
                #print("x,y baluw ", x, y)  #
    #       #elif(7 < absaftrek62 < 90 and im.getpixel((x, y)) < (135, 135, 135) and help31[0]<135 and help33[0]<135 and help121[0]<135 and help221[0]<135
    #         #and helpme1[0] < 137 and helpme2[0]<137  and helpme3[0]< 137 and helpme4[0]< 137 ):
                #im.putpixel((x, y), (219,114,36))# oranjebruin
            #elif(ja[len(ja)-1]==(132 or 131 or 130 or 129 or 128)):
               #im.putpixel((x, y), (255, 128, 255) )  # roze

            #elif(absaftrek6 >5 and (absaftrek2 >8 or absaftrek3 >8 or absaftrek4>8 or absaftrek5> 8) and iets[0]<145):
                #im.putpixel((x, y), (255,128,64))  # oranjeroze
            #elif (abs(iets[0] -help5[0]) > 6 and help5[0]<140 and iets[0]<140 and im.getpixel((x+5, y))<(140,140,140)):
                #im.putpixel((x+5, y), (255,128,64))  # oranjeroze
            #elif(abs(help12[0] -iets[0]) > 1 and im.getpixel((x+10, y))<(120,120,120)):
                #im.putpixel((x + 10, y), (255, 128, 64))  # oranjeroze
            """elif(10<absaftrek3<20): #waar vleesje zit
                    im.putpixel((x, y), (255, 242, 0) and im.getpixel((x,y)) <(180,180,180))  #geel
                elif(10<absaftrek5<20):
                    im.putpixel((x, y), (255, 128, 255) and im.getpixel((x,y)) <(180,180,180))  #roze
            elif(10 < absaftrek6< 90):
                    im.putpixel((x, y), (0, 255, 0) and im.getpixel((x,y)) <(180,180,180))  #felgroen
                elif (10 < absaftrek7 < 20):
                    im.putpixel((x, y), (128, 255, 255))  #felblauw
                elif(10 < absaftrek8 <20):
                    im.putpixel((x, y), (255,128,0))  #feloranje
                elif ( 15<absaftrek9 < 30):
                    im.putpixel((x, y), (185, 122,87))  #bruin
                    #else:
                    #im.putpixel((x, y), (0, 162, 232)) #blauw"""
            #andere algoritme bedenken want pixelwaarde donkere vlekken vlees egven probleem, figuur patroon
            #probleem weinig verschil tussen naburige pixelwaarden en te lage grijswaarde

    im.show()
    im.save('./images/bewerkteknipie.PNG')
def find_all_coordinates(path):
    with Image.open(path) as im:
        width = im.size[0] - 10
        height = im.size[1] - 10
        for x in range(1, width):
            for y in range(1, height):
                jah1 = im.getpixel((x, y))
                if(jah1[0] != jah1[1]and jah1[1] != jah1[2] and jah1[0] != jah1[2]):
                    im.putpixel((x,y), (237, 28, 36)) #rood
    im.show()
    im.save('./images/bewerkteknipierood.PNG')

def find_cut_coordinates(path):
    #moving window slider
    with Image.open(path) as im:
        print("fuck you")
        width = im.size[0] - 10
        height = im.size[1] - 10
        for x in range(20,width):
            for y in range(20, height):
                k = 0
                for i in range(-9,9):
                    for j in range(-9,9):
                        #te groot maken te veel (dik zwart)
                        jah0 = im.getpixel((x+i, y+j))
                        if(jah0==(237, 28, 36,255) or jah0==(255, 128, 255,255) or jah0==(0, 255, 0,255)):
                            k=k+1
                            if(k>=7):
                                #te veel blokjes
                                im.putpixel((x,y),(0,0,0))

    im.show()
    im.save('./images/bewerkteknipiezwart.PNG')
def find_cut_coordinates2(path):
    print("fuck you too")
    with Image.open(path) as im:
        width = im.size[0] - 10
        height = im.size[1] - 10
        for x in range(20, width):
            for y in range(20, height):
                manneke= im.getpixel((x,y))
                manneke1= im.getpixel((x+1,y))
                manneke2= im.getpixel((x-1,y))
                manneke3= im.getpixel((x,y+1))
                manneke4= im.getpixel((x,y-1))


                if ( manneke == (0,0,0,255) and manneke4 !=(0,0,0,255) and manneke4 != (0, 255, 255,255) and manneke4 != (136, 0, 21,255) and manneke4 !=(255, 0, 128) and manneke4 != (163, 73, 174) ):

                        im.putpixel((x, y-4), (163, 73, 174)) #paars
                if ( manneke == (0,0,0,255) and manneke3 != (0, 0, 0, 255) and manneke3 != (0, 255, 255,255) and manneke3 != (136, 0, 21,255) and manneke3 !=(255, 0, 128) and manneke3 != (163, 73, 174)):
                    im.putpixel((x, y + 4), (136, 0, 21))  # purper
                if (  manneke == (0,0,0,255) and manneke2 != (0, 0, 0, 255) and manneke2 != (136, 0, 21,255) and manneke2 != (163, 73, 174,255)  and manneke2 !=(255, 0, 128) and manneke4 != (0, 255, 255,255)):

                    im.putpixel((x-4, y ), (255, 0, 128))  # roze
                if ( manneke == (0,0,0,255) and manneke1 != (0, 0, 0, 255) and  manneke1 != (0, 255, 255,255) and manneke1 != (136, 0, 21,255) and manneke1 !=(255, 0, 128) and manneke1!= (163, 73, 174)):
                    im.putpixel((x+4, y), (0, 255, 255))  # lichtblauw
    im.show()
    im.save('./images/bewerkteknipieranden.PNG')
def find_cut_coordinates3(path):
    print("fuck you too too")
    with Image.open(path) as im:
        width = im.size[0] - 10
        height = im.size[1] - 10
        for x in range(20, width):
            for y in range(20, height):
                manneke = im.getpixel((x, y))
                manneke1 = im.getpixel((x + 1, y))
                manneke2 = im.getpixel((x - 1, y))
                manneke34 = im.getpixel((x, y + 4))
                manneke3 = im.getpixel((x-1, y + 4))
                manneke4 = im.getpixel((x+1, y + 4))
                if (manneke == (0,0,0,255) and manneke34 == (136, 0, 21,255) and manneke3 == (136, 0, 21,255) and manneke4 == (136, 0, 21,255)): #purper
                        im.putpixel((x, y + 4), (255,242,0))
    im.show()
    #im.save('./images/bewerkteknipieranden2.PNG')
    return np.float32(im)
def find_cut_coordinates_notblack_iswhite(path):
    print("black+white")
    with Image.open(path) as im:
        width = im.size[0]
        height = im.size[1]
        for x in range(0, width):
            for y in range(0, height):
                manneke = im.getpixel((x, y))

                if (manneke != (0,0,0,255)):
                        im.putpixel((x, y ), (255,255,255))
    im.show()
    im.save('./images/cornersinbw.PNG')
    print("cornersinbw gemaakt")
    return np.float32(im)
#takes the mean of two points
def midpoint(ptA,ptB):
    return (ptA[0]+ptB[0])*0.5, (ptA[1]+ptB[1])*0.5


def crop(x,y,h,w,path):
    image = cv2.imread(path)
    crop_image = image[ y:h,x:w]
    cv2.imshow("Cropped", crop_image)
    file_name =f'./cropped/crop_image_x{x}_y{y}_h{h}_w{w}.PNG'
    print("file_name",file_name)
    cv2.imwrite(file_name,crop_image)

    return file_name,x,y,h,w
def edit_cropped_images(path,x,y,h,w):
 with Image.open(path) as im:

        print("abs(x-w)",abs(x-w))
        print("abs(y - h)", abs(y - h))
        newhelp1 = abs(x - w) - 3
        newhelp2 = abs(y - h) - 2
        ja = []
        for a in range(0, newhelp1):
            for b in range(0, newhelp2):
                mimi = im.getpixel((a, b))
                ja += mimi
                ja.sort()
        average = sum(ja) / len(ja)
        print(len(ja),"len(ja)")
        print("len(ja)/2", (len(ja))/2)
        iets=len(ja)/2
        ietsint = int(iets)
        print(ja[ietsint], "ja[ietsint]")
        iets2 = len(ja) / 4
        ietsint2 = int(iets2)
        print(ja[ietsint2], "ja[ietsint2]")
        print("average",average)

        for c in range(2,newhelp1):
            for d in range(1,newhelp2):
                iets = im.getpixel((c, d))
                iets6 = im.getpixel((c, d + 1))
                aftrek6 = iets[0] - iets6[0]
                absaftrek6 = abs(aftrek6)
                help32 = im.getpixel((c + 2, d))
                help42 = im.getpixel((c - 2, d))
                help3242 = abs(help32[0] - help42[0])
                iets2 = im.getpixel((c, d))
                iets3 = im.getpixel((c-1, d ))
                aftrek4 = iets2[0] - iets3[0]
                absaftrek4 = abs(aftrek4)
                iets7 = im.getpixel((c, d))
                iets8 = im.getpixel((c -3, d))
                aftrek1 = iets7[0] - iets8[0]
                absaftrek1 = abs(aftrek1)
                iets61 = im.getpixel((c, d))
                iets62 = im.getpixel((c, d - 1))
                aftrek63 = iets61[0] - iets62[0]
                absaftrek64 = abs(aftrek63)
                width =abs(x-w)
                height = abs(y-h)
                if (ja[ietsint]>=145 ):
                    print("hierin4")
                    if(im.getpixel((c, d)) < (ja[ietsint2]+10,ja[ietsint2]+10,ja[ietsint2]+10)):
                        print("hierin5")
                        if (6 < absaftrek6 <90 ):
                            print("absaftrek6",absaftrek6)
                            print("absaftrek4", absaftrek4)
                            im.putpixel((c, d), (0, 45, 255)) #blauw
                            if( absaftrek4>2):
                                im.putpixel((c, d), (255, 128, 64)) #oranjeroze
                                if (absaftrek1 > 2):
                                    im.putpixel((c, d), (51, 204, 204))  # blauwgroen
                                    if (absaftrek64> 0):
                                        im.putpixel((c, d), (255, 12, 0))  # rood
                                        if (help3242 > 10):
                                            im.putpixel((c, d), (255, 204, 0))  # geel
                if (127<ja[ietsint]< 145 ):
                    print("hierin1")
                    if(im.getpixel((c, d)) < (ja[ietsint2]+5,ja[ietsint2]+5,ja[ietsint2]+5)):
                        print("hierin2")
                        print("absaftrek6 wat gebeurt", absaftrek6)
                        if (3< absaftrek6 <90 ):
                            print("absaftrek6",absaftrek6)
                            im.putpixel((c, d), (0, 255, 0)) #groen
                            if (absaftrek4 > 1 and im.getpixel((c, d)) < (ja[ietsint2],ja[ietsint2],ja[ietsint2]) ):
                                im.putpixel((c, d), (255, 128, 64))  # oranjeroze
                                if(absaftrek1 > 1 ):
                                    im.putpixel((c, d), (51, 204, 204))  # blauwgroen
                                    if (absaftrek64> 0):
                                        im.putpixel((c, d), (255, 12, 0))  # rood
                                        if (help3242 > 4):
                                            im.putpixel((c, d), (255, 204, 0))  # geel


                if (ja[ietsint] <= 127):
                    if (im.getpixel((c, d)) < (ja[ietsint] - 10, ja[ietsint] - 10, ja[ietsint] - 10)): #beetje meer toelaten
                        im.putpixel((c, d), (255, 12, 0)) #rood
            """if (160<average<180 and height>width ):
                    print("if1")
                    im.getpixel((c, d)) >= (120, 120, 120) and im.getpixel((c, d)) <= (135, 135, 135)
                    im.putpixel((c, d), (255, 128, 255))  # roze
                if (150<average<170 and width >height ):
                    print("if2")
                    newhelp3 = abs(x - w)-6
                    newhelp4 = abs(y - h)-6
                    for a in range(0, newhelp3):
                        for b in range(0, newhelp4):
                            help121 = im.getpixel((a, b + 4))
                            help221 = im.getpixel((a, b - 4))
                            help121221 = abs(help121[0] - help221[0])
                    if(im.getpixel((c, d)) <= (119, 119, 119)):
                       im.putpixel((c, d), (255, 128, 255))  # roze

                    elif (im.getpixel((c, d)) <= (121, 121, 121) and help121221 > 10 and help121[0] < help221[0]):
                        im.putpixel((c, d), (0, 0, 255))  # blauw
                if (140 < average < 160 and height>width):
                    print("if3")
                    newhelp3 = abs(x - w) - 6
                    newhelp4 = abs(y - h) - 6
                    for a in range(0, newhelp3):
                        for b in range(5, newhelp4):

                            help121 = im.getpixel((a, b + 4))

                            help221 = im.getpixel((a, b - 4))
                            help121221 = abs(help121[0] - help221[0])
                    if (im.getpixel((c, d)) <= (113, 113, 113)):
                        im.putpixel((c, d), (255, 128, 255))  # roze
                    elif (im.getpixel((c, d)) <= (121, 121, 121)): #and help121221 > 10 and help121[0] < help221[0]):
                        im.putpixel((c, d), (0, 0, 255))  # blauw
                if(190 < average < 210 and width > height):
                    print("if4")
                    newhelp1 = abs(x - w) - 3
                    newhelp2 = abs(y - h) - 2
                    for a in range(2,newhelp1):
                        for b in range(0, newhelp2):
                            help32 = im.getpixel((a + 2, b))
                            help42 = im.getpixel((a - 2, b))
                            help3242 = abs(help32[0] - help42[0])
                    if (im.getpixel((c, d)) <= (165, 165, 165)):
                        im.putpixel((c, d), (255, 128, 255))  # roze
                    elif (im.getpixel((c, d)) <= (180, 180, 180) and help3242 > 10 and help32[0] > help42[0]):
                        im.putpixel((c, d), (0, 0, 255))  # blauw
                    elif (im.getpixel((c, d)) <= (180, 180, 180) and help3242 > 10 and help32[0] > help42[0] and help32[0] < 190 and
                         help42[0] < 190):
                            im.putpixel((c, d), (0, 255, 0))  # groen
                if (120 < average < 160 and height > width):
                        print("if5")
                        newhelp3 = abs(x - w) - 6
                        newhelp4 = abs(y - h) - 6
                        for a in range(0, newhelp3):
                            for b in range(5, newhelp4):
                                help121 = im.getpixel((a, b + 4))

                                help221 = im.getpixel((a, b - 4))
                                help121221 = abs(help121[0] - help221[0])
                        if (im.getpixel((c, d)) <= (113, 113, 113)):
                            im.putpixel((c, d), (255, 128, 255))  # roze
                        elif (im.getpixel((c, d)) <= (
                        121, 121, 121)):  # and help121221 > 10 and help121[0] < help221[0]):
                            im.putpixel((c, d), (0, 0, 255))  # blauw
                if (125 < average < 160 and height>width):
                    print("if6")
                    newhelp3 = abs(x - w) - 6
                    newhelp4 = abs(y - h) - 6
                    for a in range(0, newhelp3):
                        for b in range(5, newhelp4):

                            help121 = im.getpixel((a, b + 4))

                            help221 = im.getpixel((a, b - 4))
                            help121221 = abs(help121[0] - help221[0])
                    if (im.getpixel((c, d)) <= (113, 113, 113)):
                        im.putpixel((c, d), (204, 204, 255))  # lila
                    elif (im.getpixel((c, d)) <= (121, 121, 121)): #and help121221 > 10 and help121[0] < help221[0]):
                        im.putpixel((c, d), (0, 0, 255))  # blauw
                    """

 file_name =f'./croppedprobeersel/crop_image_canny_x{x}_y{y}_h{h}_w{w}.PNG'

 im.show('im edited crop')
 im.save(file_name)
 return file_name, x, y, h, w
def convexhull():
    convexHull = cv2.convexHull(c)
    hull = cv2.arcLength(convexHull, True)
    return hull,convexHull
def paste_images_back(path,x,y,h,w,testimage): #niet in gebruik
    cutted_and_worked_on = cv2.imread(path)
    print()
    testimage[y:h, x:w] = cutted_and_worked_on
    cv2.imshow('probeersel', testimage)
    file_name = f'./croppedprobeersel/readyfordrawline_paste.PNG'
    cv2.imwrite(file_name,testimage)
    return file_name
def Lines_on_original(path,path_original):
    with Image.open(path_original) as im2:
        with Image.open(path) as im:
            width = im.size[0]
            height = im.size[1]

            for x in range(1, width):
                for y in range(1, height):
                    if (im.getpixel((x,y))==(255,0,0)):
                             im2.putpixel((x,y),(255,0,0))
    im.show(im2)
    file_name = f'./croppedprobeersel/readyfordrawline_on_original.PNG'
    im2.save(file_name)
def helpmemaar(path):
    with Image.open(path) as im:
        width = im.size[0]
        height = im.size[1]
        for x in range(0, width):
            for y in range(0, height):
                oldpixel = im.getpixel((x, y))
                brightness =1
                if(oldpixel>= (90, 90,90)):
                    oldpixel0 = oldpixel[0]
                    oldpixel1= oldpixel[1]
                    oldpixel2 = oldpixel[2]
                    oldpixel11 =int( oldpixel0 * brightness)
                    oldpixel21 = int(oldpixel1 * brightness)
                    oldpixel31 =int(oldpixel2 * brightness)
                    newpixel = int(oldpixel11),int( oldpixel21),int(oldpixel31)
                    newpixelcolor =(255,0,0)
                    im.putpixel((x, y),newpixelcolor)
    im.show(im)
    file_name = f'./dual/dual11.tif'
    im.save(file_name)
if __name__ == "__main__":
        #https://stackoverflow.com/questions/39308030/how-do-i-increase-the-contrast-of-an-image-in-python-opencv
        imn  = cv2.imread('./images/3eba5c3a-7261-4cfc-844c-8613afa5780d_RawData_RawData.tif')
        cv2.imshow('imn', imn)
        imnbil = cv2.bilateralFilter(imn,2, 75, 75)
        cv2.imshow("imnbil", imnbil)
        # converting to LAB color space
        lab = cv2.cvtColor(imnbil, cv2.COLOR_BGR2LAB)
        l_channel, a, b = cv2.split(lab)

        # Applying CLAHE to L-channel
        # feel free to try different values for the limit and grid size:
        clahe = cv2.createCLAHE(clipLimit=6.0, tileGridSize=(4, 4))
        cl = clahe.apply(l_channel)

        # merge the CLAHE enhanced L-channel with the a and b channel
        limg = cv2.merge((cl, a, b))

        # Converting image from LAB Color model to BGR color spcae
        enhanced_img = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

        # Stacking the original image with the enhanced image
        result = np.hstack((imn, enhanced_img))
        cv2.imshow('enhanced_img',enhanced_img )
        x= imn.shape[0]
        print( "x",x)
        y = imn.shape[1]
        print("y", y)
        ydeel2 =int(y/2)
        print("ydeel2", ydeel2)
        crop_image = imn[0:x, 0:ydeel2]
        crop_image2 = imn[0:x, ydeel2:y]
        cv2.imshow("Cropped", crop_image)
        cv2.imshow("Cropped2", crop_image2)
        file_name = f'./dual/dual1.tif'
        cv2.imwrite(file_name, crop_image2)
        helpmemaar(file_name)
        helpme= cv2.imread('./dual/dual11.tif')
        x2 = helpme.shape[0]
        y2 = helpme.shape[1]
        helpme2 = helpme[0:x2, 0:y2]
        fig, (ax0,ax1) = plt.subplots(nrows=1, ncols=2)
        xje =[]
        for manneke in range (0,255,10):
            xje.append(manneke)
        print("xje",xje)
        plt.xticks(xje)
       
        ax0.hist((crop_image.ravel(),crop_image2.ravel(),helpme2.ravel()),256,[0,256])
        ax1.hist((helpme2.ravel()), 256, [0, 256])
        bewerkteLEdeelHE = (crop_image / crop_image2)  #LE/HE
        #cv2.imshow("bewerkteLEdeelHE", bewerkteLEdeelHE)
        momentofondergang= crop_image-helpme2
        #cv2.imshow("momentofondergang", momentofondergang)
        plt.show()

        """
        crop_image2bil = cv2.bilateralFilter(crop_image2, 3, 125, 125)
        cv2.imshow("Cropped2bil", crop_image2bil)
        crop_imagebil = cv2.bilateralFilter(crop_image, 3, 125, 125)
        cv2.imshow("Croppedbil", crop_imagebil)
        """

        cv2.waitKey()
        path = "./images/knipie2.PNG"
        findpixels(path)
        print("ik ben hier")
        find_all_coordinates("./images/bewerkteknipie.PNG")
        print("ik ben hier2")
        find_cut_coordinates("./images/bewerkteknipierood.PNG")
        print("ik ben hier niet geraakt")
        #find_cut_coordinates2("./images/bewerkteknipiezwart.PNG")
        #print("k ben hier niet geraakt")
        #testje =find_cut_coordinates3("./images/bewerkteknipieranden.PNG")
        find_cut_coordinates_notblack_iswhite("./images/bewerkteknipiezwart.PNG")
        print("imi")

        #crop(0,0,300,510)
        #load the image
        testimage = cv2.imread(path)
        testimage2 =testimage.astype(np.uint8)
        testimage3 = cv2.cvtColor( testimage2, cv2.COLOR_BGR2GRAY)
        testimage4 = np.float32(testimage3)
        #animetestimage = cv2.imread('./croppedprobeersel/crop_image_canny_x83_y168_h254_w153.PNG')
        print("help")
        path2 ='./images/cornersinbw.PNG'
        image = cv2.imread(path2)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        gray_gb = cv2.GaussianBlur(gray,(7,7),0) # ==> niet blurren of enkel blurren om dan weer pixels af te trekken
        #lus maken met alle pixels en hun waardes
        #edges = None
        edged = cv2.Canny(gray,20, 100)
        #edgedcorner = cv2.cornerHarris(testimage4, 2,1,0.04)
        print("helpmemore1")
        cv2.imshow('edged',edged)
        print("helpmemore")
        #edged = cv2.Canny(gray,150,255) #hier nog iets doen ==> verschil in naburige pixel waarden?
        edged_d = cv2.dilate(edged, None, iterations=1)
        edged_e = cv2.erode(edged, None, iterations=1)
        #ret, thresh = cv2.threshold(testimage, 120, 240, cv2.THRESH_BINARY_INV)
        #src, thresh, maxval
        # 150 als pixel groter is dan 100 anders 0
        #th2 = cv2.adaptiveThreshold(testimage3, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 2)
        #th3 = cv2.adaptiveThreshold(testimage3, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  cv2.THRESH_BINARY, 5, 2)

        ##cv2.imshow( )
        #cv2.imshow('th3', th3)

        #show result
        rsize = 1
        result1 =np.concatenate((cv2.resize(image[:, :,0],(0,0),None,rsize,rsize),
                                cv2.resize(gray, (0,0), None, rsize, rsize),
                                cv2.resize(gray_gb, (0, 0), None, rsize, rsize)),axis=1)

        result2 = np.concatenate((cv2.resize(edged, (0, 0), None, rsize, rsize),
                                 cv2.resize(edged_d, (0, 0), None, rsize, rsize),
                                 cv2.resize(edged_e, (0, 0), None, rsize, rsize)), axis=1)
        result = np.concatenate((result1,result2),axis=0)
        print("mimimi")
        cv2.imshow('result',result)
        print("result")

        cnts,hier = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        print(cnts[2])
        cv2.drawContours(image,cnts, -1, (255, 128, 255), 1)#roze
        cv2.imshow('image',image )
        #cnts = imutils.grab_contours(cnts)

        print("\nContours shape: " + str(np.shape(cnts)))
        print("First contour shape: " + str(np.shape(cnts[0])))


        (cnts, _) = contours.sort_contours(cnts, method="left-to-right")

        pixelsPerMetric = None
        for c in cnts:
            perimeter = cv2.arcLength(c, True)
            hull,convexHull=convexhull()
            print("perimeter", perimeter)
            print("hull", hull)
            if (perimeter <105 or hull<110) :#if cv2.contourArea(c) < 105:
               print("perimeter continue", perimeter)
               print("hull continue", hull)
               continue
            cv2.drawContours(image, c, -1, (255, 128, 255), 4)  # roze
            testje = cv2.drawContours(image, [convexHull], -1, (0, 0, 255), 2)

            # Display the final convex hull image
            cv2.imshow('ConvexHull', image)
            cv2.imshow('testje', testje)
            file_name = f'./croppedprobeersel/readyfordrawline.PNG'
            cv2.imwrite(file_name, testje)
            Lines_on_original(file_name, path)

            papa = cv2.imread("./croppedprobeersel/readyfordrawline.PNG")
            cnts, hier = cv2.findContours(papa, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            convexhulll = cv2.convexHull(cnts)
            testje2 = cv2.drawContours(papa, [convexhulll], -1, (0, 255, 0), 2)
            cv2.imshow('testje2', testje2)

            print("hull groter dan 75:", hull )
            orig = image.copy()
            box = cv2.minAreaRect(c)
            print("box",box)
            print("box[1]", box[1])
            if (box[1][0] < 5 or box[1][1]<5 ):
                print("box[1][0]",box[1][0]," box[1][1]", box[1][1])
                continue
            box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
            box = np.array(box, dtype ="int")

            print("\nBounding box corner coordinates")
            print(box)
            croppath,x,y,h,w = crop(box[0][0]-2,box[1][1]-2,box[3][1]+2,box[2][0]+2,path)
            print("aub")
            #croppath2, x, y, h, w = edit_cropped_images(croppath,x,y,h,w)
            print("aub2")
            #piepje2,x,y,h,w = last_file_not_black_is_white(croppath2,x,y,h,w)
            #piepje=paste_images_back(croppath2,x,y,h,w,testimage)
            print("aub3")

            #draw_cutting_line(piepje2)


            print("\nBounding box corner ordered coordinates")
            print(box)


            cv2.drawContours(orig, [box.astype("int")], -1, (0,255,0), 2)
            cv2.imshow('Result1', orig)


            # Loop over the original points and draw them

            for (x, y) in box:
                cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)
            cv2.imshow('Result2', orig)


            (t1, tr, br, bl) = box
            (tltrx, tltry) = midpoint(t1, tr)
            (blbrx, blbry)= midpoint(bl, br)

            (tlblx, tlbly) = midpoint(t1, bl)
            (trbrx, trbry) =  midpoint(tr, br)

            cv2.circle(orig, (int(tltrx), int(tltry)), 5, (255, 0, 0), -1)
            cv2.circle(orig, (int(blbrx), int(blbry)), 5, (255, 0, 0), -1)
            cv2.circle(orig, (int(tlblx), int(tlbly)), 5, (255, 0, 0), -1)
            cv2.circle(orig, (int(trbrx), int(trbry)), 5, (255, 0, 0), -1)
            cv2.imshow('Result3', orig)



            # compute the Euclidean distance between the midpoints

            dA = dist.euclidean((tltrx, tltry), (blbrx, blbry))
            dB = dist.euclidean((tlblx, tlbly), (trbrx, trbry))

            # if the pixels per metric has not been initialized, then

            # compute it as the ratio of pixels to supplied metric
            if pixelsPerMetric is None:
                pixelsPerMetric = dB / 24.25700
                print("\nPixels per metric + str(pixelsPerMetric)")

            # compute the size of the object
            dimA = dA / pixelsPerMetric
            dimB = dB / pixelsPerMetric

            cv2.putText(orig, "{:.1f}mm".format(dimA),

            (int(tltrx - 15), int(tltry - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)
            cv2.putText(orig, "{:.1f}mm".format(dimB),
            (int(trbrx + 10), int(trbry)), cv2.FONT_HERSHEY_SIMPLEX,0.65, (255, 255, 255), 2)

            cv2.imshow("Image", orig)
