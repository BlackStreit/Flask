from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class SpellCorrector:
    def __init__(self, model_name="t5-small"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def correct(self, text):
        inputs = self.tokenizer.encode("spell: " + text, return_tensors="pt")
        outputs = self.model.generate(inputs, max_length=50, num_beams=4, early_stopping=True)
        corrected_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return corrected_text
