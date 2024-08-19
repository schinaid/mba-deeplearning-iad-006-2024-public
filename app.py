from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Carregar o modelo treinado
with open('./app/model/modelo_DecisionTree.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/main', methods=['POST'])
def main():
    data = request.json
    prediction = model.predict([data['features']])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)