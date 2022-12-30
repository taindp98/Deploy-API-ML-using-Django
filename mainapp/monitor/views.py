from django.shortcuts import render
import numpy as np
import pandas as pd
from .apps import *
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from pyvi import ViTokenizer
import torch
import torch.nn as nn



def tokenize(text):
    list_token = ViTokenizer.tokenize(text)
    return list_token.split(' ')

def encode_sentence(text, vocab2index, N=75):
    tokenized = tokenize(text)
    encoded = np.zeros(N, dtype=int)
    enc1 = np.array([vocab2index.get(word, vocab2index["UNK"]) for word in tokenized])
#     print(len(enc1))
    length = min(N, len(enc1))
    encoded[:length] = enc1[:length]
#     print(len(encoded))
    encoded_array = torch.from_numpy(encoded.astype(np.float32))
    encoded_array = torch.reshape(encoded_array,(1,N))
    
    ## padding
    pad_enc = torch.zeros([29,N])
    encoded_array_pad = torch.cat([encoded_array,pad_enc])
    return encoded_array_pad.long()



class Prediction(APIView):
    def post(self, request):
        #data = request.data
        text= request.GET.get('text')
        
        model = ApiConfig.model
        vocab2index = ApiConfig.vocab2index

        #predict using independent variables
        enc_vector = encode_sentence(text,vocab2index,22)
        preds = model(enc_vector)
        prop_preds = nn.functional.softmax(preds,dim=1)
        pred_label = prop_preds.argmax().item()
        # label = ['type_edu','case','career']
        response_dict = {"Predicted intent":  pred_label}
        print(response_dict)
        return Response(response_dict, status=200)
