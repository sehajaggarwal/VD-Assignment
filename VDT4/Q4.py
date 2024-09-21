#QUESTION 4
#----------------

import time
import threading
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

class rate_limiter:
    # Initialise the rate limiter 
    def __init__(self, max_requests: int, time_window: int):
        self.max_requests = max_requests
        self.time_window = time_window
        self.user_requests = defaultdict(list) # holds user request timestamps
        self.lock = threading.Lock()  # lock for thread safety

    # Checks if user is allowwed to make a request 
    def allow_request(self, user_id: str) -> bool:
        current_time = time.time()
        
        with self.lock: #allows concurrent access to data
            # Retrieve all requests for the user
            requests = self.user_requests[user_id]
            
            # Remove requests older than the time window
            self.user_requests[user_id] = [
                timestamp for timestamp in requests
                if current_time - timestamp < self.time_window
            ]
            
            # Check if user is within the request limit
            if len(self.user_requests[user_id]) < self.max_requests:
                self.user_requests[user_id].append(current_time)
                return True
            else:
                return False
            
#Test the solution:

# Function to simulate user behaviour for testing
def make_requests(rate_limiter, user_id, num_requests, wait_time):
    for i in range(num_requests):
        allowed = rate_limiter.allow_request(user_id)
        print(f"User {user_id} Request {i + 1} allowed: {allowed}")
        time.sleep(wait_time)

if __name__ == "__main__":

    rate_limiter = rate_limiter(max_requests=5, time_window=60)

    # Multiple users making requests concurrently
    users = ["user_1", "user_2", "user_3"]
    
    # Number of requests each user makes and delay between requests
    num_requests = 7
    wait_time_between_requests = 10  

    # Use ThreadPoolExecutor to simulate concurrent requests
    with ThreadPoolExecutor(max_workers=len(users)) as executor:
        for user in users:
            executor.submit(make_requests, rate_limiter, user, num_requests, wait_time_between_requests)

    """Expected Result will allow all users to make first 5 requests concurrently, 
    however, the 6th request will be denied as user exceeds permissible limit in the current minute.
    Now, the 7th request will be placed at the 70th second i.e. after more than a minute from the first request
    hence, it will be again allowed"""