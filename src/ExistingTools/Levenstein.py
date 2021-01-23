from deeppavlov import configs, build_model
from src.Logics.FileProcessor import FileProcessor as FP
from src.Logics.ErrorCorrector import ErrorCorrector as EC
from src.Logics.Metrics import Metrics


class Levenstein:

    def useLevenstein(self):
        self.originalText, self.errorText = FP().prepareFiles()
        originalSentencesList, errorSentencesList = EC().textToSentences(self.originalText, self.errorText)
        print(len(originalSentencesList), len(errorSentencesList))
        correctorModel = build_model(configs.spelling_correction.levenshtein_corrector_ru, download=True)
        processedSentencesList = correctorModel(errorSentencesList)
        Metrics().estimateWords(self.originalText, processedSentencesList)


if __name__ == '__main__':
    Levenstein().useLevenstein()
