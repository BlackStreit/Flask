# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 19:58:58 2024

@author: Admin
"""

from flask import Flask, request, jsonify
from model import SpellCorrector

app = Flask(__name__)
corrector = SpellCorrector()

@app.route('/correct', methods=['POST'])
def correct_text():
    try:
        data = request.get_json()
        text = data.get('text', '')
        corrected_text = corrector.correct(text)
        return jsonify({'corrected_text': corrected_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
