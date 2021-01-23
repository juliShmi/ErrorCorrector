from spellchecker import SpellChecker
from src.Logics.FileProcessor import FileProcessor as FP
from src.Logics.ErrorCorrector import ErrorCorrector as EC
from src.Logics.Metrics import Metrics


class PySpellChecker:

    def useSpellChecker(self):
        self.originalText, self.errorText = FP().prepareFiles()
        originalSentencesList, errorSentencesList = EC().textToSentences(self.originalText, self.errorText)
        print(len(originalSentencesList), len(errorSentencesList))
        checker = SpellChecker()
        corpusPath = FP().definePathToCoprus()
        checker.word_frequency.load_text_file(corpusPath)
        processedWordsList = []
        for sentence in errorSentencesList:
            wordsList = EC().sentencesToWords(sentence)
            wordsListLower = [element.lower() for element in wordsList]
            for word in wordsListLower:
                misspelled = checker.correction(word)
                processedWordsList.append(misspelled)
        self.useWordsMetrics(self.originalText, processedWordsList)

    def useWordsMetrics(self, originalText, processedWordsList):
        originalWordsList = EC().sentencesToWords(originalText)
        originalWordsListLower = [element.lower() for element in originalWordsList]
        processedWordsListLower = [element.lower() for element in processedWordsList]
        print('Words List Lower Estimation:\n')
        Metrics().printMetrics(originalWordsListLower, processedWordsListLower)



if __name__ == '__main__':
    PySpellChecker().useSpellChecker()
