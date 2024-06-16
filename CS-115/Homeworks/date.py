'''
Created on: November 20, 2017
@author:   hrana2 - Himanshu Rana 
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System" 

CS115 - Hw 11 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    
    
    def copy(self):
        '''Returns a new object with the same month, day, year as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew  


    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date, whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
            self.day == d2.day
    
    def tomorrow(self):  
        '''This function does not return anything, but rater changes the value of the object. The new value will represent one calendar day after the original value'''
        feb_leap_days = 28 + self.isLeapYear()
        DIM = [0,31,feb_leap_days,31,30,31,30,31,31,30,31,30,31]
        self.day += 1
        if self.day > DIM[self.month]:
            self.day = 1
            self.month += 1
            if self.month == 13:
                self.year += 1
                self.month = 1
                
    def yesterday(self):
        '''This function does not return anything, rather it changes the value of the object by representing one calendar day before the orginal value'''
        feb_leap_days = 28 + self.isLeapYear()
        DIM = [0,31,feb_leap_days,31,30,31,30,31,31,30,31,30,31]
        self.day -= 1
        if self.day < 1:
            self.month -= 1
            if self.month < 1:
                self.year -= 1
                self.month = 12
            self.day = DIM[self.month]
            
    def addNDays(self, N):
        '''This function changes the value of the object by adding N numbers of days to the original value'''
        for _ in range(N): 
            print(self)
            self.tomorrow()
        print(self)
           
             
    def subNDays(self, N):
        '''This function changes the value of the object by subtracting N numbers of days to the original value'''
        for _ in range(N): 
            print(self)
            self.yesterday()
        print(self)
                   
    def isBefore(self, d2):
        '''This function returns True if a given date is before another date and False if it is not'''
        if self.year < d2.year:
            return True 
        if self.month < d2.month and self.year == d2.year:
            return True
        if self.day < d2.day and d2.month == self.month and self.year == d2.year:
            return True
        return False
    
    def isAfter(self, d2):
        '''This function returns if a given date is after another by using the isBefore function and switching the values'''
        return  d2.isBefore(self)
    
    def diff(self, d2):
        '''This function computes the difference between two given dates'''
        dcopy = self.copy()
        difference = 0 
        
        while dcopy.isBefore(d2): 
            dcopy.tomorrow()
            difference -= 1
        while dcopy.isAfter(d2): 
            dcopy.yesterday()
            difference += 1
        return difference

    def dow(self):
        '''This function returns the day of the week for a given date'''
        d = self.day
        m = self.month
        y = self.year
        days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
        if m < 3:
            y -= 1
        date_diff = (y + y // 4 - y // 100 + y // 400 + t[m - 1] + d) % 7
        return days_of_week[date_diff]
       
       
     
        
        
'''print(Date(10,28,1929).dow())    
       
d1 = Date(11, 28, 2017) 
d2 = Date(12, 31, 2014)
#print(d1.isBefore(d2))


    
d = Date(11, 8, 2011)
print(d)
print(d.isLeapYear())

d2 = Date(3, 15, 2012)
print(d2.isLeapYear())

print(Date(1,1,1900).isLeapYear())

d3 = Date(11, 9, 2011)
print(d == d3)
'''

    


