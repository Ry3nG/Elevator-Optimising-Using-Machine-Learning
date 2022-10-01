"""
Dont use this i just randomly pice code together
"""


import random

SIZE = 20
HEIGHT = 20


def get_closest_requests_in_direction(reqs, head, is_going_up):
    """
    Get next closest request in the direction of the elevator
    """
    # If is going up, ignore all request smaller than head, and vice versa
    if is_going_up:
        filtered_requests = list(filter(lambda x: x >= head, reqs))
        if not filtered_requests:
            return None
        next_request = min(filtered_requests, key=lambda x: x - head)
    else:
        filtered_requests = list(filter(lambda x: x < head, reqs))
        if not filtered_requests:
            return None
        next_request = min(filtered_requests, key=lambda x: head - x)

    return next_request


def SSTF_v2(reqs, head):
    reqs_copy = reqs.copy()
    overall_distance = 0
    seek_sequence = [head]

    print("\nShortest Seek Time First :3\n")
    print(f"Head\t\t\t: {head}")

    while reqs_copy:
        # Get next closest request
        next_request = min(reqs_copy, key=lambda x: abs(x - head))
        reqs_copy.remove(next_request)
        seek_sequence.append(next_request)

        # Calculate distance to travel to next request
        distance = abs(head - next_request)
        overall_distance += distance
        head = next_request

        # Add some subsequent requests to simulate elevator calls since not all elevator calls are simultaneous
        if random.randint(0, 4) == 1:
            request_length = random.randint(1, 4)
            reqs.append("\b,")
            for _ in range(request_length):
                new_request = random.randint(0, HEIGHT)
                reqs.append(new_request)
                reqs_copy.append(new_request)

    print(f"Requests\t\t: {' '.join([str(i) for i in reqs])}")
    print(f"Total distance travelled: {overall_distance}")
    print(f"Seek sequence\t\t: {' -> '.join([str(i) for i in seek_sequence])}")
    print("\n")


def SCAN_v2(reqs, head):
    reqs_copy = reqs.copy()
    overall_distance = 0
    seek_sequence = [head]

    print("\nSCAN :3\n")
    # print(f"Requests\t\t: {' '.join([str(i) for i in reqs])}")
    print(f"Head\t\t\t: {head}")

    # Get next closest request to determine whether the elevator is going up or down
    next_request = min(reqs_copy, key=lambda x: abs(x - head))
    is_going_up = head < next_request

    while reqs_copy:
        # Get next closest request in the direction of the elevator
        next_request = get_closest_requests_in_direction(reqs_copy, head, is_going_up)
        while next_request is None:
            is_going_up = not is_going_up
            next_request = get_closest_requests_in_direction(
                reqs_copy, head, is_going_up
            )

        reqs_copy.remove(next_request)
        seek_sequence.append(next_request)

        # Calculate distance to travel to next request
        distance = abs(head - next_request)
        overall_distance += distance
        head = next_request

        # Add some subsequent requests to simulate elevator calls since not all elevator calls are simultaneous
        if random.randint(0, 4) == 1:
            request_length = random.randint(1, 4)
            reqs.append("\b,")
            for _ in range(request_length):
                new_request = random.randint(0, HEIGHT)
                reqs.append(new_request)
                reqs_copy.append(new_request)

    print(f"Requests\t\t: {' '.join([str(i) for i in reqs])}")
    print(f"Total distance travelled: {overall_distance}")
    print(f"Seek sequence\t\t: {' -> '.join([str(i) for i in seek_sequence])}")
    print("\n")


if __name__ == "__main__":
    reqs = [random.randint(1, HEIGHT) for _ in range(SIZE)]
    head = random.randint(1, HEIGHT)
    SSTF_v2(reqs, head)
    # SCAN_v2(reqs, head)
