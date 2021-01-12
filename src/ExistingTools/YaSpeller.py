from pyaspeller import YandexSpeller
from src.Logics.FileProcessor import FileProcessor as FP
from sklearn.metrics import precision_recall_fscore_support as score


class Yaspeller:

    def useSpeller(self):
        self.correctText, self.errorText = FP().prepareFiles()
        correctTextTokenized, errorTextTokenized = FP().tokenizeText(self.correctText, self.errorText)
        print(len(correctTextTokenized), len(errorTextTokenized))
        afterCorrection = []
        speller = YandexSpeller()
        for sentence in errorTextTokenized:
            for change in speller.spell(sentence):
                if change['s'] == []:
                    changes = {change['word']: change['word']}
                else:
                    changes = {change['word']: change['s'][0]}
                for word, suggestion in changes.items():
                    sentence = sentence.replace(word, suggestion)
            print(sentence)
            afterCorrection.append(sentence)
        precision, recall, fScore, support = score(correctTextTokenized, afterCorrection, average='macro')
        print('Precision : {}'.format(precision))
        print('Recall    : {}'.format(recall))
        print('F-score   : {}'.format(fScore))
        print('Support   : {}'.format(support))


if __name__ == '__main__':
    Yaspeller().useSpeller()
