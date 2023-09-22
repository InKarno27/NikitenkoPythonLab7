"""
Лабораторная 7 Вариант 9
Написать класс Publisher и несколько различных классов с постфиксом Subscriber. Реализовать между данными
классами отношения по паттерну Observer.
"""

class Publisher:
    def __init__(self):
        self.subscribers = set()

    def add_subscriber(self, subscriber):
        self.subscribers.add(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.discard(subscriber)

    def notify_all(self, *args, **kwargs):
        for subscriber in self.subscribers:
            subscriber.update(*args, **kwargs)


class Subscriber1:
    def update(self, *args, **kwargs):
        print("[Subscriber1] Received event with args - ", args, " and kwargs - ", kwargs)


class Subscriber2:
    def update(self, *args, **kwargs):
        print("[Subscriber2] Received event with args - ", args, " and kwargs - ", kwargs)


# Пример использования
publisher = Publisher()
subscriber1 = Subscriber1()
subscriber2 = Subscriber2()

publisher.add_subscriber(subscriber2)
publisher.add_subscriber(subscriber1)


publisher.notify_all("Event 1", arg1="Hello", arg2="World")
publisher.notify_all("Event 2", arg1="Goodbay", arg2="World")

publisher.remove_subscriber(subscriber1)
publisher.notify_all("Event 3")