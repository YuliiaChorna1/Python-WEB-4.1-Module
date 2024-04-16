from jinja2 import Template

name = "Bill"
age = 28

tm = Template("My name is {{ name }} and I am {{ age }} years old")
msg = tm.render(name=name, age=age)

print(msg) # y name is Bill and I am 28 years old