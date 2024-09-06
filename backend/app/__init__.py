from flask import Flask,render_template,request
from flask_socketio import SocketIO,emit
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

# Configurando o SocketIO
socketio = SocketIO(app, cors_allowed_origins="http://localhost:5173")

passaros_conectados = []

@app.route("/")
def index():

    return "API Websocket"


@socketio.on('adiciona_informacoes_para_passaro_conectado')
def handle_my_custom_event(data):

    data = json.loads(data)

    # Encontra a sid do passaro conectado e anexa o Nº do passaro junto a sid
    for (index,passaro) in enumerate(passaros_conectados):

        if(passaro['sid']== data.get('sid')):

            #Adiciona o numero do passaro junto a sid do passaro conectado
            passaros_conectados[index]['numero_passaro'] = data.get('numero_passaro')
            passaros_conectados[index]['localizacao'] = data.get('localizacao')

    #Emite lista atualizada com o numero do passaro anexado
    emit('response event connect', passaros_conectados,broadcast=True)

    
    
@socketio.on('connect')
def test_disconnect():
    sid = request.sid
    passaros_conectados.append({'sid':sid,'localizacao':'Local Desconhecido'})
    print(f'Client Connected {sid}')
    print(passaros_conectados)
    emit('response event connect', passaros_conectados,broadcast=True)
    emit('sid', {'sid': sid,'localizacao':'Desconhecida'})
    

@socketio.on('disconnect')
def test_disconnect():
    sid = request.sid 

    #Remove passaro conectado
    for (index,passaro) in enumerate(passaros_conectados):

        if(passaro['sid']==sid):

            del passaros_conectados[index]

    print(passaros_conectados)
    print(f'Client disconnected {sid}')
    emit('response event disconnected', passaros_conectados,broadcast=True)

if __name__ == '__main__':
    socketio.run(app)