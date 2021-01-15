import os
import codecs

from pathlib import Path
from src.Logics.ErrorCorrector import ErrorCorrector as EC
from src.Logics.Metrics import Metrics


class FileProcessor:

    def modifyFile(self):
        self.originalText, self.errorText = self.prepareFiles()
        originalSentencesList, processedSentencesList = EC().returnProcessedSentences(self.originalText, self.errorText)
        Metrics().estimateCorrections(self.originalText, originalSentencesList, processedSentencesList)

    def prepareFiles(self):
        fileFolder = self.__definePathToFile()
        commonErrors = '%s\\ZapovednikErrors.txt' % fileFolder
        commonText = '%s\\Zapovednik.txt' % fileFolder
        errorText = self.__readFile(commonErrors)
        correctText = self.__readFile(commonText)
        return correctText, errorText

    def __definePathToFile(self):
        rootProjectPath = Path(os.path.abspath(__file__)).parents[2]
        fileFolder = '%s\\filesToCorrect' % rootProjectPath
        return fileFolder

    def __readFile(self, file):
        with codecs.open(file, encoding='utf-8') as fileOpened:
            textReadfromFile = fileOpened.read()
        fileOpened.close()
        return textReadfromFile
