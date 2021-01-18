from symspellpy import SymSpell, Verbosity
from src.Logics.FileProcessor import FileProcessor as FP
from src.Logics.ErrorCorrector import ErrorCorrector as EC
from src.Logics.Metrics import Metrics


class Symspell:

    def useSymspell(self):
        self.originalText, self.errorText = FP().prepareFiles()
        originalSentencesList, errorSentencesList = EC().textToSentences(self.originalText, self.errorText)
        print(len(originalSentencesList), len(errorSentencesList))
        speller = SymSpell()
        corpusPath = FP().definePathToCoprus()
        speller.create_dictionary(corpusPath, encoding='utf-8')
        processedWordsList = []
        for sentence in errorSentencesList:
            sentenceWords = EC().sentencesToWords(sentence)
            for word in sentenceWords:
                suggestions = speller.lookup(word, Verbosity.CLOSEST,
                                             max_edit_distance=2, include_unknown=True)
                for suggestion in suggestions:
                    processedWordsList.append(suggestion.term)
                    break
        print(len(processedWordsList))
        self.useWordsMetrics(self.originalText, processedWordsList)

    def useWordsMetrics(self, originalText, processedWordsList):
        originalWordsList = EC().sentencesToWords(originalText)
        originalWordsListLower = [element.lower() for element in originalWordsList]
        processedWordsListLower = [element.lower() for element in processedWordsList]
        print('Words List Lower Estimation:\n')
        Metrics().printMetrics(originalWordsListLower, processedWordsListLower)


if __name__ == '__main__':
    Symspell().useSymspell()
