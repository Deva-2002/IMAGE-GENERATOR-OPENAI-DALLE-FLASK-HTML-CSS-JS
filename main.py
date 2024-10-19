from flask import Flask, jsonify
from config import key
import openai
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generateimages/<prompt>')
def generate(prompt):
    print("prompt: ", prompt)
    response = openai.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=3,
    )
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
