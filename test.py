def hashcode():
    hashval = 0
    for i in toHash:
        hashval = hashval * 31 + i
        return hashval % MAX_SIZE
