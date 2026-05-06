# Abstraction means hiding complex details and showing only necessary features
from abc import ABC ,abstractmethod

class model(ABC):
    @abstractmethod
    def train(self):
        pass
class linearregression(model):
     def train(self):
        print("training linear regression model")

model = linearregression()
model.train()