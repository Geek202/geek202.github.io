# generated the shake effect for the 404 page.
import random

for i in range(101):
    print(f"""{i}% {{ transform: translate({random.randint(0, 10)}%, {random.randint(0, 10)}%); }}""")
