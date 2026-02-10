from collections import deque
import sys

def queue(command):
    if command[0] == "push":
        q.append(int(command[1]))
    elif command[0] == "pop":
        return -1 if not q else q.popleft()
    elif command[0] == "size":
        return len(q)
    elif command[0] == "empty":
        return 1 if not q else 0
    elif command[0] == "front":
        return -1 if not q else q[0]
    elif command[0] == "back":
        return -1 if not q else q[-1]

N = int(sys.stdin.readline())
q = deque()
answer = []
for _ in range(N):
    command = sys.stdin.readline().split()
    result = queue(command)
    if result is not None:
        answer.append(str(result))

print("\n".join(answer))