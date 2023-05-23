# Create a custom model class that accepts the weights as input for initialization
# > The model class is a subclass of the PyTorch nn.Module class
# > The model class has a forward() method that accepts the input image and returns the output prediction
# > The model class has a predict() method that accepts the input image and returns the output prediction
# > The model class has a load_weights() method that accepts the weights as input and loads the weights into the model
# > The model class has a load_model() method that accepts the model as input and loads the model into the class
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
from application.data.weights import *

class YOLOv5(nn.Module):
    def __init__(self, weights):
        super(YOLOv5, self).__init__()
        self.load_weights(weights)
        self.load_model()
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = self.model.to(self.device)
        self.model.eval()
        self.transform = transforms.Compose([
            transforms.Resize((640, 640)),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], 
                                 [0.229, 0.224, 0.225])
        ])
        
        self.classes = {0: 'sculpture',
                        1: 'drawings',
                        2: 'iconography',
                        3: 'engraving',
                        4: 'painting'}
        
    def load_weights(self, weights):
        self.weights = weights
        
    def load_model(self):
        self.model = torch.load(self.weights)
        
    def predict(self, image):
        img = self.transform(image).unsqueeze(0)
        with torch.no_grad():
            prediction = self.model(img.to(self.device))
            prediction = F.softmax(prediction, dim=1)
            prediction = torch.argmax(prediction, dim=1)
            prediction = self.classes[int(prediction)]
        return prediction