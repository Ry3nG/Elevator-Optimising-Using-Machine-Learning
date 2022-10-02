"""
Why did we join the hackathon??
FML 
"""


import random

from RequestsGenerator import RequestGenerator

SIZE = 20
HEIGHT = 10


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

    while r.requests or r.tick < 287:
        # If no requests are avaiable go to next tick
        if not r.requests:
            new_reqs = [x for x in r.next_tick()]

            # Print info
            print(f"Tick {r.tick}")
            
            if new_reqs:
                print(f"New requests: {' '.join([str(x) for x in new_reqs])}")
                print(f"Current requests: {r.requests}\n")

            print(
                f"Seek sequence\t\t: {' -> '.join([str(i) for i in seek_sequence])}\n"
            )
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
            new_reqs = [x for x in r.next_tick()]

            # Print info
            print(f"Tick {r.tick}")
            
            if new_reqs:
                print(f"New requests: {' '.join([str(x) for x in new_reqs])}")
                print(f"Current requests: {r.requests}\n")

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
    r = RequestGenerator(floor_count=HEIGHT, busy_floors=[2, 5, 6, 10])
    SCAN_v3(r, 1)
