import re
import pymorphy2

from deeppavlov import configs, build_model
from stop_words import get_stop_words


class ErrorCorrector:
    def __init__(self):
        self.correctorModel = build_model(configs.spelling_correction.brillmoore_kartaslov_ru, download=False)


    def preprocessText(self, textReadfromFile):
        textToWords = self.__divideIntoTokens(textReadfromFile)
        noStopWordsList = self.__checkStopWords(textToWords)
        wordsCorrected = self.correctorModel(noStopWordsList)
        rightWordsCaseList = self.__correctMatch(noStopWordsList, wordsCorrected)
        properNounsList = self.__defineProperNouns(rightWordsCaseList)
        textCorrected = self.__insertRightCasetoText(properNounsList, noStopWordsList, textReadfromFile)
        return textCorrected

    def __checkStopWords(self, textToWords):
        stopCorpora = get_stop_words('ru')
        noStopWordsList = []
        for word in textToWords:
            if word not in stopCorpora:
                noStopWordsList.append(word)
        return noStopWordsList

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

    def __defineProperNouns(self, wordsCorrected):
        properNounsList = []
        morph = pymorphy2.MorphAnalyzer()
        for word in wordsCorrected:
            grammarTags = morph.parse(word)
            for criteria in grammarTags:
                if "Surn" in criteria.tag or "Name" in criteria.tag or "Geox" in criteria.tag:
                    word = word.title()
            properNounsList.append(word)
        return properNounsList
