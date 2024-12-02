from tweepy import Client
from dotenv import dotenv_values

class TweeterClient:
    def __init__(self):
        # Cargar las claves desde el archivo .env
        keys = dotenv_values()
        self.CONSUMER_KEY = keys["CONSUMER_KEY"]
        self.CONSUMER_SECRET = keys["CONSUMER_SECRET"]
        self.ACCESS_TOKEN = keys["ACCESS_TOKEN"]
        self.ACCESS_SECRET = keys["ACCESS_SECRET"]
        self.BEARER_TOKEN = keys["BEARER_TOKEN"]
        self.client = Client(bearer_token=self.BEARER_TOKEN,
                             consumer_key=self.CONSUMER_KEY,
                             consumer_secret=self.CONSUMER_SECRET,
                             access_token=self.ACCESS_TOKEN,
                             access_token_secret=self.ACCESS_SECRET)
        
    def get_user_tweets(self):
        try:
            # Obtener el ID del usuario autenticado
            user = self.client.get_me()
            user_id = user.data.id

            # Obtener los tweets del usuario autenticado (línea de tiempo de tu cuenta)
            tweets = self.client.get_users_tweets(id=user_id, max_results=5)  # Puedes cambiar max_results según lo necesites

            if tweets.data:
                for tweet in tweets.data:
                    print(f"{tweet.text}\n")
            else:
                print("No se encontraron tweets.")
        except Exception as e:
            print(f"Error al obtener los tweets: {e}")

    def sent_tweet(self, text):
        try:
            # Publicar un tweet
            response = self.client.create_tweet(text=text)
            print(f"Tweet publicado con ID: {response.data['id']}")
            return response
        except Exception as e:
            print(f"Error al publicar el tweet: {e}")
    
if __name__ == "__main__":
    tweeter_client = TweeterClient()
    tweeter_client.get_user_tweets()  # Muestra tus tweets más recientes
