


# 36-dars
# namuna funktsiya
# def name_function(value1, value2):
#     # body_function
#     return f'{value1}  {value2}'.upper()

# Yangi fileda test function yozamiz 
# funktsiya yoziladigan file nomi mavjud funksiya nomi bilan boshlanishi maqsadfa muvofiq
# masalan funktsiyamiz yangi.py fileda test funktsiyamiz esa yangi_test.py nomlanishi maqul ko'riladi

def get_titled(val1, val2):
    return f'{val1}  {val2}'.title()

# test file ichida 
import unittest
from Function import get_titled

# class ni ham function.py nomiga mos boshlanishi maqul
clas FuncTest(unittest.TestCase):
    def test_get_titled(self):
        text=get_titled('value1', 'value2')
        self.assertEqual(text, 'Value1 Value2')

unittest.main()
    
# shu tarzda funktsiyalar tekshiriladi bu namuna edi



num=int(input('Please enter a number:'))

# Even or odd

word='even' if num%2==0 else 'odd'

# Prime Check

if num>1:
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            prime_status='not prime'
            break
        
    else:
        prime_status='prime'
else:
    prime_status='not prime'
    
print(f"{num} is {word} and {prime_status}.")


