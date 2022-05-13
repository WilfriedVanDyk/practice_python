import temperature
import datetime as dt


print("hello world")

# adding a comment is control + K ; control + C OR ctrl + /
# return None: is a good value for an empty cel in excel

# escape caracters in a string:
print("It's easy to \"escape\" characters with a leading \\.")

# Note how Python allows you to conveniently assign multiple
# values to multiple variables in a single line
first_adjective, second_adjective = "free", "open source"
f"Python is {first_adjective} and {second_adjective}."

# slicing
language = "python"
language[::2]  # Every second element
language[-1:-4:-1]  # counting backwards
# For example, if you want to get the second character out of the last three characters, you could do it like this:
language[-3:][1]

# line continuation:using parenthesis and using forward slash
a = (1 + 2
     + 3)
b = 1 + 2 \
    + 4

list_a = [a, b, c]
tuple_a = (a, b, c)
dict_a = {"key": "value", "key1": "value1"}
# returns {'EUR', 'SGD', 'USD'}
set_a = set(["USD", "USD", "SGD", "EUR", "USD", "EUR"])

# list methods: append(), insert(0, item_to_add), pop(), del list_name[0], len(), item in list_name,
# sorted(users)) # Returns a new sorted list and print(users) returns The original list unchanged
# users.sort() # Sorts the original list!!

# Python 3.9 introduced the pipe character as a dedicated merge operator for dictionaries,
# which allows you to simplify the previous expression to this:
exchange_rates = {'EURUSD': 1.2, 'GBPUSD': 1.2454,
                  'AUDUSD': 0.6161, 'CADUSD': 0.714}
exchange_rates | {"SGDUSD": 0.7004, "GBPUSD": 1.2222}
print(exchange_rates)

# using the get method to have a ... when the key doesn't excist
exchange_rates.get(100, "N/A")  # returns "N/A"

# tuples: concatenating two tuples returns an NEW TUPLE (immutable!!)

# sets
portfolio1 = {"USD", "EUR", "SGD", "CHF"}
portfolio2 = {"EUR", "SGD", "CAD"}
# Same as portfolio2.union(portfolio1)
portfolio1.union(portfolio2)  # returns {'CAD', 'CHF', 'EUR', 'SGD', 'USD'}
# Same as portfolio2.intersection(portfolio1)
portfolio1.intersection(portfolio2)  # returns {'EUR', 'SGD'}

# the use of constructors
# List [1, 2, 3] => list((1, 2, 3))
# Dictionary {"a": 1, "b": 2} => dict(a=1, b=2)
# Tuple (1, 2, 3) => tuple([1, 2, 3])
# Set {1, 2, 3} => set((1, 2, 3))

for i in range(15):
    if i == 2:
        break
    else:
        print(i)


# list comprehension
currency_pairs = ["USDJPY", "USDGBP", "USDCHF", "USDCAD", "AUDUSD", "NZDUSD"]
usd_quote = []
for pair in currency_pairs:
    if pair[3:] == "USD":
        usd_quote.append(pair[:3])
usd_quote_list_comprh = [pair[:3]
                         for pair in currency_pairs if pair[3:] == "USD"]
# dict comprehension
exchange_rates = {"EURUSD": 1.1152,
                  "GBPUSD": 1.2454,
                  "AUDUSD": 0.6161}
exchange_rates_dict_compreh = {k: v * 100 for (k, v) in exchange_rates.items()}
# set comprehension
currency_pairs_set_compreh = {
    s + "USD" for s in ["EUR", "GBP", "EUR", "HKD", "HKD"]}

# functions
# def function_name(required_argument, optional_argument=default_value, ...):
# return value1, value2, ...
#  value1, value2, ... = function_name(positional_arg, arg_name=value, ...)


print(temperature.TEMPERATURE_SCALES)  # capitals becaus its a constant!!

# Python creates a folder called __pycache__ with files that have the .pyc extension.
# These are bytecode-compiled files that the Python interpreter creates when you import a module.

# dt.datetime(year, month, day, hour, minute, second, microsecond, timezone)
# The difference of two datetime objects returns a timedelta object
timestamp = dt.datetime(2020, 1, 31, 14, 30)
timestamp - dt.datetime(2020, 1, 14, 12, 0)
# returns a dt.timedelta object : datetime.timedelta(days=17, seconds=9000)
# Accordingly, you can also work with timedelta objects
time_plus_timededelta = timestamp + dt.timedelta(days=1, hours=4, minutes=11)

# Format a datetime object in a specific way
# You could also use an f-string: f"{timestamp:%d/%m/%Y %H:%M}"
timestamp.strftime("%d/%m/%Y %H:%M")  # '31/01/2020 14:30'
# Parse a string into a datetime object
# out[124]: datetime.datetime(2020, 1, 12, 0, 0)
dt.datetime.strptime("12.1.2020", "%d.%m.%Y")
