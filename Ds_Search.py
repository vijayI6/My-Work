class Search:
    def __init__(self, lst=None):
        self.lst = lst if lst else list(range(1, 10))
        self.len = len(self.lst)
        print('LIST :', self.lst)

    def linearSearch(self):
        ele = int(input('Enter Search Element :'))
        for i in range(self.len):
            if self.lst[i] == ele:
                return i
        return -1

    def binarySearch(self):
        ele = int(input('Enter Search Element :'))
        low, high = 0, self.len - 1
        while low <= high:
            mid = (low + high) // 2
            if self.lst[mid] == ele:
                return mid
            elif self.lst[mid] < ele:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def changeList(self, lst):
        self.lst = lst
        self.len = len(self.lst)
        print('LIST :', self.lst)

    @staticmethod
    def displayDetails(ind):
        if ind == -1:
            print('Element Is Not Found In List.')
        else:
            print(f'Element Is Found at {ind} Index.')


if __name__ == '__main__':
    print('1. Linear Search\n2. Binary Search\n3. Change List')
    obj = Search()
    while True:
        choice = int(input('Enter Your choice :'))
        match choice:
            case 1:
                obj.displayDetails(obj.linearSearch())
            case 2:
                obj.displayDetails(obj.binarySearch())
            case 3:
                a = list(map(int, input('Enter a list:').split()))
                a.sort()
                obj.changeList(a)
            case -1:
                print('Byeee')
                break
            case _:
                print('Please Enter 1 or 2.')
