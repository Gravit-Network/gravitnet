from queue import dequeue

def run():
    while True:
        action = dequeue()
        print("Processing:", action)

if __name__ == "__main__":
    run()
