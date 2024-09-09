class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, descr=''):
        self.ledger.append({"amount": amount, "description": descr})

    def withdraw(self, amount, descr=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": descr})  # Ensure withdrawal is negative
            return True
        return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")  # Fix typo in description
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def check_funds(self, amount):
        return self.get_balance() >= amount  # Call the method with parentheses

    def __str__(self):
        title = f"{self.name:*^30}\n"  # 1
        items = ""  # 2
        total = 0  # 3
        for item in self.ledger:  # 4
            desc = f"{item['description'][:23]:23}"  # 5
            amt = f"{item['amount']:>7.2f}"  # 6
            items += f"{desc}{amt}\n"  # 7
            total += item["amount"]  # 8
        output = title + items + f"Total: {total:.2f}"  # 9
        return output  # 10


def create_spend_chart(categories):
    total_spent = 0
    spent_per_category = []

    # 1. Calculate the total spent in each category and the total overall spent
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_per_category.append(spent)
        total_spent += spent

    # 2. Calculate percentage spent for each category
    percentages = [int((spent / total_spent) * 100) // 10 * 10 for spent in spent_per_category]

    # 3. Start building the chart
    chart = "Percentage spent by category\n"

    # 4. Add percentage bars to the chart
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percent in percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    # 5. Add the separator line
    chart += "    -" + "---" * len(categories) + "\n"

    # 6. Find the longest category name length for proper vertical alignment
    max_len = max(len(category.name) for category in categories)

    # 7. Add category names vertically below the bars
    for i in range(max_len):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += f"{category.name[i]}  "
            else:
                chart += "   "
        chart += "\n"

    return chart.rstrip("\n")


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')

clothing = Category('Clothing')
food.transfer(50, clothing)

auto = Category('Auto')
auto.deposit(1000, 'deposit')
auto.withdraw(15)

print(food)
print(clothing)
print(auto)
print(create_spend_chart([food, clothing, auto]))
