from sklearn import metrics

from src.Logics.ErrorCorrector import ErrorCorrector as EC


class Metrics:
    def estimateCorrections(self, originalText, originalSentencesList, processedSentencesList):
        self.estimateWords(originalText, processedSentencesList)
        self.estimateSentences(originalSentencesList, processedSentencesList)


    def estimateSentences(self, originalSentencesList, processedSentencesList):
        print(metrics.classification_report(originalSentencesList, processedSentencesList))
        originalSentencesLower = [element.lower() for element in originalSentencesList]
        processedSentencesLower = [element.lower() for element in processedSentencesList]
        print(metrics.classification_report(originalSentencesLower, processedSentencesLower))

    def estimateWords(self, originalText, processedSentencesList):
        originalWordsList = EC().sentencesToWords(originalText)
        print(originalWordsList, len(originalWordsList))
        originalWordsListLower = [element.lower() for element in originalWordsList]
        print(originalWordsListLower, len(originalWordsListLower))
        processedWordsListLower = []
        for sentence in processedSentencesList:
            words = EC().sentencesToWords(sentence)
            wordsLower = [element.lower() for element in words]
            processedWordsListLower.extend(wordsLower)
        print(processedWordsListLower, len(processedWordsListLower))
        print(metrics.classification_report(originalWordsListLower, processedWordsListLower))
