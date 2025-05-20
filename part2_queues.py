# Δευτερο Μέρος 


# Βασικός κόμβος 
class Node:
    def __init__(self, data, priority=0):
        self.data = data              
        self.priority = priority      
        self.next = None              

#  Κλάση Queue (κανονική ουρά)
class Queue:
    def __init__(self):
        self.front = None  
        self.rear = None   

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

    def display(self):
        current = self.front
        print("Queue contents:")
        while current:
            print(f"  {current.data}")
            current = current.next

# Κλάση PriorityQueue (ουρά προτεραιότητας)

class PriorityQueue:
    def __init__(self):
        self.front = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data, priority):
        new_node = Node(data, priority)
        if self.is_empty() or priority > self.front.priority:
            new_node.next = self.front
            self.front = new_node
        else:
            current = self.front
            while current.next and current.next.priority >= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = self.front.next
        return temp.data

    def display(self):
        current = self.front
        print("Priority Queue contents:")
        while current:
            print(f"  {current.data} (Priority: {current.priority})")
            current = current.next


if __name__ == "__main__":
    print("Κανονική Ουρά (Ραντεβού):")
    q = Queue()
    q.enqueue("Ασθενής Γεωργίου")
    q.enqueue("Ασθενής Παπαδόπουλος")
    q.enqueue("Ασθενής Μαρκοπούλου")
    q.display()
    print("Εξυπηρετήθηκε:", q.dequeue())
    q.display()

    print("\nΟυρά Προτεραιότητας (Επείγοντα):")
    pq = PriorityQueue()
    pq.enqueue("Ασθενής Χ", 1)
    pq.enqueue("Ασθενής Ψ", 3)  # Υψηλότερη προτεραιότητα
    pq.enqueue("Ασθενής Ω", 2)
    pq.display()
    print("Εξυπηρετήθηκε:", pq.dequeue())
    pq.display()
