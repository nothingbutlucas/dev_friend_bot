# Stickers ID Bot


## How to use it 🤖


1. Start Command

2. Send Sticker

3. Test it

4. Demo:


[![Stickers ID bot video](https://img.youtube.com/vi/M-cf3XSMwNs/0.jpg)](https://www.youtube.com/watch?v=M-cf3XSMwNs)



## How to use it? 💻

Go to [developers_friend_sticker_bot](https://t.me/developers_friend_sticker_bot) and use it!

## How to run it on local?

### Get the image

#### Get it

Get the image from [here](https://hub.docker.com/repository/docker/nothingbutlucas/developers_friend_sticker_bot)

#### Or Build the image

##### Clone this repo

```
git clone https://github.com/nothingbutlucas/developers_friend_sticker_bot
cd developers_friend_sticker_bot
docker build -t developers_friend_sticker_bot:latest .
```

### Create the docker-compose yml

```
version: "3.9"
services:
  app:
    image: nothingbutlucas/developers_friend_sticker_bot:latest
    environment:
      TOKEN: "TEKKEN" # Este es el token que te dió botfather
      LOGGING_LEVEL: INFO
    command: ["python3", "-u", "main.py"] # Ejecución del bot
```

### Run docker-compose up

```
docker-compose up -d
```

## Credits 💳

Este bot se creo usando la libreria de [python-telegram-bot (PTB)](https://python-telegram-bot.org)
