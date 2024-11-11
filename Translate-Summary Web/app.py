from transformers import T5Tokenizer, T5ForConditionalGeneration
from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# load the T5 model and tokenizer
model_name = "t5-large"  # it could be t5-small or even t5-base
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Helper function to generate text based on task


def generate_text(task_prefix, text):
    input_text = f"{task_prefix}: {text}"
    inputs = tokenizer.encode(
        input_text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs, max_length=150,
                             num_beams=4, early_stopping=True)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Route for translation


@app.route('/translate', methods=['POST'])
def translate():
    input_text = request.form['inputText']
    source_lang = request.form['sourceLanguage']
    target_lang = request.form['targetLanguage']
    task_prefix = f"translate {source_lang} to {target_lang}"
    result = generate_text(task_prefix, input_text)
    return result

# Route for summarization


@app.route('/summarize', methods=['POST'])
def summarize():
    input_text = request.form['inputText']
    result = generate_text("summarize", input_text)
    return result

# Route for translating a summary


@app.route('/translate_summary', methods=['POST'])
def translate_summary():
    source_lang = request.form['sourceLanguage']
    summary_text = request.form['summaryText']
    target_lang = request.form['targetLanguage']
    task_prefix = f"translate {source_lang} to {target_lang}"
    result = generate_text(task_prefix, summary_text)
    result = generate_text("summarize", result)
    return result


if __name__ == '__main__':
    app.run(debug=True)
