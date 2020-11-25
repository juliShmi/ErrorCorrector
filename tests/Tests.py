import unittest
from src.Logics.ErrorCorrector import ErrorCorrector as EC


class TestErrorCorrector(unittest.TestCase):

    def _testCheckCorrections(self, textCorrected, rightText):
        self.assertMultiLineEqual(textCorrected, rightText)

    def testCheckSentence1(self):
        textToCheck = "В октябре ЦЬБ ухудшил прогноз по чистому оттоку апитала из Ооссии в 2020 год3 с 25 миллиардтв долларов що 53 миллиардрв."
        rightText = "В октябре ЦБ ухудшил прогноз по чистому оттоку капитала из России в 2020 году с 25 миллиардов долларов до 53 миллиардов."
        textCorrected = EC().correctText(textToCheck)
        self._testCheckCorrections(textCorrected, rightText)

    def testCheckSentence2(self):
        textToCheck = "Поэтому за всей этой суетой вокруг рредвыборнрй гонки мы поропустили П-НАСТОЯЩЕМЦ важную новрость: в Австрлии обнаружили два новцх вида млекопитающих."
        rightText = "Поэтому за всей этой суетой вокруг предвыборной гонки мы пропустили ПО-НАСТОЯЩЕМУ важную новость: в Австралии обнаружили два новых вида млекопитающих."
        textCorrected = EC().correctText(textToCheck)
        self._testCheckCorrections(textCorrected, rightText)

    def testCheckSentence3(self):
        textToCheck = "И то — глазастые улыбчивы ушастики. Ттлько посмотрите на них!"
        rightText = "И это — глазастые улыбчивые ушастики. Только посмотрите на них!"
        textCorrected = EC().correctText(textToCheck)
        self._testCheckCorrections(textCorrected, rightText)

    def testCheckSentence4(self):
        textToCheck = "Прогнознвй показатеь приблизилдся к рекордк 2018 года, когда ротток состаил 67,5 миллиаржа доларов."
        rightText = "Прогнозный показатель приблизился к рекорду 2018 года, когда отток составил 67,5 миллиарда долларов."
        textCorrected = EC().correctText(textToCheck)
        self._testCheckCorrections(textCorrected, rightText)

    def testCheckSentence5(self):
        textToCheck = "В июле-октяббре 2020 года банки каждый мемяц обновлялди историчекие максимумы по общей свумме выданных жилищныэ кредитов."
        rightText = "В июле-октябре 2020 года банки каждый месяц обновляли исторические максимумы по общей сумме выданных жилищных кредитов."
        textCorrected = EC().correctText(textToCheck)
        self._testCheckCorrections(textCorrected, rightText)

    def testCheckSentence6(self):
        textToCheck = "Термин «самцрай», который впоследстуии объединитт всю воинсуую элиту Японии, возник аак минимум ы начале X веуа."
        rightText = "Термин «самурай», который впоследствии объединит всю воинскую элиту Японии, возник как минимум в начале X века."
        textCorrected = EC().correctText(textToCheck)
        self._testCheckCorrections(textCorrected, rightText)

    def testCheckSentence7(self):
        textToCheck = "В Минске сдпелали обязаьельным ношкние маски ппи посещении всех городмких объектв, а также в оьщественноп транспорт, включая тавси."
        rightText = "В Минске сделали обязательным ношение маски при посещении всех городских объектов, а также в общественном транспорте, включая такси."
        textCorrected = EC().correctText(textToCheck)
        self._testCheckCorrections(textCorrected, rightText)

    def testCheckSentence8(self):
        textToCheck = "Особенная яерта харакера алабая — остоинствь, уверенность в себе, что лчень выразмительно передано в новомм монументе."
        rightText = "Особенная черта характера алабая — достоинство, уверенность в себе, что очень выразительно передано в новом монументе."
        textCorrected = EC().correctText(textToCheck)
        self._testCheckCorrections(textCorrected, rightText)

    def testCheckSentence9(self):
        textToCheck = "Незнакоме не присел к мтолу, где рамположилисл немногочимленные посктители, а остался у стойви, внимателно изучая вщглядом траатирщика."
        rightText = "Незнакомец не присел к столу, где расположились немногочисленные посетители, а остался у стойки, внимательно изучая взглядом трактирщика."
        textCorrected = EC().correctText(textToCheck)
        self._testCheckCorrections(textCorrected, rightText)

    def testCheckSentence10(self):
        textToCheck = "«В это Рождевтво подари ьо, что можешо дать толькг ты», — говорит слоган праздничной рекоамы, которуб в декабре б3дут показыаать в 92 странпах мира."
        rightText = "«В это Рождество подари то, что можешь дать только ты», — говорит слоган праздничной рекламы, которую в декабре будут показывать в 92 странах мира."
        textCorrected = EC().correctText(textToCheck)
        self._testCheckCorrections(textCorrected, rightText)


suite = unittest.TestLoader().loadTestsFromTestCase(TestErrorCorrector)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    unittest.main()
