🐍 Python শেখা শুরু – বাংলা গাইড (শুধুমাত্র সিনট্যাক্স ভিত্তিক Beginners Guide)<br>
🔰 ১. Python কি?<br>
Python একটি জনপ্রিয়, সাধারণ-উদ্দেশ্য প্রোগ্রামিং ভাষা যেটি খুবই readable ও সহজে শেখা যায়।<br>
👉 এটি interpreted, high-level, dynamically typed language.<br><br>

🔡 ২. Python Syntax: W3Schools + TutorialsPoint অনুসারে সহজ রূপরেখা<br>
✅ প্রথম Python কোড:<br>
print("Hello, world!")<br>
📝 print() ফাংশন দিয়ে স্ক্রিনে কিছু দেখানো হয়।<br><br>

✅ ভেরিয়েবল:<br>

name = "Alba"<br>
age = 22<br>
pi = 3.1416<br>
🔸 টাইপ ডিক্লেয়ার করতে হয় না (Python dynamically typed)।<br>
🔸 Comments: # দিয়ে এক লাইনের কমেন্ট, ''' ''' দিয়ে মাল্টি-লাইন।<br><br>

✅ ডেটা টাইপ (Basic):<br>

x = 10           # int<br>
y = 3.14         # float<br>
name = "Alba"    # str<br>
is_active = True # bool<br><br>
✅ শর্ত (if-elif-else):<br>

age = 20<br>
if age >= 18:<br>
    print("Adult")<br>
elif age >= 13:<br>
    print("Teen")<br>
else:<br>
    print("Child")<br>
🔸 Indentation খুব গুরুত্বপূর্ণ (C++/Java এর {} এর পরিবর্তে)!<br><br>

✅ লুপ (for & while):<br><br>

# for loop<br>
for i in range(5):<br>
    print(i)<br><br>

# while loop<br>
i = 0<br>
while i < 5:<br>
    print(i)<br>
    i += 1<br><br>
✅ ফাংশন (function):<br>

def greet(name):<br>
    return "Hello, " + name<br><br>

print(greet("Basar"))<br><br>
✅ লিস্ট, টাপল, সেট, ডিকশনারি:<br>

fruits = ["apple", "banana", "mango"]  # list<br>
numbers = (1, 2, 3)                    # tuple<br>
colors = {"red", "green", "blue"}     # set<br>
student = {"name": "Basar", "age": 22} # dict<br><br>
✅ ক্লাস ও OOP (basic):<br>

class Student:<br>
    def __init__(self, name, age):<br>
        self.name = name<br>
        self.age = age<br><br>

    def greet(self):<br>
        print("Hello, I am", self.name)<br><br>

s1 = Student("Basar", 22)<br>
s1.greet()<br>
🔸 এখানে self মানে this (Java/C++ এর মতো)।<br><br>

📚 রিসোর্স লিঙ্ক (অনুশীলনের জন্য):<br>
🔗 W3Schools: Python Tutorial<br><br>

🔗 TutorialsPoint: Python Basics<br><br>

🔗 Google Colab: Python Practice Notebook<br>