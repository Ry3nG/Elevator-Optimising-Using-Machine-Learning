import random


class RequestGenerator:
    def __init__(self, floor_count=20, busy_floors=[2, 5, 6, 10, 14]) -> None:
        # We need create information on which time of the day is busy, and which floor is most commonly chose
        # Time interval -> 0030
        # e.g.
        # Floor count: 20
        # Busy floors: 2, 5, 6, 10, 14
        # Ground floor
        # Busy period -> 1, not busy period -> 0, not working period -> 2
        # 0700 - 0900: working time, more ground floor to busy floors requests
        # 1200 - 1330: lunch time, more ground to busy floors requests
        # 1700 - 1800: pangkang, more busy floors to ground floors requests
        # Rest of the 0800 - 1900: less calls, all floors have same probability of being called to, but busy floors have slightly higher probability
        # Others: even less calls,
        self.floor_count = floor_count
        self.busy_floors = busy_floors
        self.non_busy_floor = list(
            x for x in range(1, floor_count + 1) if x not in busy_floors
        )
        self.time_series = [2] * 48  # Each element represents 30 min
        self.init_time_series()
        self.requests = []
        self.init_requests()
        self._new_req = 0

        self.time_series_index = 0  # 0 means 0000, 3 means 0130, etc.
        self.tick = 0  # 1 tick represents 5 min, so 24 hr has 288 ticks

    def init_time_series(self):
        """Custom time series initialisation"""
        self.time_series[14:18] = [1 for _ in range(4)]
        self.time_series[18:24] = [0 for _ in range(6)]
        self.time_series[24:27] = [1 for _ in range(4)]
        self.time_series[27:34] = [0 for _ in range(7)]
        self.time_series[34:36] = [1 for _ in range(2)]

    def init_requests(self):
        """Populate initial requests"""
        pass

    def next_time(self):
        """Go next time interval"""
        self.time_series_index += 1

    def _create_next_requests_util(self):
        """Create more requests, requests come in pair"""
        business = self.time_series[self.time_series_index]

        non_busy_period_busy_floors_percentage = 40
        busy_period_busy_floors_percentage = 75

        if business == 0:
            for _ in range(2):
                if random.randint(1, 100) < non_busy_period_busy_floors_percentage:
                    new_req = random.sample(self.busy_floors, 1)[0]
                    self.requests.append(new_req)
                    yield new_req
                else:
                    new_req = random.sample(self.non_busy_floor, 1)[0]
                    self.requests.append(new_req)
                    yield new_req
        elif business == 1:
            for _ in range(2):
                if random.randint(1, 100) < busy_period_busy_floors_percentage:
                    new_req = random.sample(self.busy_floors, 1)[0]
                    self.requests.append(new_req)
                    yield new_req
                else:
                    new_req = random.sample(self.non_busy_floor, 1)[0]
                    self.requests.append(new_req)
                    yield new_req
        elif business == 2:
            for _ in range(2):
                new_req = random.sample(self.non_busy_floor + self.busy_floors, 1)[0]
                self.requests.append(new_req)
                yield new_req

    def create_next_requests(self):
        """Create more requests, requests come in pair"""
        business = self.time_series[self.time_series_index]
        frequency_of_requests = 0
        if business == 0:
            frequency_of_requests = random.randint(1, 4)
        elif business == 1:
            frequency_of_requests = random.randint(4, 6)
        elif business == 2:
            frequency_of_requests = (
                0 if random.randint(0, 100) < 90 else 1
            )  # very low chance of call

        self._new_req = frequency_of_requests

        # Print info
        print(f"Tick {self.tick}")

        new_reqs = []
        for _ in range(frequency_of_requests):
            new_reqs = [x for x in self._create_next_requests_util()]
            print(f"New requests: {' '.join([str(x) for x in new_reqs])}")
        
        if new_reqs:
            print(f"Current requests: {self.requests}\n")

        self.tick += 1
        self.time_series_index = self.tick // 6

    def next_tick(self):
        if self.tick >= 288:
            return
        self.create_next_requests()


if __name__ == "__main__":
    reqs = RequestGenerator()

    """
    Requests list is reqs.requests
    Every few iteration of the algo, call reqs.next_tick(), this will automatically append new requests to end of the requests
    function should run until requests is completed and day is not over yet
    I don't know whether my configuration for the generator is good enough, could be generating too much requests idk :P

    e.g.
    r = RG()

    def algo(r, head):
        while r has requests or day is not over yet:
            seek_sequence = []

            serve_next_few_requests()  # maybe 3 - 5??

            r.next_tick # to get new requests for lift

        
    """

