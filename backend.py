from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def summarize_func():
    input_data = request.get_json()
    text = input_data.get('data')
    if not text:
        return jsonify({"error": "Please provide an input"}), 400
    
    try:
        summarized_text = generate_response(text)
        return jsonify({'summary': summarized_text}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def generate_response(text):
    headers = {
        "Content-Type": "application/json"
    }
    url = "http://localhost:11434/api/generate"  # ollama runs at this particular port
    systemPrompt = "Summarize the provided text in maximum 10 sentences (if possible less than 10), capturing all the key points of the text. Try your best not to take more than 10 sentences"
    payload = {
        "model": "phi3",
        "prompt": text,
        "system": systemPrompt,
        "stream": False,
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response_data = response.json()  
        return response_data.get('response')
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
