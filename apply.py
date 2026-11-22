import os


secret = os.environ["HOWGOOD_SECRET"]

payload = {
    "name": "Kathy Snider",
    "email": "kathy.snider@tuta.com",
    "resume": "https://raw.githubusercontent.com/KathySnider/HowGood-exercise/main/docs/Kathy%20Snider%20Resume.pdf",
    "location": "Vancouver, WA, United States",
    "linkedin": "https://www.linkedin.com/in/kathyjosnider",
    "codeLink": "https://github.com/KathySnider/HowGood-exercise",
    "yearsPython": 7,
    "yearsDjango": 1,
    "repos": "https://place-picker-production.up.railway.app/",
    "notes": (
        "Place Picker is a live application and does not require a login, "
        "so you're welcome to try it directly."
    ),
}
