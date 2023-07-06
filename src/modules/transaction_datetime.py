#/bin/bash python3

from datetime import datetime


class TransactionDateTime:
    
    def __init__(self):
        
        self.year = ''
        self.month = ''
        self.day = ''
        self.hour = ''
        self.minute = ''
        self.second = ''
        
    def inject_datetime_str(self, datetime_str: str):
        
        # date_string = "2021-11-28 16:05:38"
        date_string = datetime_str
        date_format = "%Y-%m-%d %H:%M:%S"
        date_object = datetime.strptime(date_string, date_format)
        standard_time = date_object.strftime("%Y-%m-%d %H:%M:%S")
        
        self.year = date_object.year
        self.month = date_object.month
        self.day = date_object.day
        self.hour = date_object.hour
        self.minute = date_object.minute
        self.second = date_object.second
        
        
    def __str__(self):
        
        return str(self.__dict__)

    def get_v_str(self) -> str:
        
        return f"{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}:{self.second}"

    def show(self):
        
        print(f"Year: {self.year}")
        print(f"Month: {self.month}")
        print(f"Day: {self.day}")
        print(f"Hour: {self.hour}")
        print(f"Minute: {self.minute}")
        print(f"Second: {self.second}")
        
        
