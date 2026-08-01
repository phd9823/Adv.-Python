
# Decorator for formatting reports
def add_border(func):
    def wrapper(*args, **kwargs):
        print("=" * 50)
        func(*args, **kwargs)
        print("=" * 50)
    return wrapper


class Report:
    # Class variable
    template = "General Report"

    # Constructor
    def __init__(self, title, content):
        self.title = title
        self.content = content

    # Class Method
    @classmethod
    def set_template(cls, new_template):
        cls.template = new_template

    # Magic Method (__str__)
    def __str__(self):
        return f"Template : {Report.template}\nTitle    : {self.title}\nContent  : {self.content}"

    # Magic Method (__len__)
    def __len__(self):
        return len(self.content)

    # Decorator Applied
    @add_border
    def display(self):
        print(self)

    # Convert content to uppercase
    def uppercase(self):
        self.content = self.content.upper()

    # Convert content to lowercase
    def lowercase(self):
        self.content = self.content.lower()


# Main Program

print("Dynamic Report Generator")

while True:
    print("\n1. Create Report")
    print("2. Change Template")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        title = input("Enter Report Title: ")
        content = input("Enter Report Content: ")

        report = Report(title, content)

        print("\nFormatting Options")
        print("1. Uppercase")
        print("2. Lowercase")
        print("3. No Formatting")

        option = input("Choose Option: ")

        if option == "1":
            report.uppercase()
        elif option == "2":
            report.lowercase()

        report.display()

        print("Content Length:", len(report))

    elif choice == "2":
        temp = input("Enter New Template Name: ")
        Report.set_template(temp)
        print("Template Updated Successfully!")

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")