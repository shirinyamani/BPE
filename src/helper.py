def get_stats(ids, count=None):
    
    count = {} if count is None else count
    for pair in zip(ids, ids[1:]):
        count[pair] = count.get(pair, 0) + 1
    return count



def merge(ids, pair, newidx):
    newids = []
    i = 0
    
    while i < len(ids):
        if i < len(ids) - 1 and ids[i] == pair[0] and ids[i+1]==pair[1]:
            newids.append(newidx)
            i += 2
        else:
            newids.append(ids[i])
            i += 1
    return newids