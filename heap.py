class heap:

    def __init__(self, array):
        self.array = array
        self.position = (len(array)-1) #tracks the position of the part of the list that isn't solved
        
    def heapify(self):
        #left son - 2n
        #right son - 2n+1
        def swaps():
            for n in range(int((self.position+1)/2)):
                if self.array[n] < self.array[2*n]:
                    #swap parent with left son
                    self.array[n], self.array[2*n] = self.array[2*n], self.array[n]  
                    swaps()
                elif self.array[n] < self.array[2*n+1]:
                    #swap parent with right son
                    self.array[n], self.array[2*n+1] = self.array[2*n+1], self.array[n]
                    swaps()
        swaps()
        
    def max_heap(self):
        while (self.position >= 1): #replacing the last element with the first node and removing the last
            self.array[0], self.array[self.position] = self.array[self.position], self.array[0]
            self.position -= 1
            self.heapify()
        self.array.insert(0, self.array[-1])
        del self.array[-1]

    def __repr__(self):
        return str(self.array)
    

i = heap([1,7,8,2,18,9,32,21,2,3,4,5,6,7,8,9,10,1,2])
i.max_heap()
print(i)
