import json
import database as db

DB_NAME = "database/events.db"


class Event:
    def __init__(self, date, location, details, author, labels, timestamp):
        self.date = date
        self.location = location
        self.author = author
        self.details = details
        self.labels = labels
        self.timestamp = timestamp

    def __str__(self):
        txt = ""
        txt += f"{self.date}, {self.location}, {self.author}, {self.details}, {self.labels}, {self.timestamp}"
        return txt

    def to_json(self):
        return json.dumps(self.__dict__)


def get_all_events():
    con = db.get_connection(DB_NAME)
    events = db.get_all_events(con)
    con.close()
    return map_events(events)


def map_events(events):
    return [to_domain(event) for event in events]


def to_domain(event):
    return Event(event['date'],
                 event['location'],
                 event['details'],
                 event['author'],
                 event['labels'],
                 event['timestamp'])


if __name__ == "__main__":
    events = get_all_events()
    [print(ev.to_json()) for ev in events]
