from flask import Flask, request, jsonify
import pickle
import numpy as np
from PIL import Image
import io
import base64

app = Flask(__name__)

# Carregar o modelo treinado
with open('./app/model/modelo_DecisionTree.pkl', 'rb') as f:
    model = pickle.load(f)

def preprocess_image(image_base64):
    # Decodificar a imagem base64
    image_data = base64.b64decode(image_base64)
    image = Image.open(io.BytesIO(image_data))
    
    # Redimensionar e converter a imagem para o formato adequado
    image = image.resize((8, 8))
    image_array = np.array(image.convert('L'))  # Converter para escala de cinza
    image_array = image_array.flatten()  # Achatar a imagem
    return image_array

@app.route('/main', methods=['POST'])
def main():
    data = request.json
    image_base64 = data['image']
    image_array = preprocess_image(image_base64)
    prediction = model.predict([image_array])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)