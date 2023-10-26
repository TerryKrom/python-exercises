def truncate(n):
  return int(n * 10) / 10


def getTotals(categories):
  total = 0
  breakdown = []
  for category in categories:
    total += category.get_withdrawls()
    breakdown.append(category.get_withdrawls())
  rounded = list(map(lambda x: truncate(x / total), breakdown))
  return rounded


def create_spend_chart(categories):
  res = 'Percentage spent by category\n'
  spendings = [category.get_withdrawls() for category in categories]
  total_spent = sum(spendings)

  for i in range(100, -1, -10):
    res += str(i).rjust(3) + "| "
    for spending in spendings:
      category_percentage = spending / total_spent * 100
      if category_percentage >= i:
        res += "o  "
      else:
        res += "   "
    res += "\n"

  res += "    -" + "---" * len(categories) + "\n"

  max_name_length = max(len(category.name) for category in categories)
  for i in range(max_name_length):
    res += "     "
    for category in categories:
      if i < len(category.name):
        res += category.name[i] + "  "
      else:
        res += "   "
    if i < max_name_length - 1:
      res += "\n"

  return res


class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = []

  def __str__(self):
    title = "{0}".format(self.name.center(30, "*"))
    items = ""
    total = 0
    for item in self.ledger:
      items += "{0:23}{1:>7.2f}\n".format(item["description"][:23],
                                          item["amount"])
      total += item["amount"]
    output = title + "\n" + items + "Total: " + str(total)
    return output

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  def get_balance(self):
    balance = 0
    for transaction in self.ledger:
      balance += transaction["amount"]
    return balance

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)
      return True
    return False

  def check_funds(self, amount):
    if self.get_balance() >= amount:
      return True
    return False

  def get_withdrawls(self):
    total = 0
    for item in self.ledger:
      if item['amount'] < 0:
        total += item["amount"]
    return total


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))

#app made for freecodecamp course