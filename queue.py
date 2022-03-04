# queue.py
# FIFO

from collections import deque;

queue = deque();
queue.append(5);
queue.append(2);
queue.append(3);
queue.append(7);
print(queue);

queue.popleft();
print(queue);

queue.append(1);
queue.append(4);
print(queue);
queue.popleft();
print(queue);
queue.reverse();
print(queue);
