import tweepy
import os
import time
from datetime import datetime

# Authentification via les variables d'environnement (sécurisées)
api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_secret = os.getenv("TWITTER_ACCESS_SECRET")

# Configuration de l'authentification
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
api = tweepy.API(auth)

# Publier un tweet avec l'heure actuelle
def publier_tweet():
    while True:
        # Obtenir l'heure actuelle
        now = datetime.now()
        heure = now.strftime("%H:%M:%S")

        # Créer le tweet avec l'heure actuelle
        tweet = f"Heure actuelle : {heure} 🕒"
        
        try:
            api.update_status(tweet)
            print(f"Tweet posté : {tweet}")
        except Exception as e:
            print(f"Erreur lors de la publication : {e}")
        
        # Attendre 2 minutes avant de publier à nouveau
        time.sleep(120)  # 120 secondes = 2 minutes

if __name__ == "__main__":
    publier_tweet()
