"""
=============================================================================
  EXERCISE 1: PYTHON FUNDAMENTALS
=============================================================================
  Welcome! This file teaches you Python step by step.
  
  HOW TO USE THIS FILE:
  1. Read each section — it explains a concept with examples
  2. Find the TODO comments — they tell you what to write
  3. Replace 'pass' or 'None' with your code
  4. Run tests: python -m pytest test_exercise.py -v
  
  Don't delete any function names or change the function signatures!
  Only change the code INSIDE the functions where you see TODO.
=============================================================================
"""


# ============================================================================
# PART 1: VARIABLES & TYPES
# ============================================================================
#
# Python has several basic types:
#   - str    (text)      →  "hello", 'world'
#   - int    (whole numbers)  →  42, -7, 0
#   - float  (decimals)  →  3.14, -0.5
#   - bool   (true/false) →  True, False
#   - None   (nothing)   →  None
#
# You create variables by just assigning a value:
#   name = "Alice"     ← no need to declare type
#   age = 25
#   is_student = True
#
# EXAMPLE:
def example_variables():
    """This is an EXAMPLE — just read it, don't change it."""
    greeting = "Hello"
    count = 10
    pi = 3.14159
    is_active = True
    return greeting, count, pi, is_active


# TODO 1: Create variables and return them
# Create these variables:
#   - name (your name as a string)
#   - age (your age as an integer)
#   - gpa (a decimal number like 8.5)
#   - is_enrolled (True or False)
# Then return all four
def create_variables():
    # Write your code below this line
    pass


# ============================================================================
# PART 2: FUNCTIONS
# ============================================================================
#
# Functions are reusable blocks of code.
#
# SYNTAX:
#   def function_name(parameter1, parameter2):
#       """Description of what the function does."""
#       # your code here
#       return result
#
# EXAMPLE:
def example_add(a, b):
    """Add two numbers and return the result."""
    result = a + b
    return result
    # example_add(3, 5) → 8


# TODO 2: Write a function that calculates the area of a rectangle
# Formula: area = length × width
# EXAMPLE: rectangle_area(5, 3) → 15
def rectangle_area(length, width):
    # Write your code below this line
    pass


# ============================================================================
#
# FUNCTIONS WITH DEFAULT PARAMETERS:
#
# You can give parameters default values. If the caller doesn't provide
# that argument, the default is used.
#
# EXAMPLE:
def example_greet(name, greeting="Hello"):
    """Greet someone. If no greeting specified, use 'Hello'."""
    return f"{greeting}, {name}!"
    # example_greet("Alice")         → "Hello, Alice!"
    # example_greet("Bob", "Hi")     → "Hi, Bob!"


# TODO 3: Write a function that calculates the total price with tax
# Parameters: price (required), tax_rate (optional, default 0.1 which is 10%)
# Formula: total = price + (price × tax_rate)
# EXAMPLE: calculate_total(100) → 110.0
# EXAMPLE: calculate_total(100, 0.2) → 120.0
def calculate_total(price, tax_rate=0.1):
    # Write your code below this line
    pass


# ============================================================================
# PART 3: LISTS
# ============================================================================
#
# Lists are ordered collections of items. They can hold any type.
#
# Creating lists:
#   numbers = [1, 2, 3, 4, 5]
#   names = ["Alice", "Bob", "Charlie"]
#   empty = []
#
# Accessing items (index starts at 0):
#   numbers[0]   → 1      (first item)
#   numbers[-1]  → 5      (last item)
#   numbers[1:3] → [2, 3] (items at index 1 and 2)
#
# Common operations:
#   numbers.append(6)      → adds 6 to the end
#   numbers.pop()          → removes and returns last item
#   len(numbers)           → number of items
#   3 in numbers           → True (checks if 3 is in the list)
#
# Looping through a list:
#   for item in numbers:
#       print(item)
#
# EXAMPLE:
def example_sum_list(numbers):
    """Add up all numbers in a list."""
    total = 0
    for num in numbers:
        total += num   # same as: total = total + num
    return total
    # example_sum_list([1, 2, 3]) → 6


