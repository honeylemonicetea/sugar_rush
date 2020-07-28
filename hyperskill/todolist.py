from sqlalchemy import create_engine
engine = create_engine('sqlite:///todo.db?check_same_thread=False')
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta

Base = declarative_base()
class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default="Nothing to do!")
    deadline = Column(Date, default=datetime.today())
    def __repr__(self):
        return self.task
daysweek = {0 : 'Monday', 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
missed = dict()
Base.metadata.create_all(engine)
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
session.commit()
rows = session.query(Table).all()
ctr = 1

while True:
    print("""\n1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit""")
    action = input()
    if action == '3': #ALL tasks
        rows = session.query(Table).order_by(Table.deadline).all()
        print(rows)
        if len(rows) == 0:
            to = datetime.today()
            to = to.date()
            month = to.strftime('%b')
            to = str(to)
            year, mon, day = map(int, to.split('-'))
            print(f"Today {day, month}")
            print("Nothing to do!")
        else:
            for task in rows:
                deadline = task.deadline
                mon = deadline.strftime('%b')
                deadline = str(task.deadline)
                year, month, day = map(int, deadline.split('-'))
                print("{}. {}. {} {}".format(ctr, task, day, mon))
                ctr += 1
        ctr = 1
    elif action == '5': #add task
        print("Enter task")
        a = input()
        print("Enter deadline")
        currentdate = input()
        year, month, day = currentdate.split('-')
        today = datetime(int(year), int(month), int(day))
        d = today.date()
        Session = sessionmaker(bind=engine)
        session = Session()
        new_row = Table(task=a, deadline=d)
        session.add(new_row)
        session.commit()
        rows = session.query(Table).all()
        print("The task has been added!")
    elif action == '0':
        print("Bye")
        break
    elif action == '2': #week tasks
        #modify acc to dealin
        dolls = 0
        this_day = datetime.today()
        this_day = this_day.date()
        while dolls < 7:
            rows = session.query(Table).filter(Table.deadline == this_day).all()
            d = this_day.day
            m = this_day.strftime('%b')
            w = this_day.weekday()
            print(f"\n{daysweek.get(w)} {d} {m}:")
            if len(rows) == 0:
                print("Nothing to do!")
            else:
                for task in rows:
                    print("{}. {}".format(ctr, task))
                    ctr += 1
            this_day = this_day + timedelta(days=1)
            ctr = 1
            dolls += 1
    elif action == '1': #today's tasks
        today = datetime.today()
        d = today.day
        m = today.strftime('%b')
        w = today.weekday()
        print("Today {} {}:".format(d, m))
        rows = session.query(Table).filter(Table.deadline == today).all()
        if len(rows) == 0:
            print("Nothing to do!")
        else:
            for i in rows:
                print("{}. {}".format(ctr, i))
                ctr += 1
            ctr = 1
    elif action == '4': #missed tasks
        rows = session.query(Table).filter(Table.deadline < datetime.today()).all()
        print("Missed tasks:")
        if len(rows) == 0:
            print("Nothing is missed!")
        else:
            for task in rows:
                deadline = task.deadline
                mon = deadline.strftime('%b')
                deadline = str(task.deadline)
                year, month, day = map(int, deadline.split('-'))
                print("{}. {}. {} {}".format(ctr, task, day, mon))
                ctr += 1
        ctr = 1
    elif action == '6': #delete tasks
        rows = session.query(Table).order_by(Table.deadline).all()
        print("Chose the number of the task you want to delete:")
        if len(rows) == 0:
            print("Nothing to delete")
        else:
            for task in rows:
                deadline = task.deadline
                mon = deadline.strftime('%b')
                deadline = str(task.deadline)
                year, month, day = map(int, deadline.split('-'))
                print("{}. {}. {} {}".format(ctr, task, day, mon))
                print(task.id)
                missed[ctr] = task
                ctr += 1
            ctr = 1
            print(missed)
            option = int(input())
            rows = session.query(Table).filter(Table.deadline < datetime.today()).all()
            k = missed.get(option)
            session.delete(k)
            session.commit()
