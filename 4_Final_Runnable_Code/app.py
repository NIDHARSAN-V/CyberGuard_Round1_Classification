from flask import Flask, render_template, request
import torch
from transformers import BertTokenizer, BertForSequenceClassification
import joblib
import pandas as pd

app = Flask(__name__)


df = pd.read_csv("sampled_data.csv")  

df = df.dropna()


label_to_int = {label: i for i, label in enumerate(df['sub_category'].unique())}
df['sub_category'] = df['sub_category'].map(label_to_int)


model = BertForSequenceClassification.from_pretrained("trained_bert_model")
tokenizer = BertTokenizer.from_pretrained("trained_bert_tokenizer")


model.eval()


int_to_label = {v: k for k, v in label_to_int.items()}


def predict(model, tokenizer, texts, max_length=128):
    model.eval()
    predictions = []
    with torch.no_grad():
        for text in texts:
          
            tokens = tokenizer(
                text,
                padding='max_length',
                max_length=max_length,
                truncation=True,
                return_tensors="pt"
            )
            tokens = {key: val.to(model.device) for key, val in tokens.items()}

           
            output = model(**tokens)
            _, predicted_class = torch.max(output.logits, dim=1)
            predictions.append(predicted_class.item())
    return predictions


def sub_to_main(predicted_label):
    classifier = joblib.load('random_forest_model.joblib')
    tfidf = joblib.load('tfidf_vectorizer.joblib')

   
    sample_sub_category = [int_to_label[predicted_label]] 
    sample_tfidf = tfidf.transform(sample_sub_category)
    predicted_category = classifier.predict(sample_tfidf)
    return predicted_category[0]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        unknown_text = request.form["unknown_text"]
        
        
        predicted_classes = predict(model, tokenizer, [unknown_text])
        predicted_label = predicted_classes[0]  
        predicted_sub_category = int_to_label[predicted_label]

        
        category = sub_to_main(predicted_label)
        
        return render_template("index.html", predicted_sub_category=predicted_sub_category, category=category, unknown_text=unknown_text)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
