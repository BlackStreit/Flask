# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 19:42:34 2024

@author: Admin
"""

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def save_text(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)
