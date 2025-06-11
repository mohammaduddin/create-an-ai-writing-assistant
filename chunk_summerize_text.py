import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

text = """
Ducks are also called 'waterfowl' because they are normally found in places where there is water like ponds,
streams, and rivers. Ducks can live up to 20 years. Ducks are aquatic birds, often found near bodies
of water like ponds, lakes, and rivers. They belong to the family Anatidae, which also includes geese
and swans, but ducks are generally smaller in size.
"""

def summarize_text(text):
    stop_words = set(stopwords.words('english')) # Create a set of English stopwords for efficient lookup.
    sentences = sent_tokenize(text)             # Tokenize the input text into individual sentences.
    summary = []                                # Initialize an empty list to store the summary sentences.

    for sentence in sentences:                   # Iterate through each sentence.
        words = word_tokenize(sentence)          # Tokenize the current sentence into words.
        # Check if the sentence has more than 3 non-stop words (converting to lowercase).
        if len([word for word in words if word.lower() not in stop_words]) > 3:
            summary.append(sentence)             # If the condition is met, add the sentence to the summary.

    return ' '.join(summary[:3])                 # Join the first three sentences from the summary list into a single string.

# display summarize text
print(summarize_text(text))

