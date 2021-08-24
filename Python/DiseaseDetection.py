import cv2 as cv
import sys
import  tkinter
from tkinter import filedialog

def ProcessImage(self):
    OriginalImage = cv.imread(filename, 1)
    cv.imshow("Original Image", OriginalImage)
    b = OriginalImage[:, :, 0]
    g = OriginalImage[:, :, 1]
    r = OriginalImage[:, :, 2]
    cv.imshow("Red Channel", r)
    cv.imshow("Green Channel", g)
    cv.imshow("Blue Channel", b)
    
    Disease = r -g
    global Alpha
    Alpha =b
    GetAlpha(OriginalImage)
    cv.imshow("Alpha Channel", Alpha)
    ProcessingFactor = S.get()
    for i in  range(0, OriginalImage.shape[0]):
        for j in range(0, OriginalImage.shape[1]):
            if int(g[i,j]) > ProcessingFactor:
                Disease[i,j] = 255
    cv.imshow("Disease Image", Disease)
    DisplayDiseasePercentage(Disease)
    S.bind('<ButtonRelease-1', ProcessImage)
    MainWindow.mainloop()
    
def GetAlpha(OriginalImage):
    global Alpha
    for i in range(0, OriginalImage.shape[0]):
        for j in range(0, OriginalImage.shape[1]):
            if OriginalImage[i,j,0]> 200 and OriginalImage[i,j,1]  > 200 and OriginalImage[i, j, 2] > 200:
                Alpha[i,j] > 255
            else:
                Alpha[1,j]  =  0
                

def GetFile():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return filedialog.askopenfilename(title= "Select Image")
    
    
def DisplayDiseasePercentage(Disease):
    Count = 0
    Res = 0
    for i in range( 0, Disease.shape[0]):
        for j in  range( 0, Disease[1]):
            if Alpha[i,j] == 0:
                Res += 1
            if Disease[i, j] < S.get():
                Count += 1
    Percent = (Count / Res) * 100
    DiseasePercent.set("Percentage DIsease: " + str(round(Percent, 2)) + "%")
    

Alphaa = None
MainWindow = tkinter.Tk()
MainWindow.title("Plant Disease Detector")

S = tkinter.Scale(MainWindow, from_=0, to=255, length=500, orient=tkinter.HORIZONTAL,
                  background='white', fg='black', troughcolor='white', label="Processing Factor")

S.pack()
S.set(150)

DiseasePercent = tkinter.StringVar()
L = tkinter.Label(MainWindow, textvariable= DiseasePercent)
L.pack

filename = GetFile()

if filename != "":
    ProcessImage(None)
    
else:
    print("No File!")
    exit(0)