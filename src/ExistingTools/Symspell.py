from symspellpy import SymSpell, Verbosity
from src.Logics.FileProcessor import FileProcessor as FP
import re
from sklearn.metrics import precision_recall_fscore_support as score

class Symspell:

    def useSymspell(self):
        self.correctText, self.errorText = FP().prepareFiles()
        correctTextTokenized, errorTextTokenized = FP().tokenizeText(self.correctText, self.errorText)
        print(len(correctTextTokenized), len(errorTextTokenized))
        afterCorrection = []
        speller = SymSpell()
        corpusPath = 'C:\\Users\\ishmitko\\Desktop\\corpusRus.txt'
        speller.create_dictionary(corpusPath, encoding='utf-8')
        for sentence in errorTextTokenized:
            sentenceWords = re.findall(r'\d+(?:,\d+)?|[\w]+[-\w]+|[\w]', sentence)
            for word in sentenceWords:
                suggestions = speller.lookup(word, Verbosity.CLOSEST,
                                           max_edit_distance=2, include_unknown=True)
                for suggestion in suggestions:
                    afterCorrection.append(suggestion.term)
                    break
        print(afterCorrection)
        print(len(afterCorrection))




if __name__ == '__main__':
    Symspell().useSymspell()