from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    original = request.json['original'].strip()
    typed = request.json['typed'].strip()
    start_time = float(request.json['startTime'])
    end_time = time.time()

    time_taken = end_time - start_time
    word_count = len(typed.split())
    wpm = (word_count / time_taken) * 60 if time_taken > 0 else 0

    correct_chars = sum(1 for o, t in zip(original, typed) if o == t)
    total_chars = max(len(original), len(typed))
    accuracy = (correct_chars / total_chars) * 100 if total_chars > 0 else 0

    return jsonify({
        'time': round(time_taken, 2),
        'wpm': round(wpm, 2),
        'accuracy': round(accuracy, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)