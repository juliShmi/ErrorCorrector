from pyaspeller import YandexSpeller

from src.Logics.FileProcessor import FileProcessor as FP
from src.Logics.ErrorCorrector import ErrorCorrector as EC
from src.Logics.Metrics import Metrics


class Yaspeller:

    def useSpeller(self):
        self.originalText, self.errorText = FP().prepareFiles()
        originalSentencesList, errorSentencesList = EC().textToSentences(self.originalText, self.errorText)
        print(len(originalSentencesList), len(errorSentencesList))
        processedSentencesList = []
        speller = YandexSpeller()
        for sentence in errorSentencesList:
            if sentence == "":
                processedSentencesList.append(sentence)
            else:
                for change in speller.spell(sentence):
                    if change['s'] == []:
                        changes = {change['word']: change['word']}
                    else:
                        changes = {change['word']: change['s'][0]}
                    for word, suggestion in changes.items():
                        sentence = sentence.replace(word, suggestion)
                processedSentencesList.append(sentence)
        Metrics().estimateCorrections(self.originalText,originalSentencesList, processedSentencesList)


if __name__ == '__main__':
    Yaspeller().useSpeller()