# TODO 4: Write a function that finds the largest number in a list
# Do NOT use the built-in max() function — write the logic yourself
# EXAMPLE: find_largest([3, 7, 2, 9, 4]) → 9
# EXAMPLE: find_largest([5]) → 5
# EXAMPLE: find_largest([-1, -5, -2]) → -1
def find_largest(numbers):
    # Hint: Start with the first number as your "largest so far"
    # Then loop through the rest and compare
    # Write your code below this line
    pass


# TODO 5: Write a function that returns only the even numbers from a list
# EXAMPLE: filter_evens([1, 2, 3, 4, 5, 6]) → [2, 4, 6]
# EXAMPLE: filter_evens([1, 3, 5]) → []
# HINT: A number is even if number % 2 == 0 (% gives the remainder)
def filter_evens(numbers):
    # Write your code below this line
    pass


# ============================================================================
# PART 4: DICTIONARIES
# ============================================================================
#
# Dictionaries store key-value pairs (like a phone book: name → number).
#
# Creating:
#   person = {"name": "Alice", "age": 25, "city": "Chennai"}
#   empty = {}
#
# Accessing values:
#   person["name"]              → "Alice"
#   person.get("email", "N/A") → "N/A" (safe access with default)
#
# Adding/updating:
#   person["email"] = "alice@test.com"   → adds new key
#   person["age"] = 26                   → updates existing key
#
# Checking if key exists:
#   "name" in person   → True
#   "phone" in person  → False
#
# Looping:
#   for key, value in person.items():
#       print(f"{key}: {value}")
#
# EXAMPLE:
def example_count_letters(text):
    """Count how many times each letter appears."""
    counts = {}
    for letter in text:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts
    # example_count_letters("hello") → {'h': 1, 'e': 1, 'l': 2, 'o': 1}


# TODO 6: Write a function that creates a student record (dictionary)
# Parameters: name (str), age (int), grades (list of numbers)
# Return a dictionary with keys: "name", "age", "grades", "average"
# The "average" should be calculated from the grades list
# EXAMPLE: create_student("Alice", 20, [85, 90, 78])
#    → {"name": "Alice", "age": 20, "grades": [85, 90, 78], "average": 84.33}
# HINT: average = sum(grades) / len(grades). Round to 2 decimals with round()
def create_student(name, age, grades):
    # Write your code below this line
    pass


# TODO 7: Write a function that merges two dictionaries
# If a key exists in both, use the value from dict2
# EXAMPLE: merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4})
#    → {"a": 1, "b": 3, "c": 4}
# HINT: Start with a copy of dict1, then update with dict2
def merge_dicts(dict1, dict2):
    # Write your code below this line
    pass


# ============================================================================
# PART 5: CLASSES & OBJECTS
# ============================================================================
#
# Classes are blueprints for creating objects. Think of a class as a template.
#
# SYNTAX:
#   class ClassName:
#       def __init__(self, param1, param2):  ← constructor (runs when you create object)
#           self.param1 = param1             ← 'self' = this object
#           self.param2 = param2
#
#       def method_name(self):               ← method (function inside class)
#           return self.param1
#
# EXAMPLE:
class ExampleBankAccount:
    """A simple bank account."""

    def __init__(self, owner, balance=0):
        """Create a new account."""
        self.owner = owner        # who owns it
        self.balance = balance    # how much money
        self.transactions = []    # list of transactions

    def deposit(self, amount):
        """Add money to the account."""
        self.balance += amount
        self.transactions.append(f"+{amount}")
        return self.balance

    def get_balance(self):
        """Return current balance."""
        return self.balance

    # Usage:
    # acc = ExampleBankAccount("Alice", 100)
    # acc.deposit(50)        → 150
    # acc.get_balance()      → 150


