# System Stats Bot

A simple telegram bot that sends the current stats (CPU, RAM and swap usage and disk quota) and allows the admin to grant access to other users after their request.

## Run

To start the bot, change environment variables in `.env.sample` with valid values and rename it to `.env`, then run `docker-compose up -d --build`.

You can also remove `ADMIN_ID` or set it to `-1` to automatically set the admin user as the first that runs the `/iamadmin` command in the bot chat.

## Add Commands

Just create a module in `commands` folder that has a `command` variable and a handle(Update, CallbackContext) function. This will be automatically loaded.
