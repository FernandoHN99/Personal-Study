const express = require('express');
const bodyParser = require('body-parser');
const axios = require("axios");
const net = require('net');


const app = express();
app.use(bodyParser.json());

const lembretes = {};
contador = 0

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

app.get ('/lembretes', (req, res) => {
    res.send(lembretes)
}); 

app.put("/lembretes", async (req, res) => {
    contador++;
    const { texto } = req.body;
    lembretes[contador] = {
        contador, texto
    }

    const port = 10000;
    const isPortOpen = await checkPort(port);

    // if (isPortOpen) {
    if (true) {
        await axios.post("http://barramento-de-eventos-service:10000/eventos", {
            tipo: "LembreteCriado",
            dados: {
                contador,
                texto,
            },
        });
    } else{
        console.log(`Porta ${port} não está disponível`);
    }
    res.status(201).send(lembretes[contador]);
});

app.post("/eventos", (req, res) => {
    console.log(req.body);
    res.status(200).send({ msg: "ok" });
});

app.listen(4000, () => {
    console.log("Agora usando o Docker Hub");
    console.log('Lembretes. Porta 4000');
});


