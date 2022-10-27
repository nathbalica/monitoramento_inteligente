<p align="center">
<img src="resources/capa-project.jpg";/>
</p>


## 📖 Sobre
Projeto capaz de conectar ao servidor que um medidor está enviando as mensagens,
guardá-las em algum lugar e criar uma API para que consigamos buscar essas informações.
## 🚀 Tecnologias

Esse projeto foi desenvolvido com as seguintes  tecnologias:

- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Postgresql](https://www.postgresql.org/)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [MQTT](https://mqtt.org/)

## 💻 Projeto

Receber menssagens do broker através do hivemq e armazenando ao banco de dados Postgresql


## Como subir o projeto

Para subir é necessário rodar esse comando:
```bash
docker compose up -d --build
```

## comando para executar a api
```bash
python3 application.py
```
 - endoint para realizar o get: http://127.0.0.1:8080/get
 - fazer a requisicao como json:
```json
 {
	"mac_adress" : "<mac_name>",
	"date_inicial" : "2022-10-26 15:32:21.000",
	"date_final" : "2022-10-26 15:32:36.000"
}
```
    
