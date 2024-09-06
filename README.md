## Tsuru 3D
Este projeto tem por finalidade em aprender conceitos sobre webgl para redenrização de elementos 3D no browser, websockets para atualizar a lista de novos passaros conectados em tempo real e também para identificar a localização de cada passaro conectado utilizando a Geolocation API.

<img src="https://github.com/joseguilherme96/tsuru/blob/main/frontend/public/image.png?raw=true" style="display:inline;">

Foi utilizado o framework vue.js e a biblioteca three.js para renderizar o passáro em 3D.

O pássaro foi importado do site [(sketchfab)](https://skfb.ly/o8Pyt) que gera um arquivo na extensão .glb que é utilizado para criação de objetos 3D. Após baixado o modelo fiz a importação para dentro da biblioteca three.js onde pude ter acesso ao objeto onde pude alterar sua cor como outras propriedades que o arquivo oferece para alteração.

## Passaros ativos

É possível saber em tempo real quais pássaros que estão conectados, assim como a localização deles.

Foi utilizada também a biblioteca Socket.IO que permite conectar com uma API websocket feita em flask. Assim cada passaro conectado é enviado a informação para a API, onde ela faz um broadcast para todos os outros passaros conectados. Assim todos sabem quais passaros estão ativos e aonde estão, claro apenas se o usuário autorizar sua localização.

## Setup do projeto

### Pasta backend
Entre na pasta backend e instale as dependências com os seguintes comandos :

#### Execute

```sh
    pip install -r requirements.txt

```

Execute o flask

```sh
    flask run
```

### Pasta frontend

Abra a pasta frontend e execute os seguintes comandos :

#### Execute

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```
