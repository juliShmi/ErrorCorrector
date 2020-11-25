import re
import pymorphy2

from deeppavlov import configs, build_model


class ErrorCorrector:
    def __init__(self):
        self.correctorModel = build_model(configs.spelling_correction.brillmoore_kartaslov_ru, download=False)


    def preprocessText(self, textReadfromFile):
        textToWords = self.__divideIntoTokens(textReadfromFile)
        wordsCorrected = self.correctorModel(textToWords)
        rightWordsCaseList = self.__correctMatch(textToWords, wordsCorrected)
        nomensGeoxList = self.__defineNomens(rightWordsCaseList)
        textCorrected = self.__insertRightCasetoText(nomensGeoxList, textToWords, textReadfromFile)
        return textCorrected

    def __divideIntoTokens(self, text):
        textTokenized = re.findall(r'\d+(?:,\d+)?|[-\w]+|[А-Яа-яЁё]+', text)
        return textTokenized

    def __correctMatch(self, textToWords, wordsCorrected):
        rightCase = []
        if len(textToWords) == len(wordsCorrected):
            i = 0
            while i < len(textToWords):
                rightWord = self.__checkCase(textToWords[i])(wordsCorrected[i])
                rightCase.append(rightWord)
                i += 1
        return rightCase

    def __checkCase(self, word):
        if word.isupper():
            return str.upper
        elif word.islower():
            return str.lower
        elif word.istitle():
            return str.title
        else:
            return str

    def __insertRightCasetoText(self, rightWordsCaseList, textToWords, textReadfromFile):
        if len(rightWordsCaseList) == len(textToWords):
            i = 0
            while i < len(textToWords):
                textCorrected = re.sub(textToWords[i], rightWordsCaseList[i], textReadfromFile)
                textReadfromFile = textCorrected
                i += 1
        else:
            print('Check the length of lists')
        textCorrected = textReadfromFile
        return textCorrected

    def __defineNomens(self, wordsCorrected):
        nomensGeoxList = []
        morph = pymorphy2.MorphAnalyzer()
        for word in wordsCorrected:
            grammem = morph.parse(word)
            for tags in grammem:
                if "Surn" in tags.tag or "Name" in tags.tag or "Geox" in tags.tag:
                    word = word.title()
            nomensGeoxList.append(word)
        return nomensGeoxList
