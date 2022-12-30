import os
import joblib
from django.apps import AppConfig
from django.conf import settings
from custom_model import AttentionModel
import torch

def load_checkpoint(filepath):
    checkpoint = torch.load(filepath)
    model = checkpoint['model']
    model.load_state_dict(checkpoint['state_dict'])
    for parameter in model.parameters():
        parameter.requires_grad = False

    model.eval()
    return model

class ApiConfig(AppConfig):
    name = 'monitor'
    model_path = '../../../model'
    model = load_checkpoint(r'C:\\Users\\Admin\\working\\python\\mine\\Django-Deploy-UI-Chatbot\\model\\checkpoint.pth')
    vocab2index = torch.load(r'C:\\Users\\Admin\\working\\python\\mine\\Django-Deploy-UI-Chatbot\\model\\vocab_12jul.pth')

