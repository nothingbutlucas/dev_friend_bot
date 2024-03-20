# Stickers ID Bot


## How to use it 🤖


1. Start Command

2. Send Sticker

3. Test it

## How to use it? 💻

Go to [developers_friend_sticker_bot](https://t.me/dev_friend_bot) and use it!

## How to run it on local?

### Get the image

#### Get it

Get the image from [here](https://hub.docker.com/repository/docker/nothingbutlucas/developers_friend_sticker_bot)

#### Or Build the image yourself

```bash
git clone https://github.com/nothingbutlucas/developers_friend_sticker_bot
cd developers_friend_sticker_bot
docker build -t developers_friend_sticker_bot:latest .
```

### Create the docker-compose yml

```yml
services:
  app:
    image: nothingbutlucas/developers_friend_sticker_bot:latest
    environment:
      TOKEN: "TEKKEN" # Este es el token que te dió botfather
      LOGGING_LEVEL: INFO
    command: ["python3", "-u", "main.py"] # Ejecución del bot
```

### Run docker-compose up

```bash
docker-compose up -d
```

## Credits 💳

Este bot se creo usando la libreria de [python-telegram-bot (PTB)](https://python-telegram-bot.org)
