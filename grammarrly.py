import textblob
from textblob import TextBlob
a = TextBlob(input("Enter a sentence: "))
print(a.correct())