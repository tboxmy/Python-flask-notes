from datetime import datetime

now = datetime.now()
formatted_now = now.strftime("%A, %d %B, %Y at %X")
print("Hello, Flask! Its ", formatted_now)