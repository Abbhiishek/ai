from flask import Flask, render_template, request
from transformers import AutoModelForQuestionAnswering, AutoTokenizer

app = Flask(_name_, template_folder='templates')

model_name = "mistralai/Mixtral-8x7B-Instruct-v0.1"
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form['question']
       
        inputs = tokenizer(question, return_tensors="pt", max_length=512, truncation=True)
        
        outputs = model(**inputs)
      
        answer_start = torch.argmax(outputs.start_logits)
        answer_end = torch.argmax(outputs.end_logits) + 1
        answer = tokenizer.decode(inputs["input_ids"][0][answer_start:answer_end])
        return render_template('index.html', question=question, answer=answer)
    else:
        return render_template('index.html')

if _name_ == '_main_':
    app.run(debug=True)
