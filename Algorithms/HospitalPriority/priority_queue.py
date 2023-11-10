from datetime import datetime


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, patient, time):
        self.queue.append(patient, time)
        self.queue.sort(
            key=lambda x: x["time"]
        )  # Sort the queue based on appointment time

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def display_queue(self):
        if self.is_empty():
            print("The hospital priority queue is empty.")
        else:
            print("Hospital Priority Queue:")
            for appointment in self.queue:
                print(f"Name: {appointment['name']}, Time: {appointment['time']}")


def validate_time_format(time_str):
    # Check if the time is in the correct format (HH:MM)
    try:
        datetime.datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False


def convert_to_12hr(time_str):
    time_obj = datetime.strptime(time_str, "%H:%M")
    # Convert 24hr time format to 12hr time format
    return time_obj.strftime("%I:%M %p")


def convert_to_24hr(time_str):
    time_obj = datetime.strptime(time_str,"%I:%M %p")
    # Convert 12hr time format to 24hr time format
    return time_obj.strftime("%H:%M")
