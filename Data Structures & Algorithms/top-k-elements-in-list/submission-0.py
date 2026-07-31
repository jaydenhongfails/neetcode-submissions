class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} #keep count of occuring keys
        res = [] #store the most occuring keys in a list

        for num in nums: #iterate through every number in nums
            if num not in freq: #setting a new number freq to 1
                freq[num] = 1
            else:
                freq[num] += 1 #increasing the already existing num by 1
        
        def get_freq(pair): #func to receive a (num, freq) pair
            return pair[1] #returns its freq so sorted() can compare

        #freq.items converts dict into (num, freq) pairs
        #key = get_freq sorts each pair by its freq
        #reverse=True orders by descending order
        sorted_pair = sorted(freq.items(), key = get_freq, reverse=True)


        for pair in sorted_pair[:k]: #iterates through from 0 to k-1
            res.append(pair[0]) #adds the num from each pair to list

        return res
        