# TODO 8: Create a TaskList class
# This class manages a to-do list. Implement these methods:
#
# __init__(self):
#   - Initialize an empty list called self.tasks
#
# add_task(self, task_name):
#   - Add a dictionary to self.tasks with keys:
#     "name" (the task_name) and "done" (False)
#
# complete_task(self, task_name):
#   - Find the task with that name and set "done" to True
#   - If the task doesn't exist, do nothing
#
# get_pending(self):
#   - Return a list of task names where "done" is False
#
# EXAMPLE:
#   tl = TaskList()
#   tl.add_task("Buy milk")
#   tl.add_task("Write code")
#   tl.complete_task("Buy milk")
#   tl.get_pending()  → ["Write code"]
#
class TaskList:
    def __init__(self):
        # TODO: Initialize self.tasks as an empty list
        pass

    def add_task(self, task_name):
        # TODO: Append {"name": task_name, "done": False} to self.tasks
        pass

    def complete_task(self, task_name):
        # TODO: Find task by name and set "done" to True
        pass

    def get_pending(self):
        # TODO: Return list of names where "done" is False
        pass


# ============================================================================
# PART 6: ERROR HANDLING
# ============================================================================
#
# When something goes wrong, Python raises an "exception".
# You can catch exceptions with try/except blocks.
#
# SYNTAX:
#   try:
#       result = risky_operation()        ← code that might fail
#   except SomeError as e:
#       print(f"Error: {e}")              ← what to do if it fails
#   finally:
#       cleanup()                         ← always runs (optional)
#
# Common exceptions:
#   ValueError      → wrong value (like int("hello"))
#   TypeError       → wrong type (like 5 + "hello")
#   KeyError        → dictionary key doesn't exist
#   IndexError      → list index out of range
#   ZeroDivisionError → dividing by zero
#
# EXAMPLE:
def example_safe_divide(a, b):
    """Divide a by b, returning None if b is zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return None
    # example_safe_divide(10, 3)  → 3.333...
    # example_safe_divide(10, 0)  → None


# TODO 9: Write a function that safely converts a string to an integer
# If the string is a valid number, return the integer
# If the string is NOT a valid number, return the default_value
# EXAMPLE: safe_int("42") → 42
# EXAMPLE: safe_int("hello") → 0
# EXAMPLE: safe_int("xyz", -1) → -1
# HINT: Use try/except with ValueError
def safe_int(text, default_value=0):
    # Write your code below this line
    pass


# TODO 10: Write a function that safely gets a value from a nested dictionary
# Sometimes config files are nested: {"database": {"host": "localhost"}}
# This function should access nested keys without crashing
# EXAMPLE: safe_get({"a": {"b": {"c": 42}}}, ["a", "b", "c"]) → 42
# EXAMPLE: safe_get({"a": {"b": 1}}, ["a", "x", "y"]) → None
# EXAMPLE: safe_get({"a": 1}, ["a"]) → 1
# HINT: Loop through the keys list, going one level deeper each time
#        Use try/except to catch KeyError or TypeError
def safe_get(data, keys):
    # Write your code below this line
    pass


# ============================================================================
# PART 7: STRING FORMATTING
# ============================================================================
#
# Python has f-strings for formatting (put f before the quotes):
#   name = "Alice"
#   age = 25
#   f"Name: {name}, Age: {age}"   → "Name: Alice, Age: 25"
#   f"Total: {100 * 0.15:.2f}"    → "Total: 15.00" (2 decimal places)
#
# EXAMPLE:
def example_format_log(level, message):
    """Format a log message."""
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"[{timestamp}] {level.upper()}: {message}"


# TODO 11: Write a function that creates a formatted receipt
# Parameters: items (list of dicts with "name" and "price")
# Return a string with each item on its own line, plus a total
# EXAMPLE: format_receipt([{"name": "Coffee", "price": 4.50},
#                          {"name": "Muffin", "price": 3.25}])
# Returns:
#   "Coffee    -  $4.50\nMuffin    -  $3.25\n---------\nTotal     -  $7.75"
# HINT: use f-string with :<10 for left-aligned padding
#       f"{'Coffee':<10}-  ${4.50:.2f}"  → "Coffee    -  $4.50"
def format_receipt(items):
    # Write your code below this line
    pass


# ============================================================================
# PART 8: LIST COMPREHENSIONS
# ============================================================================
#
# List comprehensions are a short way to create lists.
# It's like a for loop squeezed into one line.
#
# SYNTAX:
#   [expression for item in iterable]
#   [expression for item in iterable if condition]
#
# EXAMPLES:
#   squares = [x**2 for x in range(5)]           → [0, 1, 4, 9, 16]
#   evens = [x for x in range(10) if x % 2 == 0] → [0, 2, 4, 6, 8]
#   upper = [s.upper() for s in ["a", "b", "c"]]  → ["A", "B", "C"]
#
# LONG FORM (equivalent to the squares example above):
#   squares = []
#   for x in range(5):
#       squares.append(x**2)

# TODO 12: Write a function using list comprehension
# Given a list of words, return only words longer than 3 characters, in uppercase
# EXAMPLE: transform_words(["hi", "hello", "hey", "python", "go"])
#    → ["HELLO", "PYTHON"]
# HINT: [word.upper() for word in words if len(word) > 3]
def transform_words(words):
    # Write your code below this line (use list comprehension!)
    pass


# ============================================================================
# PART 9: FILE I/O & JSON
# ============================================================================
#
# Reading/writing files is ESSENTIAL — most tasks involve config files, logs,
# or data files.
#
# READING A FILE:
#   with open("data.txt", "r") as f:   ← "r" = read mode
#       content = f.read()              ← reads entire file as string
#       # OR
#       lines = f.readlines()           ← reads as list of lines
#
# WRITING A FILE:
#   with open("output.txt", "w") as f: ← "w" = write (overwrites!)
#       f.write("Hello\n")
#
# APPENDING TO A FILE:
#   with open("log.txt", "a") as f:    ← "a" = append (adds to end)
#       f.write("New entry\n")
#
# JSON (JavaScript Object Notation) — the universal data format:
#   import json
#
#   # Python dict → JSON string
#   json_str = json.dumps({"name": "Alice", "age": 25})
#   # → '{"name": "Alice", "age": 25}'
#
#   # JSON string → Python dict
#   data = json.loads('{"name": "Alice", "age": 25}')
#   # → {"name": "Alice", "age": 25}
#
#   # Read JSON file
#   with open("config.json") as f:
#       config = json.load(f)
#
#   # Write JSON file
#   with open("config.json", "w") as f:
#       json.dump(data, f, indent=2)
#
# EXAMPLE:
import json

def example_read_json(json_string):
    """Parse a JSON string into a Python dictionary."""
    return json.loads(json_string)


# TODO 13: Write a function that reads a JSON string and extracts specific fields
# Parameters: json_string (str), fields (list of field names to extract)
# Return a new dictionary with only the requested fields
# If a field doesn't exist in the JSON, skip it
# EXAMPLE: extract_fields('{"name": "Alice", "age": 25, "city": "NYC"}', ["name", "age"])
#    → {"name": "Alice", "age": 25}
# EXAMPLE: extract_fields('{"a": 1}', ["a", "b"]) → {"a": 1}
def extract_fields(json_string, fields):
    # Write your code below this line
    pass


# TODO 14: Write a function that merges multiple JSON strings into one
# Each JSON string represents a config layer (later ones override earlier ones)
# EXAMPLE: merge_json_configs(['{"host": "localhost", "port": 3000}',
#                               '{"port": 8080, "debug": true}'])
#    → {"host": "localhost", "port": 8080, "debug": True}
def merge_json_configs(json_strings):
    # Write your code below this line
    pass


# ============================================================================
# PART 10: THREADING & LOCKS
# ============================================================================
#
# Many Python tasks use threading for concurrent operations
# (connection pools, background workers, etc.)
#
# CREATING A THREAD:
#   import threading
#
#   def worker():
#       print("Working...")
#
#   t = threading.Thread(target=worker)
#   t.start()     # Start the thread
#   t.join()      # Wait for it to finish
#
# THE PROBLEM: Two threads modifying the same variable = data corruption!
#
# THE SOLUTION: Use a Lock:
#   lock = threading.Lock()
#
#   lock.acquire()      # Only one thread can pass at a time
#   shared_data += 1    # Safe to modify
#   lock.release()      # Let other threads through
#
#   # Better: use 'with' statement (automatically acquires/releases):
#   with lock:
#       shared_data += 1
#
# EXAMPLE:
import threading

class ExampleSafeList:
    """A thread-safe list."""
    def __init__(self):
        self._items = []
        self._lock = threading.Lock()

    def add(self, item):
        with self._lock:
            self._items.append(item)

    def get_all(self):
        with self._lock:
            return list(self._items)  # Return a copy!


# TODO 15: Create a thread-safe counter class
# This is EXACTLY the pattern used in Week-1 connection pools!
#
# Methods:
#   __init__(self): Initialize count to 0, create a threading.Lock()
#   increment(self): Safely add 1 to count (use the lock!)
#   decrement(self): Safely subtract 1 from count (use the lock!)
#   get_count(self): Safely return current count
#
# EXAMPLE:
#   counter = ThreadSafeCounter()
#   counter.increment()
#   counter.increment()
#   counter.get_count() → 2
#
# WHY THIS MATTERS: Without the lock, 1000 threads calling increment()
# might result in a count less than 1000 (lost updates!)
class ThreadSafeCounter:
    def __init__(self):
        # TODO: Initialize self.count and self._lock
        pass

    def increment(self):
        # TODO: Safely add 1
        pass

    def decrement(self):
        # TODO: Safely subtract 1
        pass

    def get_count(self):
        # TODO: Safely return count
        pass


# ============================================================================
# PART 11: LOGGING
# ============================================================================
#
# Production code uses the logging module instead of print().
# You'll see this in almost every Python task file:
#
#   import logging
#   logger = logging.getLogger(__name__)
#
#   logger.debug("Detailed info for debugging")
#   logger.info("Normal operation message")
#   logger.warning("Something unexpected but not broken")
#   logger.error("Something failed!")
#   logger.critical("System is going down!")
#
# Setting up a logger:
#   logging.basicConfig(level=logging.INFO,
#                       format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# EXAMPLE:
import logging

def example_with_logging():
    logger = logging.getLogger("example")
    logger.info("Starting operation")
    try:
        result = 10 / 2
        logger.info(f"Result: {result}")
    except Exception as e:
        logger.error(f"Operation failed: {e}")
    return result


# TODO 16: Write a function that processes a list of records and logs its progress
# Parameters: records (list of dicts), logger_name (str)
# For each record:
#   - If record has "status" == "error", log a WARNING with the record's "message"
#   - If record has "status" == "ok", log an INFO with the record's "id"
#   - If record is missing "status", log an ERROR: "Record missing status field"
# Return the count of successfully processed records (status == "ok")
# EXAMPLE:
#   records = [
#       {"id": 1, "status": "ok", "message": "fine"},
#       {"id": 2, "status": "error", "message": "disk full"},
#       {"id": 3, "message": "no status"},
#   ]
#   process_records(records, "myapp") → 1
def process_records(records, logger_name="processor"):
    # Write your code below this line
    pass


# ============================================================================
# PART 12: DECORATORS
# ============================================================================
#
# Decorators are functions that wrap other functions to add behavior.
# You'll see @decorator syntax in many Python tasks.
#
# HOW A DECORATOR WORKS:
#   def my_decorator(func):             ← takes a function as input
#       def wrapper(*args, **kwargs):   ← creates a new function
#           print("Before")
#           result = func(*args, **kwargs)  ← calls the original
#           print("After")
#           return result
#       return wrapper                  ← returns the new function
#
# USING IT:
#   @my_decorator
#   def say_hello():
#       print("Hello!")
#
#   say_hello()
#   # Output: Before
#   #         Hello!
#   #         After
#
# EXAMPLE — timing decorator:
import time

def example_timer(func):
    """Decorator that measures how long a function takes."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.3f}s")
        return result
    return wrapper


