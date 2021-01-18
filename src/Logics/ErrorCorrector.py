import re
import pymorphy2

from deeppavlov import configs, build_model
from stop_words import get_stop_words


class ErrorCorrector:

    def returnProcessedSentences(self, originalText, errorText):
        originalSentencesList, errorSentencesList = self.textToSentences(originalText, errorText)
        print(len(originalSentencesList), len(errorSentencesList))
        correctedSentencesList = self.useDeeppavlov(errorSentencesList)
        processedSentencesList = self.__returnRightCaseSentence(errorSentencesList, correctedSentencesList)
        return originalSentencesList, processedSentencesList

    def textToSentences(self, originalText, errorText):
        originalSentencesList = re.split(r' *[\…\.\?!][\'"\)\]\»]* *', originalText)
        errorSentencesList = re.split(r' *[\…\.\?!][\'"\)\]\»]* *', errorText)
        return originalSentencesList, errorSentencesList

    def sentencesToWords(self, sentencesList):
        wordsList = re.findall(r'\d+(?:,\d+)?|[\w]+[-\w]+|[\w]', sentencesList)
        return wordsList

    def __returnRightCaseSentence(self, errorSentencesList, correctedSentencesList):
        processedSentencesList = []
        i = 0
        while i < len(correctedSentencesList):
            errorWordsList = self.sentencesToWords(errorSentencesList[i])
            correctedWordsList = self.sentencesToWords(correctedSentencesList[i])
            rightWordsCaseList = self.__correctMatch(errorWordsList, correctedWordsList)
            properNounsList = self.__defineProperNouns(rightWordsCaseList)
            correctionToText = self.__insertRightCasetoSentence(errorWordsList, properNounsList, errorSentencesList[i])
            processedSentencesList.append(correctionToText)
            i += 1
        return processedSentencesList

    def useDeeppavlov(self, errorSentencesList):
        correctorModel = build_model(configs.spelling_correction.brillmoore_kartaslov_ru, download=False)
        correctedSentencesList = correctorModel(errorSentencesList)
        return correctedSentencesList

    def __checkStopWords(self, textToWords):
        stopCorpora = get_stop_words('ru')
        noStopWordsList = []
        for word in textToWords:
            if word not in stopCorpora:
                noStopWordsList.append(word)
        if len(noStopWordsList) == 0:
            return textToWords
        return noStopWordsList

    def __correctMatch(self, errorWordsList, correctedWordsList):
        rightWordsCaseList = []
        if len(errorWordsList) == len(correctedWordsList):
            i = 0
            while i < len(errorWordsList):
                rightWord = self.__checkCase(errorWordsList[i])(correctedWordsList[i])
                rightWordsCaseList.append(rightWord)
                i += 1
        return rightWordsCaseList

    def __checkCase(self, word):
        if word.isupper():
            return str.upper
        elif word.islower():
            return str.lower
        elif word.istitle():
            return str.title
        else:
            return str

    def __insertRightCasetoSentence(self, errorWordsList, properNounsList, errorSentence):
        if len(properNounsList) == len(errorWordsList):
            i = 0
            while i < len(errorWordsList):
                replacedWords = re.sub(errorWordsList[i], properNounsList[i], errorSentence)
                errorSentence = replacedWords
                i += 1
        else:
            print('Check the length of lists')
        correctionToText = errorSentence
        return correctionToText

    def __defineProperNouns(self, rightWordsCaseList):
        properNounsList = []
        morph = pymorphy2.MorphAnalyzer()
        for word in rightWordsCaseList:
            grammarTags = morph.parse(word)
            for criteria in grammarTags:
                if "Surn" in criteria.tag or "Name" in criteria.tag or "Geox" in criteria.tag:
                    word = word.title()
            properNounsList.append(word)
        return properNounsList
