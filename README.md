# Stickers ID Bot


## How to use it 🤖


1. Start Command

2. Send Sticker

3. Test it

## How to use it? 💻

Go to [dev_friend_bot](https://t.me/dev_friend_bot) and use it!

## How to run it on local?

### Get the image

#### Get it

Get the image from [here](https://hub.docker.com/repository/docker/nothingbutlucas/dev_friend_bot) with this command:

```bash
docker pull nothingbutlucas/dev_friend_bot:latest
```

#### Or Build the image yourself

```bash
git clone https://github.com/nothingbutlucas/dev_friend_bot
cd dev_friend_bot
docker build -t dev_friend_bot:latest .
```

### Create the docker-compose yml

```yml
services:
  app:
    image: nothingbutlucas/dev_friend_bot:latest
    environment:
      TOKEN: "HERE_YOUR_TELEGRAM_TOKEN"
      LOGGING_LEVEL: INFO
    command: ["python3", "-u", "main.py"]
```

### Run docker-compose up

```bash
docker-compose up -d
```

## Credits 💳

Este bot se creo usando la libreria de [python-telegram-bot (PTB)](https://python-telegram-bot.org)
