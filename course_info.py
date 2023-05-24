from abc import ABCMeta, abstractmethod
from typing import List
from datetime import datetime

import pandas as pd

class CourseDetails:
    course_uuid: str
    name: str
    starts: datetime
    ends: datetime

    def __str__(self, key):
        return '{}, {}, {}, {}'.format(self.course_uuid, self.name, self.starts, self.ends)
    
    def __iter__(self):
        yield self.course_uuid
        yield self.name
        yield self.starts
        yield self.ends 

class Assignment:
    assignment_uuid: str
    name: str
    due: datetime
    late: datetime
    points: int
    ec_points: int
    weight: float

class Person:
    student_id: str
    name: str
    emails: List[str]

    def __str__(self, key):
        return '{}, {}, {}'.format(self.student_id, self.name, self.emails)
    
    def __iter__(self):
        yield self.student_id
        yield self.name
        yield self.emails

class CourseApi:
    @abstractmethod
    def get_course_list(self) -> List[CourseDetails]:
         raise NotImplementedError()
    
    def get_course_list_df(self) -> pd.DataFrame:
        return pd.DataFrame(self.get_course_list())

    @abstractmethod    
    def get_assignments(self) -> List[Assignment]:
         raise NotImplementedError()
    
    def get_assignments_df(self) -> pd.DataFrame:
        return pd.DataFrame(self.get_assignments())

    @abstractmethod
    def get_quizzes(self) -> List[Assignment]:
        pass

    @abstractmethod
    def get_students(self) -> List[Person]:
        raise NotImplementedError()
 
    def get_students_df(self) -> pd.DataFrame:
        return pd.DataFrame(self.get_students())

 
    @abstractmethod
    def get_instructors(self) -> List[Person]:
        raise NotImplementedError()

    def get_instructors_df(self) -> pd.DataFrame:
        return pd.DataFrame(self.get_instructors())

    