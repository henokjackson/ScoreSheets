import csv
from curses import color_content                                                                        # LIBRARY FOR CSV FILE OPERTIONS
import spacy                                                                                            # LIBRARY FOR NLP
import string                                                                                           # LIBRARY FOR STRING OPERATIONS
import PyPDF2                                                                                           # LIBRARY FOR READING NO.OF PAGES IN A PDF
from Vars import *                                                                                      # MODULE CONTAINING GLOBAL VARIABLES
import multiprocessing                                                                                  # LIBRARY FOR GETTING CPU CORE COUNT
import pdf2image as PDF                                                                                 # LIBRARY FOR CONVERTING PDF TO IMAGE
import pytesseract as OCR                                                                               # LIBRARY FOR OCR
from nltk.corpus import stopwords                                                                       # LIBRARY FOR DETERMINING STOPWORDS FROM TEXT
from nltk.tokenize import word_tokenize                                                                 # LIBRARY FOR TOKENIZATION OF TEXT
from Score_Calculation.MOOC import WeekExtract                                                          # LIBRARY FOR SCORE CALCULATION FUNCTIONS
from Image_Pre_Processing.ImgProcess import ImageProcess

def TextProcess(text):
    remove=str.maketrans(string.punctuation, ' '*len(string.punctuation))   
    newtext=text.translate(remove)                                                                      # JUNK REMOVAL

    stop_words=set(stopwords.words("english"))                                                          # STOP WORDS LIST

    words=word_tokenize(newtext)                                                                        # TOKENIZE EACH WORD
    text_list=[]
    for word in words:
        if word not in stop_words:
            text_list.append(word)                                                                      # CREATE LIST OF WORDS AFTER REMOVING STOPWORDS

    refined_text=' '.join(text_list)                                                                    # CREATING CLEAN TEXT

    wordlist=refined_text.split()                                                                       # CREATING WORDLIST ? SAME AS TEXTLIST

    csvfile=open(courselistpath)                                                                        # CSV CONTIANS COURSE PROVIDER'S NAMES
    coursecsv=csv.reader(csvfile)

    course_type="NONE"                                                                                  # INITIAL COURSE TYPE IS NONE
    cat=[]                                                                                              # CSV HEADER : CATEGORY TEMP VARIABLE
    cat_index=-1
    row_flag=-1
    for row in coursecsv:
        if row_flag==-1:
            cat=row
            row_flag=1
        for word in row:
            for i in range(0,len(wordlist)):
                if(word.lower()==str(wordlist[i].lower())):
                    cat_index=row.index(word)
                    course_type=cat[cat_index]
                    break
    """
    for row in coursecsv:                                                                               # READING THE CSV COLUMN-WISE
        for i in range(0,len(wordlist)):
            if (str(row[0]).lower())==(str(wordlist[i]).lower()):                                       # CHECKING FOR COURSE NAME IN THE LIST AND CSV
                course_type="MOOC"                                                                      # SETTING COURSE TYPE
    """

    nlp=spacy.load("en_core_web_sm")                                                                    # LOADS ENGLISH ENTITIES
    text=nlp(refined_text)
    
    name="NO_NAME"                                                                                      # NAME_VARIABLES
    names=[]                                                                                            # CREATING NAME LIST

    for word in text.ents:                                                                              # CHECKING FOR ENTITIES
        if word.label_=="PERSON":                                                                       # CHECKING FOR PERSON ENTITY
            names.append(word.text)                                                                     # APPENDING NAME TO NAMES LIST

    csvfile=open(namelistpath)                                                                          # CSV CONTAINS STUDENT NAMES
    namecsv=csv.reader(csvfile)
    for row in namecsv:                                                                                 # READING THE CSV COLUMN-WISE
        for i in range(0,len(names)):
            if (str(row[0]).lower())==(str(names[i]).lower()):                                          # CHECKING IF NAME LIST CONTAIN ANY MATCHING ENTITY
                name=names[i]                                                                           # ASSINGING NAME
    if(name=="NO_NAME"):
        details["NAME"]="=HYPERLINK("+"\""+srcpath+"\\"+filename+"\""+",\"NO_NAME\""+")"                # GIVE FILE PATH AS HYPERLINK IN CASE OF NO_NAME
    else:
        details["NAME"]=name                                                                            # APPENDING NAME TO DICT
    details["COURSE TYPE"]=course_type                                                                  # APPENDING COURSE TYPE TO DICT
    return course_type

def TextExtract(img):
    text=OCR.image_to_string(img)                                                                       # IMAGE TO TEXT
    return TextProcess(text)


def PDFExtract():
    reader=PyPDF2.PdfFileReader(open(srcpath+"\\"+filename,mode="rb"),strict=False)                     # READING NO.OF PAGES OF A PDF
    pages=PDF.convert_from_path(srcpath+"\\"+filename,thread_count=multiprocessing.cpu_count(),dpi=200,strict=False)
    for pagecount,page in enumerate(pages,1):                                                           # CONVERSION OF PDF TO JPEG       
        if pagecount==reader.getNumPages() or pagecount==1:                       
            img=ImageProcess(page)                                                                      # IMAGE PROCESSING FUNCTION CALL                                                  
            if pagecount==1:                                                                            # CONDITION FOR SINGLE PAGED PDF OR FOR THE FIRST PAGE OF THE PDF
                course_type=TextExtract(img)                                                                        # EXTRACTING TEXT FROM IMAGE
            """
            elif pagecount==reader.getNumPages():                                                       # CONDITION FOR LAST PAGE OF PDF (CONTAINS WEEK INFORMATION) 
                WeekExtract(img)                                                                        # WEEK EXTRACTION FUNCTION CALL
            """
def MERGE_DUPLICATES():
    if not dictlist:
        dictlist.append(details)
    else:    
        flag=1
        for no,item in enumerate(dictlist,0):                                                           # ITERATING OVER EACH DICTIONARY FROM DICTLIST
            if(item["NAME"]==details["NAME"] and item["COURSE TYPE"]==details["COURSE TYPE"]):          # FOR SAME NAME AND COURSE TYPE MERGE POINTS
                details["POINTS"]+=item["POINTS"]                                                       # MERGING POINTS
                details["DURATION"]+=item["DURATION"]                                                   # MERGING WEEKS
                dictlist[no]=details                                                                    # APPENDING DICTIONARY TO LIST
                flag=0
                break
        if flag==1:
            dictlist.append(details)


def DICT_TO_CSV():                                                                                      # CONVERT DICT TO CSV
    columns=['NAME','COURSE TYPE','DURATION','POINTS','TOTAL']
    global csvflag
    with open(outpath+"\\Data\\CertificateDetails.csv",'a+') as csv_file:  
        writer=csv.DictWriter(csv_file,fieldnames=columns)                                              # IMPORTING CSV FILE AND SETTING FIELDS
        if csvflag!=1:                                                                                  # CHECKING FOR HEADER FLAG
            writer.writeheader()                                                                        # WRITING HEADER TO CSV
            csvflag=1                                                                                   # SETTING FLAG
        for data in dictlist:
            if (data["POINTS"]>=50):
                data["TOTAL"]=data["POINTS"]                                                            # ADDING TOTAL POINTS
                data["POINTS"]=50                                                                       # CUTTING OF POINTS ABOVE 50
            else:
                data["TOTAL"]=data["POINTS"]
            writer.writerow(data)                                                                       # WRITING DICTIONARY DATA INTO CSV