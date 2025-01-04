import tweepy
import os
import time
from datetime import datetime

# Authentification via les variables d'environnement
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_secret = os.getenv("TWITTER_ACCESS_SECRET")

# Configuration de l'authentification
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_secret
)

# Publier un tweet uniquement si les minutes sont un multiple de 2
def publier_tweet():
    while True:
        now = datetime.now()
        minutes = now.minute
        print(f"Vérification des minutes : {minutes}")  # Log pour voir les minutes

        if minutes % 2 == 0:
            heure = now.strftime("%H:%M:%S")
            tweet = f"Heure actuelle (minute paire) : {heure} 🕒"
            print(f"Condition remplie, tweet à publier : {tweet}")  # Log du tweet

            try:
                response = client.create_tweet(text=tweet)
                print(f"Tweet posté avec succès : {response.data['id']}")
            except Exception as e:
                print(f"Erreur lors de la publication : {e}")
        
        # Attendre 60 secondes avant de vérifier à nouveau
        time.sleep(60)

if __name__ == "__main__":
    publier_tweet()
