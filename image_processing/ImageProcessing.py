import pytesseract as OCR
from config import Globals
from PIL import Image, ImageEnhance

def CropImage(inputImage):
    # Get Image Size
    _, inputImageHeight = inputImage.size
    
    # Crop Image
    outputImage = inputImage.crop((0, 0, 600, inputImageHeight))

    return outputImage

def ScaleImage(inputImage):
    # Get Image Size
    inputImageWidth, inputImageHeight = inputImage.size 

    # Create a White Canvas
    canvas = Image.new('RGB', (1080, 1080), 'white')

    # Reduce Input Image
    inputImageWidthReduced = int(inputImageWidth/5)                                                             
    inputImageHeightReduced = int(inputImageHeight/5)
    inputImageResized = inputImage.resize((inputImageWidthReduced, inputImageHeightReduced))

    # Get Canvas Size
    canvasWidth, canvasHeight = canvas.size

    # Calculating Image Offset
    imageBorderOffset = (int((canvasWidth-inputImageWidthReduced)/2),int((canvasHeight-inputImageHeightReduced)/2))

    # Pasting Image To Canvas
    canvas.paste(inputImageResized, imageBorderOffset)

    outputImage = canvas

    return outputImage

def ImagePreProcess(pdfCurrentPageImage):
    # Increase Image Contrast
    pdfCurrentPageImage = ImageEnhance.Contrast(pdfCurrentPageImage).enhance(Globals.imgContrastEnhanceFactor)

    # Increase Image Sharpness
    pdfCurrentPageImage = ImageEnhance.Sharpness(pdfCurrentPageImage).enhance(Globals.imgSharpnessEnhanceFactor)

    # Convert Image To Grayscale
    pdfCurrentPageImage = pdfCurrentPageImage.convert('L')

    # Correct Image Orientation
    angle = OCR.image_to_osd(pdfCurrentPageImage)
    angle = angle.split("\n")
    rot = [int(i) for i in angle[2].split() if i.isdigit()]
    pdfCurrentPageImage = pdfCurrentPageImage.rotate(rot[0],expand = True)

    # Return Pre-Processed Image
    return pdfCurrentPageImage