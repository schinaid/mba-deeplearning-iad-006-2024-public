from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Carregar o modelo treinado
model = joblib.load('model/modelo_DecisionTree.pkl')

@app.route('/predict', methods=['POST'])
def main():
    # Obter os dados do JSON da solicitação
    data = request.json
    # Converter os dados para um array numpy
    input_data = np.array(data['input']).reshape(1, -1)
    # Fazer a predição
    prediction = model.predict(input_data)
    # Retornar a resposta como JSON
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)