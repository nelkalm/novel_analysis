# This program performs a natural language parsing analysis using the two novels:
# Oscar Wilde’s The Picture of Dorian Gray or Homer’s The Iliad. User can find out
# the main topics of discussion in the novel parsed by this program.

from nltk import pos_tag, RegexpParser
from nltk.tokenize import word_tokenize, sent_tokenize
from counter import vp_chunk_counter, np_chunk_counter

# import text of choice
text = open("the_iliad.txt", encoding='utf-8').read().lower()

# sentence and word tokenize text
sent_text = sent_tokenize(text)
# print(sent_text)

# store and print any word tokenized sentence
tokenized_word = list()

# create a list to hold part-of-speech tagged sentences
pos_tagged_text = list()

# for loop through each word tokenized sentence
# part-of-speech tag each sentence and append to list of pos-tagged sentences
# store and print any part-of-speech tagged sentence
for sentence in sent_text:
    tokenized_text = word_tokenize(sentence)
    tagged = pos_tag(tokenized_text)
    tokenized_word.append(tokenized_text)
    pos_tagged_text.append(tagged)

# print(tokenized_word)
# print(pos_tagged_text)

# define noun phrase chunk grammar
np_chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"

# create noun phrase RegexpParser object
np_chunk_parser = RegexpParser(np_chunk_grammar)

# define verb phrase chunk grammar
vp_chunk_grammar = "VP: {<NN><VB.*><RB.?>}"

# create verb phrase RegexpParser object
vp_chunk_parser = RegexpParser(vp_chunk_grammar)

# create a list to hold noun phrase chunked sentences and a list to hold verb phrase chunked sentences
np_chunked_text = list()
vp_chunked_text = list()

# create a for loop through each pos-tagged sentence
# chunk each sentence and append to lists
for pos_tagged in pos_tagged_text:
    chunked_noun_phrase = np_chunk_parser.parse(pos_tagged)
    np_chunked_text.append(chunked_noun_phrase)
    chunked_verb_phrase = vp_chunk_parser.parse(pos_tagged)
    vp_chunked_text.append(chunked_verb_phrase)

# store and print the most common NP-chunks here
most_common_np_chunks = np_chunk_counter(np_chunked_text)
print(most_common_np_chunks)

# store and print the most common VP-chunks here
most_common_vp_chunks = vp_chunk_counter(vp_chunked_text)
print(most_common_vp_chunks)
