from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="static")

@app.route('/')
def serve_index():
    return send_from_directory(".",'index.html')

@app.route('/manifest.json')
def serve_manifest():
    return send_from_directory(".",'manifest.json')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
