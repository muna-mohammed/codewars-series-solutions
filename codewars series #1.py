# codewars series #1
# the url , link of the problem:
https://www.codewars.com/kata/597c684822bc9388f600010f/train/python
# the question is to fix the bugs


class Dinglemouse(object):
    def __init__(self, first_name, last_name):
        first_name = first_name
        last_name = last_name
    def get_full_name(self):
        return first_name + ' ' + last_name


#The correct answer is as follows: my solution 

class Dinglemouse(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def get_full_name(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        else:
            return self.first_name + self.last_name
            
# another solution
class Dinglemouse(object):
    def __init__(self, first, last):
        self.name = '{} {}'.format(first, last).strip()
    def get_full_name(self):
        return self.name
        
# another solution
class Dinglemouse(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'.strip()