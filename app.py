from flask import Flask, render_template, request, jsonify
import urllib.request
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    name = data.get('name')
    skills = data.get('skills')
    experience = data.get('experience')

    prompt = f"Generate a professional resume for {name}. Skills: {skills}. Experience: {experience}. Make it clean and professional."

    payload = json.dumps({
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 1000,
        "messages": [{"role": "user", "content": prompt}]
    }).encode('utf-8')

    req = urllib.request.Request(
        'https://api.anthropic.com/v1/messages',
        data=payload,
        headers={
            'Content-Type': 'application/json',
            'x-api-key': 'YOUR_API_KEY_HERE',
            'anthropic-version': '2023-06-01'
        }
    )

    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read())
        resume_text = result['content'][0]['text']

    return jsonify({'resume': resume_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)