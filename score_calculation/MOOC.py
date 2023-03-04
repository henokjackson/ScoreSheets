from vars import *                                                                                      # MODULE CONTAINING GLOBAL VARIABLES
from pathlib import Path                                                                                # LIBRARY FOR READING FILE EXTENSION FROM PATH
import pytesseract as OCR                                                                               # LIBRARY FOR OCR
from image_processing.ImgProcess import CROP_IMAGE,SCALE_IMAGE                                          # LIBRARY FOR PERFORMING SPECIALIZED IMAGE PRE-PREOCESSING

week12_marks=0                                                                                          # GLOBAL WEEK POINT VARIABLES
week6_marks=0
week3_marks=0
week2_marks=0
week1_marks=0

def PointCalc(week):                                                                                    # POINT CALCULATOR
    points=0
    while(week>=12):
        points+=int(week12_marks)
        week-=12
    while(week>=6):
        points+=int(week6_marks)
        week-=6
    while(week>=3):
        points+=int(week3_marks)
        week-=3
    while(week>=2):
        points+=int(week2_marks)
        week-=2
    while(week>=1):
        points+=int(week1_marks)
        week-=1
    details["POINTS"]=points                                                                            # APPENDING POINT TO DICT


def READ_WEEKS(img):                                                                                    # WEEKS READING FUNCTION
    text=OCR.image_to_string(img,config='--psm 6')                                                      # SETTING PYTESSERACT TO psm6 CONFIGUTAION TO READ LARGE FONTS
    large=0
    for word in text:
        if word.isnumeric():                                                                            # CHECKING IF THE READ DATA CONTAINS A NUMBER (WEEK)
            if large<int(word):
                large=int(word)                                                                         # FINDING THE LARGEST NUMBER
    return large                                                                                        # RETURNING THE LARGEST NO.OF WEEKS

def WeekExtract(img):
    img=CROP_IMAGE(img) 
    img=SCALE_IMAGE(img)                                                                                # CALLING IMAGE SCALING FUNCTION   
    week=READ_WEEKS(img)                                                                                # CALLING WEEK READING FUNCTION
    details["DURATION"]=week                                                                            # APPENDING DURATION TO DICT
    PointCalc(week)                                                                                     # CALLING POINT CALCULATING FUNCTION