# TODO 17: Write a retry decorator
# This decorator should retry a function up to max_retries times if it raises an exception
# If all retries fail, raise the last exception
# EXAMPLE:
#   @retry(max_retries=3)
#   def flaky_function():
#       # might fail sometimes
#       pass
#
# HINT: A decorator with arguments needs an extra layer:
#   def retry(max_retries=3):          ← outer: takes decorator args
#       def decorator(func):           ← middle: takes the function
#           def wrapper(*args, **kwargs):  ← inner: replacement function
#               ...
#           return wrapper
#       return decorator
def retry(max_retries=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # TODO: Try calling func. If it raises an exception,
            # retry up to max_retries times. If all fail, raise the last exception.
            pass
        return wrapper
    return decorator


# ============================================================================
# PART 13: REGULAR EXPRESSIONS
# ============================================================================
#
# Regex = pattern matching in strings. Used for parsing logs, validating
# input, extracting data from text.
#
# import re
#
# BASIC PATTERNS:
#   \d    → any digit (0-9)
#   \w    → any word character (letter, digit, underscore)
#   \s    → any whitespace
#   .     → any character
#   *     → zero or more
#   +     → one or more
#   ?     → zero or one
#   []    → character class: [a-z] = any lowercase letter
#   ()    → capture group: extracts matched text
#
# COMMON FUNCTIONS:
#   re.search(pattern, text)    → finds first match (or None)
#   re.findall(pattern, text)   → finds all matches → list
#   re.sub(pattern, repl, text) → replace all matches
#   match.group(1)              → get first capture group
#
# EXAMPLE:
import re

def example_find_emails(text):
    """Find all email addresses in text."""
    return re.findall(r'[\w.+-]+@[\w-]+\.[\w.]+', text)


# TODO 18: Write a function that extracts all IP addresses from a log string
# An IP address looks like: 192.168.1.1 (four groups of 1-3 digits separated by dots)
# EXAMPLE: extract_ips("Connection from 192.168.1.1 and 10.0.0.5 failed")
#    → ["192.168.1.1", "10.0.0.5"]
# EXAMPLE: extract_ips("No IPs here") → []
# HINT: Use re.findall() with pattern r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
def extract_ips(text):
    # Write your code below this line
    pass


# TODO 19: Write a function that parses log lines into structured data
# Log format: "[TIMESTAMP] LEVEL: message"
# EXAMPLE: parse_log_line("[2026-01-15 14:30:00] ERROR: Connection timeout")
#    → {"timestamp": "2026-01-15 14:30:00", "level": "ERROR", "message": "Connection timeout"}
# EXAMPLE: parse_log_line("not a log line") → None
# HINT: Use re.match() with capture groups: r'\[(.+?)\] (\w+): (.+)'
def parse_log_line(line):
    # Write your code below this line
    pass


# ============================================================================
# PART 14: IMPORTS & MULTI-FILE PROJECTS
# ============================================================================
#
# Real projects have multiple files that import from each other.
# This is how EVERY task in the simulator is structured:
#
#   src/
#       connection.py      ← defines Connection class
#       connectionPool.py  ← imports and uses Connection
#   tests/
#       test_pool.py       ← imports and tests ConnectionPool
#
# IMPORT STYLES:
#   from connection import Connection        ← import specific class
#   from validator import RecordValidator     ← import specific class
#   import json                              ← import entire module
#   from datetime import datetime, timedelta ← import multiple things
#
# RUNNING TESTS FROM PROJECT ROOT:
#   cd Task-5
#   python -m pytest tests/test_connectionPool.py -v
#
# UNDERSTANDING MODULE IMPORTS (how to read them):
#   from priorityQueue import PriorityQueue
#   ↑                         ↑
#   file: priorityQueue.py    class inside that file

# TODO 20: Write a function that simulates importing and using another module
# This function receives a "module" (actually a dict) and a function name,
# and calls that function with the given arguments
# This simulates how imports work in the tasks
# EXAMPLE:
#   math_module = {"add": lambda a, b: a + b, "multiply": lambda a, b: a * b}
#   call_module_function(math_module, "add", 3, 5) → 8
#   call_module_function(math_module, "unknown", 1, 2) → None
def call_module_function(module, func_name, *args):
    # Write your code below this line
    pass


# ============================================================================
# 🎉 You're done with Exercise 1!
# Run the tests to see how you did:
#   python -m pytest test_exercise.py -v
#
# If all tests pass, you're FULLY ready for all Python tasks in weeks 1-8!
# ============================================================================
