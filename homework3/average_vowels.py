# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Put this function right here:
def counting_vowels_and_consonants(text):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    
    for char in text:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return (v_count, c_count)

# --- 2. Average Vowels ---
# Put this second function here:
def average_vowels_and_consonants(paragraph):
    # Split the paragraph into individual sentences (splitting by punctuation)
    # This regex-like split handles periods, exclamation points, and question marks
    import re
    sentences = re.split(r'[.!?]\s*', paragraph)
    sentences = [s for s in sentences if s] # Remove any empty strings
    
    num_sentences = len(sentences)
    total_v = 0
    total_c = 0
    
    for s in sentences:
        # Using your first function to count values for each sentence
        v, c = counting_vowels_and_consonants(s)
        total_v += v
        total_c += c
        
    avg_v = total_v / num_sentences
    avg_c = total_c / num_sentences
    
    return (num_sentences, avg_v, avg_c)

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# --- Output ---
# First, call the function and save the results
num_s, avg_v, avg_c = average_vowels_and_consonants(paragraph)

# Write descriptive print statements, with f-strings, at the bottom:
print(f"The Feynman paragraph contains {num_s} sentences.")
print(f"On average, there are {avg_v:.2f} vowels in each sentence.")
print(f"On average, there are {avg_c:.2f} consonants in each sentence.")