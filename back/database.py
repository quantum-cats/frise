import sqlite3
from prettytable import from_db_cursor


def get_connection(db_name):
    con = sqlite3.connect(db_name)
    con.row_factory = sqlite3.Row
    return con


# ----------------------- Events ---------------------------


def create_events_table(con):
    sql_create_events_table = """
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            date date, location TEXT, author TEXT, details TEXT, labels TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP);
    """
    with con:
        con.execute(sql_create_events_table)


def insert_events_rows(con, rows):
    sql_insert_events = """
        INSERT INTO events 
            (author, date, location, details, labels) 
        VALUES
            (?, ?, ?, ?, ?);
    """
    with con:
        try:
            con.executemany(sql_insert_events, rows)
        except sqlite3.IntegrityError:
            return "Line already exists."


def get_all_events(con):
    sql_select_all = """
        SELECT *
        FROM events
        ORDER by Timestamp desc
        LIMIT 10;
    """

    return con.execute(sql_select_all)


# ----------------------- Test ---------------------------


def print_table(rows):
    table = from_db_cursor(rows)
    print(table)


def test_database_creation():
    con = get_connection(":memory:")
    create_events_table(con)

    events = [
        (
            "morgan madelaine",
            "01-03-1990",
            "martinique",
            "I was born in Schoelcher",
            "date of birth",
        ),
        (
            "rudolph madelaine",
            "28-07-1992",
            "martinique",
            "I was born in Schoelcher",
            "date of birth",
        ),
        (
            "ruben madelaine",
            "20-03-1994",
            "martinique",
            "I was born in Schoelcher",
            "date of birth",
        ),
        (
            "manfred madelaine",
            "01-08-1995",
            "martinique",
            "I was born in Schoelcher",
            "date of birth",
        ),
    ]

    insert_events_rows(con, events)
    events = get_all_events(con)
    print_table(events)

    con.close()


if __name__ == "__main__":
    test_database_creation()
