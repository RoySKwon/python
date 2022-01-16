# queue01
# FIFO

from collections import deque

#push
queue = deque();
print(queue);

queue.append(5);
print(queue);

queue.append(2);
print(queue);

queue.append(3);
print(queue);

queue.append(7);
print(queue);


#pop
""" 
queue.pop();
print(queue);
 """

queue.popleft();
print(queue); 

queue.append(1);
print(queue);

queue.append(4);
print(queue);

queue.popleft();
print(queue);

queue.reverse();
print(type(queue), queue);

listQueue = list(queue);
print(type(listQueue), listQueue);
