🐍 Python শেখা শুরু – বাংলা গাইড (শুধুমাত্র সিনট্যাক্স ভিত্তিক Beginners Guide)
🔰 ১. Python কি?
Python একটি জনপ্রিয়, সাধারণ-উদ্দেশ্য প্রোগ্রামিং ভাষা যেটি খুবই readable ও সহজে শেখা যায়।
👉 এটি interpreted, high-level, dynamically typed language.

🔡 ২. Python Syntax: W3Schools + TutorialsPoint অনুসারে সহজ রূপরেখা
✅ প্রথম Python কোড:
python
Copy
Edit
print("Hello, world!")
📝 print() ফাংশন দিয়ে স্ক্রিনে কিছু দেখানো হয়।

✅ ভেরিয়েবল:
python
Copy
Edit
name = "Alba"
age = 22
pi = 3.1416
🔸 টাইপ ডিক্লেয়ার করতে হয় না (Python dynamically typed)।
🔸 Comments: # দিয়ে এক লাইনের কমেন্ট, ''' ''' দিয়ে মাল্টি-লাইন।

✅ ডেটা টাইপ (Basic):
python
Copy
Edit
x = 10           # int
y = 3.14         # float
name = "Alba"    # str
is_active = True # bool
✅ শর্ত (if-elif-else):
python
Copy
Edit
age = 20
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")
🔸 Indentation খুব গুরুত্বপূর্ণ (C++/Java এর {} এর পরিবর্তে)!

✅ লুপ (for & while):
python
Copy
Edit
# for loop
for i in range(5):
    print(i)

# while loop
i = 0
while i < 5:
    print(i)
    i += 1
✅ ফাংশন (function):
python
Copy
Edit
def greet(name):
    return "Hello, " + name

print(greet("Basar"))
✅ লিস্ট, টাপল, সেট, ডিকশনারি:
python
Copy
Edit
fruits = ["apple", "banana", "mango"]  # list
numbers = (1, 2, 3)                    # tuple
colors = {"red", "green", "blue"}     # set
student = {"name": "Basar", "age": 22} # dict
✅ ক্লাস ও OOP (basic):
python
Copy
Edit
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, I am", self.name)

s1 = Student("Basar", 22)
s1.greet()
🔸 এখানে self মানে this (Java/C++ এর মতো)।

📚 রিসোর্স লিঙ্ক (অনুশীলনের জন্য):
🔗 W3Schools: Python Tutorial

🔗 TutorialsPoint: Python Basics

🔗 Google Colab: Python Practice Notebook

