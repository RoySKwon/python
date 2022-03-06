# queue_without_deque.py
import time

startTime = time.time();

queue = list();

print(queue);

queue.append(5);
queue.append(2);
queue.append(3);
queue.append(7);
print(queue);

queue.pop();
print(queue);

queue.append(1);
queue.append(4);
print(queue);

queue.pop();
print(queue);

queue.reverse();
print(queue);

endTime = time.time();
print("Total Time:", endTime - startTime);
