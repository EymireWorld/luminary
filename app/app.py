from flask import Flask, jsonify

from .api.router import router as api_router


app = Flask(__name__)
app.json.ensure_ascii = False
app.json.sort_keys = False
app.register_blueprint(api_router)


@app.get('/')
def main_page():
    data = {
        'root': app.root_path
    }

    print(
        app.url_map
    )
    
    return jsonify(data)
