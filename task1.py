from queue import Queue
from random import randint
from time import sleep

queue = Queue()

def generate_request(request_number):
    sleep(0.2)
    queue.put(request_number)
    print('Request #{} added to queue'.format(request_number))
    pass

def process_request():
    if not queue.empty():
        sleep(0.5)
        print("Request #{} processed".format(queue.get()))
    else:
        print("Queue is empty")

def main():
    prev_req_number = 0

    while True:
        count_of_new_requests = randint(1, 10)
        for _ in range(count_of_new_requests):
            generate_request(prev_req_number + 1)
            prev_req_number += 1

        count_of_requests_to_process = randint(1, 10)
        for _ in range(count_of_requests_to_process):
            process_request()


if __name__ == '__main__':
    main()
