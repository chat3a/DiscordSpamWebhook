
# Made By github.com/chat3a
# https://guns.lol/cha_tea

from discord_webhook import DiscordWebhook
import time

spam = DiscordWebhook(url = "Webhook URL Here",
                      content = "Messages Here")
# Put the numbers you want to spam in the "selected_times".
# Default: 99
selected_times = 99
current_times = 0
while current_times <= selected_times:
    spam.execute()
    time.sleep(1)
    current_times += 1
    print(current_times)

print("Done!")







