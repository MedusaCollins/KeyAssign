import multiprocessing
import keyCaptures
import actions
import sys

if __name__ == "__main__":
    try:
        queue = multiprocessing.Queue()
        # keyCaptures process start
        captureProcess = multiprocessing.Process(target=keyCaptures.startKeyCapture, args=(queue, sys.argv))
        captureProcess.start()
        
        # actions process start
        actionsProcess = multiprocessing.Process(target=actions.processKeyEvents, args=(queue, sys.argv))
        actionsProcess.start()
        
        captureProcess.join()
        actionsProcess.join()
    except KeyboardInterrupt:
        print("Keyboard interrupt received, exiting from the program.");
        captureProcess.terminate()
        actionsProcess.terminate()
