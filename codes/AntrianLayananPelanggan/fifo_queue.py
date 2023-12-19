from queue import Queue

fifo_queue = Queue()
fifo_queue.put('Pelanggan 1')
fifo_queue.put('Pelanggan 2')
fifo_queue.put('Pelanggan 3')

while not fifo_queue.empty():
    current_customer = fifo_queue.get()
    print(f"Melayani {current_customer}")