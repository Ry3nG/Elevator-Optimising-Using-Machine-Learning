"""
Implementation of Shortest Seek Time First (SSTF) algorithm :3
"""

import random

SIZE = 10
HEIGHT = 100


def SSTF(reqs, head):
    reqs_copy = reqs.copy()
    overall_distance = 0
    seek_sequence = [head]

    print("\nShortest Seek Time First :3\n")
    print(f"Requests\t\t: {' '.join([str(i) for i in reqs])}")
    print(f"Head\t\t\t: {head}")

    for _ in range(len(reqs_copy)):
        # Get next closest request
        next_request = min(reqs_copy, key=lambda x: abs(x - head))
        reqs_copy.remove(next_request)
        seek_sequence.append(next_request)

        # Calculate distance to travel to next request
        distance = abs(head - next_request)
        overall_distance += distance
        head = next_request

    print(f"Total distance travelled: {overall_distance}")
    print(f"Seek sequence\t\t: {' -> '.join([str(i) for i in seek_sequence])}")
    print("\n")


if __name__ == "__main__":
    reqs = [random.randint(1, HEIGHT) for _ in range(SIZE)]
    head = random.randint(1, HEIGHT)
    SSTF(reqs, head)
