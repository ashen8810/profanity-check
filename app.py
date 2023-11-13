from flask import Flask, request, jsonify
from profanity_check import predict

app = Flask(__name__)

def check_profanity(word):
    return predict([word])[0]

@app.route('/check_profanity', methods=['POST'])
def check_profanity_api():
    data = request.get_json()

    if 'sentence' not in data:
        return jsonify({'error': 'Missing "sentence" parameter'}), 400

    word = data['sentence']
    is_profane = check_profanity(word)

    response = {'sentence': word, 'is_profane': bool(is_profane)}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
