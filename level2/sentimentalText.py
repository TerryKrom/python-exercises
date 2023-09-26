import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Certifique-se de baixar os recursos necessários do NLTK
nltk.download('vader_lexicon')

# Inicialize o analisador de sentimentos VADER
sia = SentimentIntensityAnalyzer()

def analisar_sentimento(text):
    sentiment = sia.polarity_scores(text)
    
    if sentiment['compound'] >= 0.05:
        return "Positive"
    elif sentiment['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Usage
texto = "Eu amo este produto! É incrível."
sentimento = analisar_sentimento(texto)
print(f"Sentimento: {sentimento}")
