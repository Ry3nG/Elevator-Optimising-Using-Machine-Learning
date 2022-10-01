"""
Why did we join the hackathon??
FML 
"""


import random

from RequestsGenerator import RequestGenerator

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


def SCAN_v3(r: RequestGenerator, head):
    overall_distance = 0
    seek_sequence = [head]

    reqs = r.requests.copy()

    print("\nSCAN :3\n")
    print(f"Head\t\t\t: {head}")

    i = 0

    is_going_up = True

    # Get next closest request to determine whether the elevator is going up or down
    while r.requests or r.tick < 287:
        # Get next closest request in the direction of the elevator
        if not r.requests:
            r.next_tick()
            continue

        next_request = get_closest_requests_in_direction(r.requests, head, is_going_up)
        while next_request is None:
            is_going_up = not is_going_up
            next_request = get_closest_requests_in_direction(
                r.requests, head, is_going_up
            )

        r.requests = [x for x in r.requests if x != next_request]
        seek_sequence.append(next_request)

        # Calculate distance to travel to next request
        distance = abs(head - next_request)
        overall_distance += distance
        head = next_request

        # Add more requests every 4 iter
        i += 1
        if i % 4 == 0:
            i = 0
            r.next_tick()
            print(
                f"Seek sequence\t\t: {' -> '.join([str(i) for i in seek_sequence])}\n"
            )

    print(f"Requests\t\t: {' '.join([str(i) for i in reqs])}")
    print(f"Total distance travelled: {overall_distance}")
    print(f"Seek sequence\t\t: {' -> '.join([str(i) for i in seek_sequence])}")
    print("\n")


if __name__ == "__main__":
    reqs = [random.randint(1, HEIGHT) for _ in range(SIZE)]
    head = random.randint(1, HEIGHT)
    r = RequestGenerator()
    SCAN_v3(r, 1)

"""
Don't mind this move along
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
    print("\n")"""