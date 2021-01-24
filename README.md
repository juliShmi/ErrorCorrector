ErrorCorrector is a spell-checking tool which allows to compare some existing NLP tools (DeepPavlov Levenshtein, DeepPavlov Brilmoore, Yandex.Speller, SymSpell, PyspellChecker)
Is corrects a text with grammar mistakes, compares with the correct text and provides metrics score to define accuracy, recall and F-score parameters.
ErrorCorrector calls an NLP tool in a row, corrects text and returns the case and punctuation of the original document to raise metrics.

To compare texts add 2 files in txt.format to "filesToCorrect" folder. One file should be original text without mistakes. Second one is the text to correct.
Rewrite paths to added files in FileProcessor.prepareFiles
Run main.py
