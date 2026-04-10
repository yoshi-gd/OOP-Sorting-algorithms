class Sort:
    def __init__(self):
        self._list = []
        self._sorted_list = []

    def list(self, lst):
        self._list = lst

    @property
    def isSorted(self):
        return(all(self._list[i] <= self._list[i+1] for i in range(len(self._list)-1)))
    
    def sort_list(self):
        i=0
        while not self.isSorted:
            if self._list[i] > self._list[i+1]:
                self._list[i], self._list[i+1] = self._list[i+1], self._list[i]
                i+=1
            else:
                i=0
        return self._list

    def sorted_list(self):
        self._sorted_list = self.sort_list()
        print(self._sorted_list)
    
lst = [4, 3, 1, 6, 7]
sorteD = Sort()

sorteD.list(lst)

sorteD.sorted_list()