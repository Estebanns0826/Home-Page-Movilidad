from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_db():
    if 'file' not in request.files:
        return 'No file part in request', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    # Guarda siempre en la raíz como 'registro_equipos.db'
    save_path = os.path.join(os.getcwd(), 'registro_equipos.db')
    file.save(save_path)
    
    return 'Database updated successfully', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
