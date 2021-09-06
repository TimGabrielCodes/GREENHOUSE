import picamera
import tkinter as Tkinter
import time
from PIL import ImageTk, Image
from threading import Thread
import io
import sys

RQS_0=0
RQS_QUIT=1
RQS_CAPTURE=2
rqs=RQS_0

def camHandler():
    global rqs
    rqs = RQS_0
    
    camera = picamera.PiCamera()
    #stream = io.BytesIO()

    #set default
    camera.sharpness = 0
    camera.contrast = 0
    camera.brightness = 50
    camera.saturation = 0
    camera.ISO = 0
    camera.video_stabilization = False
    camera.exposure_compensation = 0
    camera.exposure_mode = 'auto'
    camera.meter_mode = 'average'
    camera.awb_mode = 'auto'
    camera.image_effect = 'none'
    camera.color_effects = None
    camera.rotation = 0
    # camera.rotation = 270
    camera.hflip = False
    camera.vflip = False
    camera.crop = (0.0, 0.0, 1.0, 1.0)
    #camera.resolution = (1024, 768)
    camera.resolution = (400, 300)
    #end of set default
    #camera.start_preview()

    while rqs != RQS_QUIT:
        if rqs == RQS_CAPTURE:
            print("Capture")
            rqs=RQS_0
            timeStamp = time.strftime("%Y%m%d-%H%M%S")
            jpgFile='/home/pi/Pictures/leafPictures/leaf_'+timeStamp+'.jpg'
            camera.resolution = (400, 400)    #set photo size
            camera.capture(jpgFile)
            camera.resolution = (400, 300)      #resume preview size
            labelCapVal.set(jpgFile)
        else:
            #set parameter
            camera.sharpness = scaleSharpness.get()
            camera.contrast = scaleContrast.get()
            camera.brightness = scaleBrightness.get()
            camera.saturation = scaleSaturation.get()
            camera.exposure_compensation = scaleExpCompensation.get()

            stream = io.BytesIO()
            camera.capture(stream, format='jpeg')
            stream.seek(0)
            tmpImage = Image.open(stream)
            tmpImg = ImageTk.PhotoImage(tmpImage)
            previewPanel.configure(image = tmpImg)
            #sleep(0.5)
                
    print("Quit")        
    #camera.stop_preview()
    
def startCamHandler():
    camThread = Thread(target=camHandler)
    camThread.start()

def quit():
    global rqs
    rqs=RQS_QUIT

    global tkTop
    tkTop.destroy()

def capture():
    global rqs
    rqs = RQS_CAPTURE
    labelCapVal.set("capturing")

tkTop = Tkinter.Tk()
tkTop.wm_title("Greenhouse Camera")
tkTop.geometry('800x500')

previewWin = Tkinter.Toplevel(tkTop)
previewWin.title('Preview')
previewWin.geometry('400x300')
previewPanel = Tkinter.Label(previewWin)
previewPanel.pack(side = "bottom", fill = "both", expand = "yes")

tkButtonQuit = Tkinter.Button(
    tkTop, text="Quit", command=quit)
tkButtonQuit.pack()

tkButtonCapture = Tkinter.Button(
    tkTop, text="Capture", command=capture)
tkButtonCapture.pack()

SCALE_WIDTH = 780;

labelCapVal = Tkinter.StringVar()
Tkinter.Label(tkTop, textvariable=labelCapVal).pack()

scaleSharpness = Tkinter.Scale(
    tkTop,
    from_=-100, to=100,
    length=SCALE_WIDTH,
    orient=Tkinter.HORIZONTAL,
    label="sharpness")
scaleSharpness.set(0)
scaleSharpness.pack(anchor=Tkinter.CENTER)

scaleContrast = Tkinter.Scale(
    tkTop,
    from_=-100, to=100,
    length=SCALE_WIDTH,
    orient=Tkinter.HORIZONTAL,
    label="contrast")
scaleContrast.set(0)
scaleContrast.pack(anchor=Tkinter.CENTER)

scaleBrightness = Tkinter.Scale(
    tkTop,
    from_=0, to=100,
    length=SCALE_WIDTH,
    orient=Tkinter.HORIZONTAL,
    label="brightness")
scaleBrightness.set(50)
scaleBrightness.pack(anchor=Tkinter.CENTER)

scaleSaturation = Tkinter.Scale(
    tkTop,
    from_=-100, to=100,
    length=SCALE_WIDTH,
    orient=Tkinter.HORIZONTAL,
    label="saturation")
scaleSaturation.set(0)
scaleSaturation.pack(anchor=Tkinter.CENTER)

scaleExpCompensation = Tkinter.Scale(
    tkTop,
    from_=-25, to=25,
    length=SCALE_WIDTH,
    orient=Tkinter.HORIZONTAL,
    label="exposure_compensation")
scaleExpCompensation.set(0)
scaleExpCompensation.pack(anchor=Tkinter.CENTER)

print("start camera")
startCamHandler()

Tkinter.mainloop()