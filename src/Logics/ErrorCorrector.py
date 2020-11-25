import re

from deeppavlov import configs
from deeppavlov.core.commands.infer import build_model


class ErrorCorrector:

    def __init__(self):
        self.correctorModel = build_model(configs.spelling_correction.levenshtein_corrector_ru, download=True)


    def correctText(self, textReadfromFile):
        textToWords = self.__divideIntoTokens(textReadfromFile)
        wordsCorrected = self.correctorModel(textToWords)
        rightWordsCaseList = self.__correctMatch(textToWords, wordsCorrected)
        textCorrected = self.__insertRightCasetoText(rightWordsCaseList, textToWords, textReadfromFile)
        return textCorrected

    def __divideIntoTokens(self, text):
        textTokenized = re.findall(r'\w+(?:[-]\w+)|[А-Яа-яЁё]+', text)
        return textTokenized

    def __correctMatch(self, textToWords, wordsCorrected):
        rightCase = []
        for correctWord in range(len(wordsCorrected)):
            for token in range(len(textToWords)):
                rightWord = self.__checkCase(textToWords[token])(wordsCorrected[correctWord])
                rightCase.append(rightWord)
                list.remove(wordsCorrected, wordsCorrected[correctWord])
                correctWord = 0
            break
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
