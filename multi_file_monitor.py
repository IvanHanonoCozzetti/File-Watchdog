import time
import logging
import multiprocessing
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

event_handler = LoggingEventHandler()
observer = Observer()

folder = "C:/Users/Ivan/Downloads"
folder1 = "C:/Users/Ivan/Desktop"
folder2 = "C:/Users/Ivan/Documents"


# Activity display
def monitor_folder(folder):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%d-%m-%Y %H:%M:%S')
    
    observer.schedule(event_handler, folder, recursive=True)
    observer.start()

    try:
        while True:
            #Thread sleep time
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("File monitor deactivated.")
    observer.join()


# Start running the monitor in each folder (Multiprocessing)
if __name__ == "__main__":
    m = multiprocessing.Process(target=monitor_folder, args=(folder,))
    m1 = multiprocessing.Process(target=monitor_folder, args=(folder1,))
    m2 = multiprocessing.Process(target=monitor_folder, args=(folder2,))
    m.start()
    m1.start()
    m2.start()
    print("File monitor is now running.")
