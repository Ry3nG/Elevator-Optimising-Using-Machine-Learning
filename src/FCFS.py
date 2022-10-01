"""
Implementation of First Come First Serve (FCFS) algorithm :3
This code is based on code by Rajput-Ji, GeeksforGeeks
"""

import random

SIZE = 10
HEIGHT = 100


def FCFS(reqs, head):
    overall_distance = 0
    seek_sequence = [head]

    print("\nFirst Come First Serve :3\n")
    print(f"Requests\t\t: {' '.join([str(i) for i in reqs])}")
    print(f"Head\t\t\t: {head}")

    for req in reqs:
        next_request = req
        seek_sequence.append(req)
        distance = abs(next_request - head)
        overall_distance += distance
        head = next_request

    print(f"Total distance travelled: {overall_distance}")
    print(f"Seek sequence\t\t: {' -> '.join([str(i) for i in seek_sequence])}")
    print("\n")


if __name__ == "__main__":
    reqs = [random.randint(1, HEIGHT) for _ in range(SIZE)]
    head = random.randint(1, HEIGHT)
    FCFS(reqs, head)
