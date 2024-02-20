import time
import os

message = "Stop trying to teach a goldfish to juggle – you're splashing water everywhere and confusing the fish!"

padding = 25

format_message = " " * padding + message + " " * padding

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(format_message)
    format_message = format_message[1:] + format_message[0]
    time.sleep(0.1)
