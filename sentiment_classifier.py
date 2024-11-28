from transformers import pipeline

cls = pipeline('sentiment-analysis')

def analyze_review(review):
  # Check if the review has more than 512 tokens
  if len(review.split()) > 512:
    # If it does, split the review into chunks of 512 tokens
    review_chunks = [review[i:i+512] for i in range(0, len(review), 512)]
    
    # Analyze each chunk and return the average sentiment
    avg_sentiment = 0
    for chunk in review_chunks:
      avg_sentiment += cls(chunk)[0]['score']
      
    positive_chunks = 0
    negative_chunks = 0
    total_score = 0
    
    for chunk in review_chunks:
      result = cls(chunk)[0]
      total_score += result['score']
      if result['label'] == 'POSITIVE':
        positive_chunks += 1
      else:
        negative_chunks += 1
    
    if positive_chunks > negative_chunks:
      return 'POSITIVE', total_score / len(review_chunks)
    else:
      return 'NEGATIVE', total_score / len(review_chunks)

  else:
    # Analyze the review
    result = cls(review)[0]
    return result['label'], result['score']
  
  
def avg_sentiment(reviews):
  sentiment_scores = {'POSITIVE': 0, 'NEGATIVE': 0, 'NEUTRAL': 0}
  sentiment_counts = {'POSITIVE': 0, 'NEGATIVE': 0, 'NEUTRAL': 0}
  
  for review in reviews:
    sentiment, score = analyze_review(review['review'])
    
    sentiment_scores[sentiment] += score
    sentiment_counts[sentiment] += 1
    
  # Calculo el sentimiento predominante
  total_score = sum(sentiment_scores.values())
  weighted_sentiment = {k: v / total_score for k, v in sentiment_scores.items()}
  
  # Sacamos un sentimiento medio en forma de texto
  if weighted_sentiment['POSITIVE'] >= 0.85:
    return 'VERY POSITIVE 🎉'
  elif weighted_sentiment['POSITIVE'] >= 0.5:
    return 'POSITIVE 👍🏻'
  elif weighted_sentiment['NEGATIVE'] >= 0.85:
    return 'VERY NEGATIVE 💩'
  elif weighted_sentiment['NEGATIVE'] >= 0.5:
    return 'NEGATIVE 👎🏻'
  else:
    return 'NEUTRAL 🤷🏻‍♀️'