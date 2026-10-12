import pytest
from app import app

# cria um cliente de teste falso para não precisarmos subir o servidor real
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    resposta = client.get ('/')
    assert resposta.status_code == 200

def test_home_mensagem(client):
    resposta = client.get('/')
    dados = resposta.get_json()
    assert dados['mensagem'] == "Bem-vindo a API FastOrder!"

def test_soma(client):
    # Envia uma requisição GET simulada com os parâmetros a=10 e b=5
    resposta = client.get('/api/soma?a=10&b=5')
    
    # Verifica se a API respondeu com sucesso (HTTP 200 OK)
    assert resposta.status_code == 200
    
    # Extrai o corpo da resposta convertido para um dicionário Python
    dados = resposta.get_json()
    
    # Verifica se a chave 'resultado' existe e se o valor é exatamente 15
    assert dados['resultado'] == 15    