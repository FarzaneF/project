class Queue:
    #max-size: size of Q
    #Q: Array

    def __init__ (self, max_size):
        self.max_size = max_size
        self.Q = [0] * max_size
        self.num = 0
        self.first = 0
#------------------------------------------
        
    def enqueue(self,item):
        if self.num >= self.max_size:
            raise Exception("Queue overflow")
        self.Q[(self.num + self.first) % self.max_size] = item
        self.num +=1 
#-------------------------------------------
    def dequeue(self):
        if self.num == 0:
            raise Exception("Queue empty")
        item=self.Q[self.first]
        self.first=(self.first + 1) % self.max_size
        self.num-=1
        return item
#-------------------------------------------
    def front(self):
        if self.num==0:
            raise Exception("Queue empty")
        return self.Q[self.first]
#--------------------------------------------
    def is_empty(self):
        return self.num==0
#--------------------------------------------
    def size(self):
        return self.num

#--------------------------------------------
    def is_full(self):
        return self.num >= self.max_size
    
#--------------------------------------------
from queue import Queue

def get_nth_element(queue, n):
    if n < 1 or n > queue.qsize():
        return None  # اگر n از محدوده اعداد مجاز صف خارج شود، مقدار None برمی‌گردانیم

    for _ in range(n - 1):
        queue.put(queue.get())  # عنصر‌هایی که قبل از عنصر مورد نظر قرار دارند، دوباره به صف اضافه می‌شوند

    result = queue.get()  # عنصر مورد نظر را از صف خروجی می‌دهیم

    while not queue.empty():
        queue.put(queue.get())  # سایر عناصر صف دوباره به صف اضافه می‌شوند
    return result

q = Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)

print(get_nth_element(q, 3))  # این دستور 3 را چاپ خواهد کرد




 #******************************************   
# q=Queue(10)
# q.enqueue("ra'na")
# q.enqueue("vez")
# q.enqueue("Arya")
# print("queue size is:",q.size())
# print(q.dequeue(),"left the queue")
# print("front of queue is:", q.front())

# q.enqueue("milad")
# q.dequeue()
# q.dequeue()
# q.dequeue()
# print("it was a queue")