from flask import Flask, request, jsonify, render_template
import pickle
from preprocess import preprocess_text

app = Flask(__name__)

model = pickle.load(open('model_spam.pkl', 'rb'))
vectorizer = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        processed_text = preprocess_text(data['user_input'])

        vectorized_text = vectorizer.transform([processed_text])

        if vectorized_text.shape[0] == 1:
            prediction = model.predict(vectorized_text)
            output = 'Spam' if prediction[0] == 1 else 'Not spam'
        else:
            raise ValueError("Unexpected input shape.")

        return jsonify({'prediction': output})
    except Exception as e:
        return jsonify({'error': str(e)})



if __name__ == "__main__":
    app.run(debug = True)