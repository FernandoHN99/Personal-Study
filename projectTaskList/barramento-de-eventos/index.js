const express = require('express');
const bodyParser = require('body-parser');
const net = require('net');
//para enviar eventos para os demais microsserviços
const axios = require('axios');
const app = express();
app.use(bodyParser.json());

const eventos = []

function checkPort(port) {
    return new Promise((resolve, reject) => {
      const client = net.createConnection(port, '192.168.15.168', () => {
        client.end();
        resolve(true);
      });
      client.on('error', () => {
        resolve(false);
      });
    });
  }

async function sendRequest(port, strRequest, evento) {
    const isPortOpen = await checkPort(port);
    if (isPortOpen) {
        axios.post(strRequest, evento);
    } else {
        console.log(`Porta ${port} não está disponível`);
    }
}

app.post('/eventos', (req, res) => {
    const evento = req.body;
    eventos.push(evento)

    //envia o evento para o microsserviço de lembretes
    sendRequest(4000, 'http://192.168.15.168:4000/eventos', evento)
    
    //envia o evento para o microsserviço de observações
    sendRequest(5001, 'http://192.168.15.168:5001/eventos', evento)
    
    //envia o evento para o microsserviço de consulta
    sendRequest(6000, 'http://192.168.15.168:6000/eventos', evento)
    
    //envia o evento para o microsservico de classificacao
    sendRequest(7001, 'http://192.168.15.168:7001/eventos', evento)

    res.status(200).send({ msg: "ok" });
});


app.get('/eventos', (req, res) => {
    res.send(eventos)
})

app.listen(10000, () => {
    console.log('Barramento de eventos. Porta 10000.')
})