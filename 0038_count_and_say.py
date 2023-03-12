
class Solution:
    def countAndSay(self, n):
        sequence = "1"
        for i in range(n - 1):
            sequence = self.getNext(sequence)
        return sequence

    def getNext(self, sequence):
        i, next_sequence = 0, ""
        while i < len(sequence):
            count = 1
            while i < len(sequence) - 1 and sequence[i] == sequence[i + 1]:
                count += 1
                i += 1
            next_sequence += str(count) + sequence[i]
            i += 1
        return next_sequence
    
if __name__ == "__main__":
    for i in range(1, 4):
        print(Solution().countAndSay(i))
