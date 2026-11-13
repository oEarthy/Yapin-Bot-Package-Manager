import yapper
import os
import time
from dotenv import load_dotenv

load_dotenv() # load environment variables from the .env file
bot = yapper.Bot(os.environ.get("YAPPER_BOT_TOKEN")) # get the bot token from the .env file
yapper.log_message("Starting...")

@bot.command("ping", "Is the bot alive?")
def ping(msg):
    started = time.perf_counter()
    response = msg.reply("pong 🏓")
    latency_ms = round((time.perf_counter() - started) * 1000)
    bot.edit(msg.channel_id, response["id"], content=f"pong 🏓 (estimated ping: {latency_ms} ms)")

bot.run()
