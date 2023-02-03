import os                                                                                               # LIBRARY FOR FOLDER OPERATIONS
from vars import *                                                                                      # MODULE CONTAINING GLOBAL VARIABLES
from GUI.Dashboard import MENU,PROGBAR                                                                  # IMPORTING GUI ELEMENTS
from Score_Calculation.Score_Calc import CustomizeMarks,Path                                            # LIBRARY FOR SCORE CALCULATION FUNCTIONS
from Text_Processing.TextProcess import PDFExtract,MERGE_DUPLICATES,DICT_TO_CSV                         # LIBRARY FOR TEXT PROCESSING FUNCTIONS

def WORKSPACE(outpath):                                                                                 # WORKSPACE SETUP FUNCTION
    os.makedirs(outpath+"\\data")                                                                       # MAKING FOLDER CALLED Data FOR STORING ALL THE PROGRAM DATA

def main():
    MENU()                                                                                              # CALLING PROGRAM INTERFACE FUNCTION
    global srcpath,outpath,courselistpath,namelistpath,filename,details                                 # REFFERING ALL GLOBAL FOLDER AND FILE PARAMETERS
    """
    global week12_marks, week6_marks, week3_marks, week2_marks, week1_marks                             # GLOBAL VARIABLE FOR MARKS

    week1_marks=3                                                                                       # DEFAULT MARKS FOR WEEKS
    week2_marks=6
    week3_marks=12
    week6_marks=25
    week12_marks=50
    """
    srcpath=input("\nENTER THE SOURCE FOLDER PATH : ")
    outpath=input("ENTER THE WORKSPACE FOLDER PATH : ")
    courselistpath=input("ENTER COURSE NAME LIST FILE PATH : ")
    namelistpath=input("ENTER NAME LIST FILE PATH : ")                                                  # ALLOCATING CUSTOM MARKS
    for count,filename in enumerate(os.listdir(srcpath),1):                                             # READING ALL FILES IN WORKSPACE FOLDER
        PROGBAR(count,len(os.listdir(srcpath)))                                                         # CALLING PROGRESS BAR  ->GUI
        ext=(Path(filename).suffix).lower()                                                             # GETTING FILE EXTENSION
        if ext=='.pdf':                                                                                 # FOR .PDF EXTENSION                                           
            PDFExtract()                                                                                # PDF EXTRACTING FUNCTION
        MERGE_DUPLICATES()                                                                              # FUNCTION TO MERGE VALUES UNDER DUPLICATE NAMES
        details={}                                                                                      # FLUSH OUT DICT AFTER EVERY FILE READ
    WORKSPACE(outpath)                                                                                  # CALLING WORKSPACE SETUP FUNCTION
    DICT_TO_CSV()                                                                                       # FUNCTION TO WRITE DICT TO CSV

if __name__ == "__main__":                                                                              # CALLING MAIN FUNCTION
    main()
