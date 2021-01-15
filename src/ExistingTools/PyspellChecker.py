from spellchecker import SpellChecker
from src.Logics.FileProcessor import FileProcessor as FP
import re

class PySpellChecker:

    def useSpellChecker(self):
        self.correctText, self.errorText = FP().prepareFiles()
        correctTextTokenized, errorTextTokenized = FP().tokenizeText(self.correctText, self.errorText)
        print(len(correctTextTokenized), len(errorTextTokenized))
        checker = SpellChecker()
        corpusPath = 'C:\\Users\\ishmitko\\Desktop\\corpusRus.txt'
        checker.word_frequency.load_text_file(corpusPath)
        correctedWords = []
        for sentence in errorTextTokenized:
            sentenceWords = re.findall(r'\d+(?:,\d+)?|[\w]+[-\w]+|[\w]', sentence)
            for word in sentenceWords:
                misspelled = checker.correction(word)
                correctedWords.append(misspelled)
        print(correctedWords)
        print(len(correctedWords))


if __name__ == '__main__':
    PySpellChecker().useSpellChecker()
