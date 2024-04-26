my_name = "Your Name"
my_age = 19
my_personal_data = {"name": "Your Name", "age": 19}
my_first_five_things = ["AI", "punk", "Python", "solar system", "growth mindset"]
my_best_friends = [
  {"name": "Friend One", "age": 19},
  {"name": "Friend Two", "age": 20}
]
my_name = "Inne imię"

my_age = 19
print(my_age)
my_new_age = my_age  # my_new_age is now 19
print(my_new_age)
my_age = 20  # my_new_age still remains 19
print(my_age)
print(my_new_age)

my_personal_data = {
    "name": "Your Name",
    "age": 19
}

print(my_personal_data["name"])
my_personal_data["name"] = "Jan"
print(my_personal_data["name"])

my_shopping_list = ["banana", "bread", "oat milk"]

print(my_shopping_list[0])
print(my_shopping_list[1])
print(my_shopping_list[-1]) # ostatni element
my_shopping_list[0] = "olive oil"
print(my_shopping_list[0])

my_people_list = [
  {
    "name": "Your Name",
    "age": 19
  },
  {
    "name": "Another Name",
    "age": 65
  }
]

print(my_people_list[1]["name"])
my_people_list[1]["name"] = "Zbigniew"
print(my_people_list[1]["name"])

my_tuple = ("apple", "banana", "cherry")
print(my_tuple[0])

print(my_tuple)
print(my_tuple[:2] + ("orange",))

my_tuple = (
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25}
)
print(my_tuple[0]["name"])
