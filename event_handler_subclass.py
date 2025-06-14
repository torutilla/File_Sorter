from watchdog.events import FileSystemEventHandler
class Handler(FileSystemEventHandler):
    def on_moved(self, event):
        return super().on_moved(event)
