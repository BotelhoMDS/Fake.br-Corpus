from LeIA import SentimentIntensityAnalyzer
import pandas as pd

# use for testing the library LeIA

# Load the SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

teste  = [ "Eu te amo", "Eu te odeio", "Eu não", "amor", "ódio", "amo", "matar"]

for t in teste:
    print(t)
    print(analyzer.polarity_scores(t))
    print("\n")