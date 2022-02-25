# ThreadSafeCounter

WordCounter class that is able to count words in large texts, so that a user of that class can quickly calculate how many times
a specific word occurs in a string.

WordCounter implements the following methods:

process_text(text) takes in a string, 'text' and updates the internal attributes of WordCounter in a thread-safe manner. 
It is assumed naively that text.split(" ") is good enough to return a list of words in the passed "text".

get_word_count(word) takes in a string, 'word', and checks how many times it occurs in all the texts that WordCounter has processed. If this word has
never been seen, it returns 0.

Note: This class is a thread-safe; meaning that many threads are able to use the WordCounter at the same time, and the calculations must remain accurate
as if only a single thread is using the instance of WordCounter.

Example of how it works:

=> wc = WordCounter()

=> wc.process_text("the cat is in the bag")

=> wc.get_word_count("the")

2

=> wc.get_word_count("bag")

1

=> wc.get_word_count("dog")

0

