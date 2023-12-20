# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 08:31:30 2019

@author: Hrishikesh Pisal
"""
from string import Template


t = Template('Hey, $name!')
print(t)
print(type(t))

fname = "Kapil"
s = t.substitute(name=fname)
print(s)

s = t.substitute(name="Ravi")
print(s)

#  ${identifier} is same as $identifier
t = Template('Hey, $name!')
t = t.substitute(name=fname)
print(t)

t = Template('Hey, ${name}!')
s = t.substitute(name=fname)
print(s)

fname= "Smita"
s = t.substitute(name=fname)
print(s)

t = Template('${name} is the ${job} of ${company}')
s = t.substitute(name='Ratan Tata', job='CEO', company='Tata Motors.')
print(s)

t = Template('${name} is the ${job} of ${company}')
s = t.substitute( job='CEO', company='Tata Motors.',name='Ratan Tata')
print(s)

# dictionary as substitute argument
d = {"name": "Ratan Tata", "company": "Tata Motors.","job": "CEO"}
s = t.substitute(d)
print(s)

company = [
     {"name": "Ratan Tata",  "company": "Tata Motors", "job": "CEO"},
     {"name": "Anand Mahindra", "job": "CEO", "company": "Mahindra"},
     {"name": "Anu Aga", "job": "CEO", "company": "Thermax"}]

t = Template('${name} is the ${job} of ${company}')
for record in company:
    # print(record)
    s = t.substitute(record)
    print(s)

t = Template('${name} is the  ${job} of ${company}')
# s = t.substitute(name='Ratan Tata', job='CEO') #Error

s = t.safe_substitute(name='Ratan Tata', job='CEO',company= "Tata Motors")
print(s)

s = t.safe_substitute(name='Ratan Tata', job='CEO')
print(s)

# Escaping $ sign
# We can use $$ to escape $ sign and treat it as part of normal string.

t = Template('$$ is called ${name}')
s = t.substitute(name='Dollar')
print(s)


t = Template('${noun} adjective is ${noun}ing')
s = t.substitute(noun='Test')
print(s)


t = Template('Pay ${who} Rs $$100')
s = t.substitute(who ='Mandar')
print(s)

t = Template('Pay ${who} $$${amount}')
s = t.substitute(who='Mandar',amount=999)
print(s)
