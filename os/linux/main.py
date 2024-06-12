import multiprocessing
import keyCaptures
import actions

if __name__ == "__main__":
    try:
        queue = multiprocessing.Queue()
        # keyCaptures process start
        capture_process = multiprocessing.Process(target=keyCaptures.start_key_capture, args=(queue,))
        capture_process.start()
        
        # actions process start
        actions_process = multiprocessing.Process(target=actions.process_key_events, args=(queue,))
        actions_process.start()
        
        capture_process.join()
        actions_process.join()
    except KeyboardInterrupt:
        print("Keyboard interrupt received, exiting from the program");
        capture_process.terminate()
        actions_process.terminate()
