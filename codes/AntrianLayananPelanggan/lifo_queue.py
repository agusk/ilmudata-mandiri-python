from queue import LifoQueue

lifo_queue = LifoQueue()
lifo_queue.put('Pelanggan 1')
lifo_queue.put('Pelanggan 2')
lifo_queue.put('Pelanggan 3')

while not lifo_queue.empty():
    current_customer = lifo_queue.get()
    print(f"Melayani {current_customer}")