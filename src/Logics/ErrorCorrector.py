import re

from deeppavlov import configs, build_model


class ErrorCorrector:
    def __init__(self):
        self.correctorModel = build_model(configs.spelling_correction.brillmoore_kartaslov_ru, download=False)

    def preprocessText(self, textReadfromFile):
        textToWords = self.__divideIntoTokens(textReadfromFile)
        wordsCorrected = self.correctorModel(textToWords)
        rightWordsCaseList = self.__correctMatch(textToWords, wordsCorrected)
        textCorrected = self.__insertRightCasetoText(rightWordsCaseList, textToWords, textReadfromFile)
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
        for word in range(len(rightWordsCaseList)):
            for token in range(len(textToWords)):
                textCorrected = re.sub(textToWords[token], rightWordsCaseList[word], textReadfromFile)
                textReadfromFile = textCorrected
                token += 1
                word += 1
            break
        textCorrected = textReadfromFile
        return textCorrected
