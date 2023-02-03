import pytesseract as OCR                                                                               # LIBRARY FOR OCR
from PIL import Image,ImageEnhance                                                                      # LIBRARY FOR IMAGE PROCESSING

def CROP_IMAGE(img):                                                                                    # IMAGE CROPPING
    img_w,img_h=img.size
    return img.crop((0,0,600,img_h))                                                                    # RETURNING PIL OBJECT OF CROPPED IMAGE

def SCALE_IMAGE(img):                                                                                   # IMAGE SCALING FUNCTION
    img_w,img_h=img.size                                                                                # DETERMINE IMAGE SIZE
    bg=Image.new('RGB',(1080,1080),'white')                                                             # CREATE WHITE BACKGROUND
    img_w=int(img_w/5)                                                             
    img_h=int(img_h/5)
    img=img.resize((img_w,img_h))                                                                       # RESIZE THE IMAGE BY A FACTOR OF 10
    bg_w,bg_h=bg.size                                                                                   # DETERMINE BACKGROUND IMAGE SIZE
    offset=(int((bg_w-img_w)/2),int((bg_h-img_h)/2))                                                    # CALCULATE OFFSET
    bg.paste(img,offset)                                                                                # PASTE RESIZED IMAGE TO WHITE BACKGROUND
    return bg

def ImageProcess(img):
    img=ImageEnhance.Contrast(img).enhance(1.5)                                                         # INCREASE IMAGE CONTRAST
    img=ImageEnhance.Sharpness(img).enhance(2)                                                          # INCREASE IMAGE SHARPNESS
    img=img.convert('L')                                                                                # CONVERT TO GRAYSCALE
    angle=OCR.image_to_osd(img)
    angle=angle.split("\n")
    rot=[int(i) for i in angle[2].split() if i.isdigit()]
    img=img.rotate(rot[0],expand=True)                                                                  # ROTATE IMAGE
    return img