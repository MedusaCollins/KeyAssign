def process_key_events(queue):
    while True:
        event = queue.get()
        if event:
            key, action, timestamp_or_duration = event
            if action == 'pressed':
                print(f"Key {key} pressed.")
            elif action == 'released':
                print(f"Key {key} released after {timestamp_or_duration:.2f} seconds")
