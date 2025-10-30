class Solution:
    '''
    understand:
    given input words:an array of strings words
    k:return k most

    time:O(n + k log n).counting + heap ops

    space:O(m),Counter + heap storage


    match:
        use the counter first, calculate the frenquency of the words
        and then create pq:((-freqneuency),word) : max heap

        iterate k time, pop out the k most elements in the heap and then append to the res List
    
    '''
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq = Counter(words) #Counter format: word:freq
        res = []

        pq = [(-freq,word) for word, freq in word_freq.items()]
        heapq.heapify(pq) #build heap

        for _ in range(k):
            res.append(heapq.heappop(pq)[1])
        return res