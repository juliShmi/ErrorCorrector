import re
import pymorphy2

from deeppavlov import configs, build_model
from stop_words import get_stop_words


class ErrorCorrector:

    def returnProcessedSentences(self, originalText, errorText):
        originalSentencesList, errorSentencesList = self.textToSentences(originalText, errorText)
        correctedSentencesList = self.__useDeeppavlov(errorSentencesList)
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
            correctionToText = self.__insertRightCasetoText(errorWordsList, properNounsList, errorSentencesList[i])
            processedSentencesList.append(correctionToText)
            i += 1
        return processedSentencesList

    def __useDeeppavlov(self, errorSentencesList):
        correctorModel = build_model(configs.spelling_correction.brillmoore_kartaslov_ru, download=False)
        sentencesListCorrected = correctorModel(errorSentencesList)
        return sentencesListCorrected

    def __checkStopWords(self, textToWords):
        stopCorpora = get_stop_words('ru')
        noStopWordsList = []
        for word in textToWords:
            if word not in stopCorpora:
                noStopWordsList.append(word)
        if len(noStopWordsList) == 0:
            return textToWords
        return noStopWordsList

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

    def __insertRightCasetoText(self, textToWords, rightWordsCaseList, textReadfromFile):
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
