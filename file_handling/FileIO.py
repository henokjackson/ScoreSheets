import csv
import PyPDF2
import pdf2image
from config import Globals
from text_processing.TextProcessing import TextExtract
from image_processing.ImageProcessing import ImagePreProcess
from score_calculation.ScoreCalculation import GetCourseDuration


def CSVWriter():
    # Setting CSV File Columns Names
    csvColumns = ['Name','Course Type','Duration','Current Score','Total Score']
    
    # Opening CSV File
    scoreSheetCsvFile = open(Globals.outputFolderParentPath + '/' + Globals.outputFolderName + "/" + Globals.outputFileName + ".csv", "a+")
    scoreSheetCsvFileWriter = csv.DictWriter(scoreSheetCsvFile, fieldnames = csvColumns)

    # Writing CSV Header
    if not Globals.isCsvHeaderWritten:
        scoreSheetCsvFileWriter.writeheader()
        Globals.isCsvHeaderWritten = True
    
    # Calculating Total SCore
    for data in Globals.currentPdfDataList:
        if (Globals.isMarksCustomized):
            data["Total Score"] = data["Current Score"]
        else:
            # Checking Total Score Restriction
            if (data["Current Score"] >= Globals.maximumScoreThreshold):
                data["Total Score"] = data["Current Score"]
                data["Current Score"] = Globals.maximumScoreThreshold
            else:
                data["Total Score"] = data["Current Score"]
        # Writting Data To CSV
        scoreSheetCsvFileWriter.writerow(data)

def PDFDataExtract():
    # Setting Up PDF Reader
    pdfReader = PyPDF2.PdfReader(open(Globals.sourceFolderPath + '/' + Globals.pdfFileName, mode = "rb"), strict = False)

    # Converting All Pages of PDF To List of Images
    pdfPagesImgList = pdf2image.convert_from_path(Globals.sourceFolderPath + '/' + Globals.pdfFileName, thread_count = Globals.noOfThreads, dpi = Globals.pdfDPI, strict = False)

    # Processing Each Page
    for pdfCurrentPageNumber, pdfCurrentPageImage in enumerate(pdfPagesImgList,1):

        # Checking For First-Page and Last-Page
        if pdfCurrentPageNumber == len(pdfReader.pages) or pdfCurrentPageNumber == 1:

            # Pre-Processing The Image
            preprocessedpdfCurrentPageImage = ImagePreProcess(pdfCurrentPageImage)

            # Extract Info From First-Page
            if pdfCurrentPageNumber == 1: TextExtract(preprocessedpdfCurrentPageImage)

            # Extract Info From Last-Page
            elif pdfCurrentPageNumber == len(pdfReader.pages): GetCourseDuration(preprocessedpdfCurrentPageImage)