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