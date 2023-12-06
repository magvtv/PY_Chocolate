from re import T


class TheatrePriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def heapify_up(self, index=None):
        if index is None:
            return len(self.heap) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if (
                self.heap[parent_index]["user_priority"]
                > self.heap[index]["user_priority"]
            ):
                self.heap_swap(parent_index, index)
                index = parent_index
            else:
                break

    def heapify_down(self, index=0):
        while True:
            left_child_index = (2 * index) + 1
            right_child_index = (2 * index) + 2

            least = index

            if least != index:
                self.heap_swap(index, least)
                index = least
            if (left_child_index < len(self.heap)) and (
                self.heap[left_child_index]["user_priority"]
                < self.heap[least]["user_priority"]
            ):
                least = left_child_index
            if (right_child_index < len(self.heap)) and (
                self.heap[right_child_index]["user_priority"]
                < self.heap[least]["user_priority"]
            ):
                least = right_child_index
            else:
                break

    def heap_swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def enqueue(self, user_info):
        self.heap.append(user_info)
        self.heapify_up()  # up heap bubbling

    def dequeue(self):
        if not self.is_empty():
            self.heap_swap(0, len(self.heap) - 1)  # swap root with last element
            removed_user = self.heap.pop()
            self.heapify_down()  # down heap bubbling
            return removed_user
        return None

    def remove_user(self, user_name):
        for i, user in enumerate(self.heap):
            if user["user_name"] == user_name:
                self.heap_swap(
                    i, len(self.heap) - 1
                )  # swap user with the last heap element
                removed_user = self.heap.pop()  # remove the user
                self.heapify_down(i)  # restore heap property
                return removed_user
            return None

    def update_priority(self, user_name, new_priority):
        for i, user in enumerate(self.heap):
            if user["user_name"] == user_name:
                self.heap[i]["user_priority"] = new_priority
                self.heapify_up(i)
                self.heapify_down(i)
                return True
            return False


film_queue = TheatrePriorityQueue()

user1 = {
    "user_name": "PH Magutu",
    "user_contact": {"user_email": "magutujr@gmail.com", "user_phone": "+25497649768"},
    "user_priority": 1,
}
