from flask import Flask
from flask import request
import json
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    text = str(request.args.get('input'))
    character_count = len(text)
    data_set = {
        'text': text,
        'character_count': character_count,
        'timestamp': time.time()
    }
    json_data = json.dumps(data_set)
    return json_data

if __name__ == '__main__':
    app.run(debug=True)
