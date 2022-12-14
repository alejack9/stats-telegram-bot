# System Stats Bot

A simple telegram bot that sends the current stats (CPU, RAM and swap usage and disk quota) and allows the admin to grant access to other users after their request.

## Run

To start the bot, change environment variables in `.env.sample` with valid values and rename it to `.env`, then run `docker-compose up -d --build`.

## Todos

- [x] Refactoring for dynamic loading 
- [ ] `/iamadmin` command to set admin if `ADMIN_ID` env variable is empty
- [ ] `/kick` command to remove access to a user
- [ ] `/ban` command to prevent user to make requests
- [ ] `/unban` command to unban a user
- [ ] not propagate `/ask` if user is already saved
