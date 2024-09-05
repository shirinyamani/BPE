
from helper import get_stats, merge
class BasicTokenizer:
    def __init__(self):
        self.merges = {} #pair: idx
    
    def train():
        pass
    
    def encode(self, text): #text ---> ids
        raw_byte_text = text.encode('utf-8')
        ids = list(map(int, raw_byte_text))
        
        while len(ids) >=2:
            stats = get_stats(ids)
            pair = min(stats, key=lambda p: self.merges.get(p, float("inf")))
            if pair not in self.merges:
                break
            idx = self.merges[pair]
            ids = merge(ids, pair, idx)
        return ids
        
        # TODO: 
        #1. merge gotta be in base tokenizer and use in here!
    
    def decode():
        pass
    
    
    
if __name__ =="__main__":
    obj = BasicTokenizer()
    print(obj.encode("hi he software he let et go!"))