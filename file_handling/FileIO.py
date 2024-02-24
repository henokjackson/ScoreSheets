import csv
import PyPDF2
import pdf2image
from config import globals
from text_processing.TextProcessing import TextExtract
from image_processing.ImageProcessing import ImagePreProcess
from score_calculation.ScoreCalculation import GetCourseDuration


def CSVWriter():
    # Setting CSV File Columns Names
    csvColumns = ['Name','Course Type','Duration','Current Score','Total Score']
    
    # Opening CSV File
    scoreSheetCsvFile = open(globals.outputFolderParentPath + '/' + globals.outputFolderName + "/" + globals.outputFileName + ".csv", "a+")
    scoreSheetCsvFileWriter = csv.DictWriter(scoreSheetCsvFile, fieldnames = csvColumns)

    # Writing CSV Header
    if not globals.isCsvHeaderWritten:
        scoreSheetCsvFileWriter.writeheader()
        globals.isCsvHeaderWritten = True
    
    # Calculating Total SCore
    for data in globals.currentPdfDataList:
        if (globals.isMarksCustomized):
            data["Total Score"] = data["Current Score"]
        else:
            # Checking Total Score Restriction
            if (data["Current Score"] >= globals.maximumScoreThreshold):
                data["Total Score"] = data["Current Score"]
                data["Current Score"] = globals.maximumScoreThreshold
            else:
                data["Total Score"] = data["Current Score"]
        # Writting Data To CSV
        scoreSheetCsvFileWriter.writerow(data)

def PDFDataExtract():
    # Setting Up PDF Reader
    pdfReader = PyPDF2.PdfReader(open(globals.sourceFolderPath + '/' + globals.pdfFileName, mode = "rb"), strict = False)

    # Converting All Pages of PDF To List of Images
    pdfPagesImgList = pdf2image.convert_from_path(globals.sourceFolderPath + '/' + globals.pdfFileName, thread_count = globals.noOfThreads, dpi = globals.pdfDPI, strict = False)

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