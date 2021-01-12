from deeppavlov import configs, build_model
from src.Logics.FileProcessor import FileProcessor as FP
from sklearn.metrics import precision_recall_fscore_support as score

class Levenstein:

    def useLevenstein(self):
        self.correctText, self.errorText = FP().prepareFiles()
        correctTextTokenized, errorTextTokenized = FP().tokenizeText(self.correctText, self.errorText)
        correctorModel = build_model(configs.spelling_correction.levenshtein_corrector_ru, download=False)
        textCorrected = correctorModel(errorTextTokenized)
        print(textCorrected)
        precision, recall, fScore, support = score(correctTextTokenized, textCorrected, average='macro')
        print('Precision : {}'.format(precision))
        print('Recall    : {}'.format(recall))
        print('F-score   : {}'.format(fScore))
        print('Support   : {}'.format(support))

if __name__ == '__main__':
    Levenstein().useLevenstein()