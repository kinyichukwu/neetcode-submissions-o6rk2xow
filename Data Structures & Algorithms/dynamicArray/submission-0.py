class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.array = [0] * capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        # Check if array is full; if so, resize
        if self.length == self.capacity:
            self.resize()
            
        # Insert at the current length index
        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        # Soft delete: just decrease the length pointer
        if self.length > 0:
            self.length -= 1
        return self.array[self.length]

    def resize(self) -> None:
        # 1. Double the capacity
        self.capacity = 2 * self.capacity
        
        # 2. Create new array with new capacity
        new_arr = [0] * self.capacity
        
        # 3. Copy old elements to new array
        for i in range(self.length):
            new_arr[i] = self.array[i]
            
        # 4. Update the reference
        self.array = new_arr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity