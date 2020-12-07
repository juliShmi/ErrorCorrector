import os
from pathlib import Path

import codecs
from nltk import tokenize
from sklearn import metrics

from src.Logics.ErrorCorrector import ErrorCorrector as EC


class FileProcessor:

    def modifyFile(self):
        self.correctText, self.errorText = self.prepareFiles()
        self.correctTextTokenized, self.errorTextTokenized = self.tokenizeText(self.correctText, self.errorText)
        print(len(self.correctTextTokenized), len(self.errorTextTokenized))
        afterCorrection = []
        sentenceCorrected = EC().preprocessText(self.errorText)
        print(sentenceCorrected)
        print(afterCorrection)
        print(len(afterCorrection))
        print(metrics.classification_report(self.correctText, sentenceCorrected))

    def prepareFiles(self):
        fileFolder = self.__definePathToFile()
        commonErrors = '%s\\ZapovednikErrors.txt' % fileFolder
        commonText = '%s\\Zapovednik.txt' % fileFolder
        errorText = self.__readFile(commonErrors)
        correctText = self.__readFile(commonText)
        return correctText, errorText

    def tokenizeText(self, correctText, errorText):
        correctTextTokenized = tokenize.sent_tokenize(correctText, language='russian')
        errorTextTokenized = tokenize.sent_tokenize(errorText, language="russian")
        return correctTextTokenized, errorTextTokenized

    def __definePathToFile(self):
        rootProjectPath = Path(os.path.abspath(__file__)).parents[2]
        fileFolder = '%s\\filesToCorrect' % rootProjectPath
        return fileFolder

    def __readFile(self, file):
        with codecs.open(file, encoding='utf-8') as fileOpened:
            textReadfromFile = fileOpened.read()
        fileOpened.close()
        return textReadfromFile

    def __writeToFile(self, newSentence, file):
        fileOpened = codecs.open(file, 'w', encoding='utf-8')
        fileOpened.write(newSentence)
        fileOpened.close()

