# Crée un fichier "tweet_bot.py" avec ce contenu :
import tweepy
import os

# Authentification via les variables d'environnement (sécurisées)
api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_secret = os.getenv("TWITTER_ACCESS_SECRET")

# Configuration de l'authentification
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
api = tweepy.API(auth)

# Liste de tweets à publier automatiquement
tweets = [
    "Hello Twitter! 🤖 #BotTwitter",
    "Je suis un bot qui tweete automatiquement grâce à GitHub Actions! 🚀",
    "Les bots sont cools, pas vrai? 😎",
]

# Publier un tweet
def publier_tweet():
    for tweet in tweets:
        try:
            api.update_status(tweet)
            print(f"Tweet posté : {tweet}")
        except Exception as e:
            print(f"Erreur lors de la publication : {e}")

if __name__ == "__main__":
    publier_tweet()
