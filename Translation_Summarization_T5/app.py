from transformers import T5Tokenizer, T5ForConditionalGeneration
from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# load the T5 model and tokenizer
model_name = "t5-base" # it could be t5-small or even t5-large
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    input_text = request.form['inputText']
    summary_input = f"summarize: {input_text}"
    summary_input_ids = tokenizer.encode(summary_input, return_tensors="pt")
    summary_outputs = model.generate(summary_input_ids, max_length=20, num_beams=4, early_stopping=True)
    summary_text = tokenizer.decode(summary_outputs[0], skip_special_tokens=True)
    return summary_text

@app.route('/translate', methods=['POST'])
def translate():
    print("Translate route called")
    input_text = request.form['inputText']
    source_language = request.form['sourceLanguage']
    target_language = request.form['targetLanguage']
    translation_input = f"translate {source_language} to {target_language}: {input_text}"
    translation_input_ids = tokenizer.encode(translation_input, return_tensors="pt")
    translation_outputs = model.generate(translation_input_ids, max_length=60, num_beams=4, early_stopping=True)
    translated_text = tokenizer.decode(translation_outputs[0], skip_special_tokens=True)
    print(f"Input Text: {input_text}, Source: {source_language}, Target: {target_language}")
    return translated_text

@app.route('/translate_summary', methods=['POST'])
def translate_summary():
    summary_text = request.form['summaryText']
    source_language = request.form['sourceLanguage']
    target_language = request.form['targetLanguage']
    translation_summary_input = f"translate {source_language} to {target_language}: {summary_text}"
    translation_summary_input_ids = tokenizer.encode(translation_summary_input, return_tensors="pt")
    translated_summary_outputs = model.generate(translation_summary_input_ids, max_length=20, num_beams=4, early_stopping=True)
    translated_summary_text = tokenizer.decode(translated_summary_outputs[0], skip_special_tokens=True)
    return translated_summary_text

if __name__ == "__main__":
    app.run(debug=True, port=5000)


