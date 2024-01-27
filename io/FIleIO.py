import csv
import PyPDF2
import pdf2image
import multiprocessing as mulproc

sourceFolderPath = ''
outputFolderParentPath = ''
outputFolderName = 'data'
courseProviderNameListCsvFilePath = ''
personNameListCsvFilePath = ''
pdfFileName = ''

isMarksCustomized = False
isCsvHeaderWritten = False

maximumScoreThreshold = 50

currentPdfDataDictionary = {}
currentPdfDataList = []

def CSVWriter():
    # Setting CSV File Columns Names
    csvColumns = ['Name','Course Type','Duration','Current Score','Total Score']

    global isCsvHeaderWritten
    
    # Opening CSV File
    scoreSheetCsvFile = open(outputFolderParentPath + '/' + outputFolderName + "/CertificateDetails.csv", 'a+')
    scoreSheetCsvFileWriter = csv.DictWriter(scoreSheetCsvFile, fieldnames = csvColumns)

    # Writing CSV Header
    if not isCsvHeaderWritten:
        scoreSheetCsvFileWriter.writeheader()
        isCsvHeaderWritten = True
    
    # Calculating Total SCore
    for data in currentPdfDataList:
        if (isMarksCustomized):
            data["Total Score"] = data["Current Score"]
        else:
            # Checking Total Score Restriction
            if (data["Current Score"] >= maximumScoreThreshold):
                data["Total Score"] = data["Current Score"]
                data["Current Score"] = maximumScoreThreshold
            else:
                data["Total Score"] = data["Current Score"]
        # Writting Data To CSV
        scoreSheetCsvFileWriter.writerow(data)

def PDFDataExtract():
    # Setting Up PDF Reader
    pdfReader = PyPDF2.PdfReader(open(sourceFolderPath+"/"+pdfFileName,mode="rb"),strict=False)

    # Converting All Pages of PDF To List of Images
    pdfPagesImgList = pdf2image.convert_from_path(sourceFolderPath+"/"+pdfFileName,thread_count=mulproc.cpu_count(),dpi=200,strict=False)

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