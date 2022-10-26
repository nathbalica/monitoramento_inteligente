<p align="center">
<img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fzefiro.com.br%2Fcomo-e-a-estrutura-de-uma-rede-iot%2F&psig=AOvVaw2NxxmluQDhurWb5i3R4--P&ust=1666903223046000&source=images&cd=vfe&ved=0CA0QjRxqFwoTCJid6cXg_voCFQAAAAAdAAAAABAE";/>
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