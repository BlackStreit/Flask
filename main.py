from model import SpellCorrector
from utils import load_text, save_text

def main():
    corrector = SpellCorrector()
    input_text = load_text("input.txt")
    corrected_text = corrector.correct(input_text)
    save_text("output.txt", corrected_text)
    print("Исправленный текст сохранен в output.txt")

if __name__ == "__main__":
    main()
