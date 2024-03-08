from flask import Flask, jsonify


app = Flask(
    __name__
)
app.json.ensure_ascii = False
app.json.sort_keys = False


@app.route('/', methods= ['GET'])
def main_page():
    data = {
        'root': app.root_path
    }
    
    return jsonify(data)
