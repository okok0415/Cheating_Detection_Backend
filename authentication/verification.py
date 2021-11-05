#!/usr/bin/env python
# coding: utf-8
import numpy as np


def CosineDistance(source_representation, test_representation):
    a = np.matmul(np.transpose(source_representation), test_representation)
    b = np.sum(np.multiply(source_representation, source_representation))
    c = np.sum(np.multiply(test_representation, test_representation))
    return 1 - (a / (np.sqrt(b) * np.sqrt(c)))


def EuclideanDistance(source_representation, test_representation):
    euclidean_distance = source_representation - test_representation
    euclidean_distance = np.sum(np.multiply(euclidean_distance, euclidean_distance))
    euclidean_distance = np.sqrt(euclidean_distance)
    return euclidean_distance


def l2_normalize(x):
    return x / np.sqrt(np.sum(np.multiply(x, x)))


def verify(img1_embedding, img2_embedding):
    
    distance = CosineDistance(img1_embedding, img2_embedding)
    print(distance)
        
    if distance <= 0.45:
        return 'True'
    else: 
        return 'False'
    



