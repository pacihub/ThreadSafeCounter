import threading

class WordCounter:
    def __init__(self):
        self.lock = threading.Lock()
        self.word_counts = {}


    def process_text(self,text):
        text_words = text.split(" ")
        for i in text_words:

            self.lock.acquire() # putting lock here, b/c I'm modifying the data structure word_counts
            self.word_counts[i] = self.word_counts.get(i, 0) + 1
            self.lock.release()


    def get_word_count(self, word):
        self.lock.acquire()
        count = self.word_counts.get(word, 0)
        self.lock.release()
        return count