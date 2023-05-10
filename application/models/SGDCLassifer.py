from .base import Model
from ..data.Preprocessing import Preprocessing as prep


class SGDClassifier(Model):

    def performTest(self, testData):
        pass
    pass


SGDobject = SGDClassifier()
SGDobject.performTest(
    prep.testData()
)
