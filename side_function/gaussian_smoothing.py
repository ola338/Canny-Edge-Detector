# -*- coding: utf-8 -*-
"""gaussian_smoothing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/179BVwjGO5lseB0MYcmPAoWi3CJc5H_Po
"""

def gaussian_smoothing(image, sigma):
  return nd.gaussian_filter(image, sigma)