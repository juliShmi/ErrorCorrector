import os
from pathlib import Path

import codecs

from src.Logics.ErrorCorrector import ErrorCorrector as EC


class FileProcessor:

    def modifyFile(self):
        fileFolder = self.__definePathToFile()
        file = '%s\\Example.txt' % fileFolder
        textReadfromFile = self.__readFile(file)
        textCorrected = EC().preprocessText(textReadfromFile)
        print(textCorrected)
        self.__writeToFile(textCorrected, file)

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
