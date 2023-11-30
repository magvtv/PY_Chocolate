from datetime import datetime


def convert_to_12hr(time_str):
    time_obj = datetime.strptime(time_str, "%H%M")
    # Convert 24hr time format to 12hr time format
    return time_obj.strftime("%I:%M %p")


def convert_to_24hr(time_str):
    time_obj = datetime.strptime(time_str, "%H%M")
    # Convert 12hr time format to 24hr time format
    return time_obj.strftime("%H:%M")


def validate_time_format(time_str):
    # Check if the time is in the correct format (HH:MM)
    try:
        datetime.strptime(time_str, "%H%M")
        return True
    except ValueError:
        return False


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return str(self.queue)

    def enqueue(self, patient):
        self.queue.append(patient)
        self.queue.sort(key=lambda x: x["Time"])

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def __iter__(self):
        return iter(self.queue)

    def add(self, item):
        self.queue.append(item)
        self.queue.sort(key=lambda x: datetime.strftime(x["Time"], "%H%M"))

    def remove(self, item):
        self.queue.remove(item)

    def remove_next(self):
        if self.queue:
            return self.queue.pop(0)

    def refresh(self):
        self.queue.sort(key=lambda x: datetime.strftime(x["Time"], "%H%M"))

    def get_queue(self):
        return self.queue
    
    def get_length(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0
