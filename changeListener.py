# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 09:47:19 2018

@author: GHR6KOR
"""
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class Watcher:
    DIRECTORY_TO_WATCH = r"/home/pi/Desktop/motion"
    
    def __init__(self):
        self.observer = Observer()
    
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print ("Error")
    
        self.observer.join()


class Handler(PatternMatchingEventHandler):
    BACKUP_DIRECTORY = r"/home/pi/Desktop/motion/backup"
    patterns = ["*.jpg", "*.png"]

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print ("File created at path - %s." % event.src_path)
            
            """
                This block should contain post operation to the API
            """
            shutil.move(event.src_path, Handler.BACKUP_DIRECTORY)
            print ("File moved to backup")

if __name__ == '__main__':
    w = Watcher()
    w.run()
