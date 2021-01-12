import jamspell
from src.Logics.FileProcessor import FileProcessor as FP
from sklearn.metrics import precision_recall_fscore_support as score


class Jamspell:

    def useJamspell(self):
        self.correctText, self.errorText = FP().prepareFiles()
        correctTextTokenized, errorTextTokenized = FP().tokenizeText(self.correctText, self.errorText)
        print(len(correctTextTokenized), len(errorTextTokenized))
        afterCorrection = []
        corrector = jamspell.TSpellCorrector()
        corrector.LoadLangModel('C:\\Users\\ishmitko\\Downloads\\ru_small.bin')
        for sentence in errorTextTokenized:
            sentenceCorrected = corrector.FixFragment(sentence)
            print(sentenceCorrected)
            afterCorrection.append(sentenceCorrected)
        precision, recall, fScore, support = score(correctTextTokenized, afterCorrection, average='macro')
        print('Precision : {}'.format(precision))
        print('Recall    : {}'.format(recall))
        print('F-score   : {}'.format(fScore))
        print('Support   : {}'.format(support))

if __name__ == '__main__':
    Jamspell().useJamspell()
