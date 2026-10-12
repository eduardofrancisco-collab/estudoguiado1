from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"mensagem": "Bem-vindo a API FastOrder!"})

@app.route('/api/status')
def status():
    return jsonify({"status": "Operacional", "serviço": "FastOrder-Web"})

@app.route('/api/soma')
def soma():
    # Captura os parâmetros 'a' e 'b' passados na Query String
    a = request.args.get('a')
    b = request.args.get('b')
    
    # Validação básica de segurança
    if a is None or b is None:
        return jsonify({"erro": "Forneça os parâmetros 'a' e 'b'."}), 400
        
    try:
        # Converte as strings para float
        valor_a = float(a)
        valor_b = float(b)
        
        # Realiza a soma matemática
        soma_total = valor_a - valor_b
        
        # Retorna o dicionário convertido em JSON
        return jsonify({"resultado": soma_total})
        
    except ValueError:
        # Trata o erro caso o utilizador envie texto
        return jsonify({"erro": "Os parâmetros devem ser números válidos."}), 400

# O bloco de arranque principal fica encostado à margem esquerda
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)