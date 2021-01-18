from sklearn.metrics import precision_recall_fscore_support as score

from src.Logics.ErrorCorrector import ErrorCorrector as EC


class Metrics:
    def estimateCorrections(self, originalText, originalSentencesList, processedSentencesList):
        self.estimateSentences(originalSentencesList, processedSentencesList)
        self.estimateWords(originalText, processedSentencesList)

    def estimateSentences(self, originalSentencesList, processedSentencesList):
        print('Sentences Original Case Estimation:\n')
        self.printMetrics(originalSentencesList, processedSentencesList)
        originalSentencesLower = [element.lower() for element in originalSentencesList]
        processedSentencesLower = [element.lower() for element in processedSentencesList]
        print('Sentences Lower Case Estimation:\n')
        self.printMetrics(originalSentencesLower, processedSentencesLower)

    def estimateWords(self, originalText, processedSentencesList):
        originalWordsList = EC().sentencesToWords(originalText)
        originalWordsListLower = [element.lower() for element in originalWordsList]
        processedWordsListLower = []
        for sentence in processedSentencesList:
            words = EC().sentencesToWords(sentence)
            processedWordsList = [element.lower() for element in words]
            processedWordsListLower.extend(processedWordsList)
        print('Words List Lower Estimation:\n')
        self.printMetrics(originalWordsListLower, processedWordsListLower)

    def printMetrics(self, originalText, correctedText):
        precision, recall, fScore, support = score(originalText, correctedText, average='macro')
        print('Precision : {}'.format(precision))
        print('Recall    : {}'.format(recall))
        print('F-score   : {}'.format(fScore))
        print('Support   : {}'.format(support))
