from django.shortcuts import render
import paypalrestsdk

paypalrestsdk.configure({
    "mode": "sandbox",
    "client_id": "AQwcWHO9p0_cy2P4xfr36FvYUEYmvzn2fLzOgzbylkdfcP3YECxWiCJ4NlVzTyu_bkhQFx4q3mp7VcLe",
    "client_secret": "EDkhLXQC2ndCkKXn8oUDS7Cn2-OxWgpdEZ97xz4aN8tsFRCZS3ceDuJAIa-8vFpzHl6C-YGXX33CS7yK"
})

# Create your views here.
