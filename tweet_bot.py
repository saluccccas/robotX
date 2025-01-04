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

# Publier un tweet uniquement si les minutes sont un multiple de 2
def publier_tweet():
    while True:
        now = datetime.now()
        minutes = now.minute  # Récupère les minutes de l'heure

        # Vérifie si les minutes sont un multiple de 2
        if minutes % 2 == 0:
            heure = now.strftime("%H:%M:%S")
            tweet = f"Heure actuelle (minute paire) : {heure} 🕒"
            
            try:
                api.update_status(tweet)
                print(f"Tweet posté : {tweet}")
            except Exception as e:
                print(f"Erreur lors de la publication : {e}")
        
        # Attendre 60 secondes avant de vérifier à nouveau
        time.sleep(60)

if __name__ == "__main__":
    publier_tweet()
