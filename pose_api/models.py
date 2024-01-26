from re import S
from sqlalchemy import Column, Integer, String, Text, ARRAY, JSON
from sqlalchemy.sql.expression import false, true
from sqlalchemy.sql.functions import array_agg, random, user
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import TEXT
from pose_api.database import Base

# USERS TABLE
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(120), unique=True)
    password = Column(String(50), unique=True)
    age = Column(Integer)
    date_joined = Column(String(50))
    account_type = Column(String(50))

    def __init__(self, name=None, email=None, password=None, age=None, date_joined=None, account_type=None):
        self.name = name
        self.email = email
        self.password = password
        self.date_joined = date_joined
        self.account_type = account_type

    def __repr__(self):
        return f'<User {self.name!r}>'
    
    def create_user_id(self):
        # TODO: Implement logic to create random unique number
        pass


# WORKOUT EVENTS TABLE
class Workout_Events(Base):
    __tablename__ = 'workout_events'
    workout_event_id = Column(Integer, primary_key=True)
    date = Column(Text)
    user_id = Column(Integer)
    all_workouts = Column(JSON)
    exercises = Column(JSON)
    sets_reps_scheme = Column(JSON)
    completed = Column(JSON)

    # TO INCLUDE LATER:
    # description = Column(JSON)
    # video_link = Column(JSON)

    def __init__(self,
                workout_event_id = None,
                date=None,
                user_id=None,
                all_workouts=None,
                exercises=None,
                sets_reps_scheme=None,
                completed=None
    ):
        self.date = date
        self.user_id = user_id
        self.all_workouts = all_workouts
        self.exercises = exercises
        self.sets_reps_scheme = sets_reps_scheme
        self.completed = completed

    def __repr__(self):
        return f'<Workouts: {self.all_workouts}>'


# EXERCISES TABLE
# Exercises table to utilize later for Allowed Exercise Selection
class Exercises(Base):
    __tablename__ = 'exercises'
    exercise_name = Column(String(50), primary_key=true)
    exercise_description = Column(TEXT)
    exercise_group = Column(String(50))

    def __init__(self, exercise_name=None, exercise_description=None, exercise_group=None):
        self.exercise_name = exercise_name
        self.exercise_description = exercise_description
        self.exercise_group = exercise_group

    # Possible Exercise Groups
    # squats
    # deadlifts
    # lunges
    # pushing
    # pulling
    # running