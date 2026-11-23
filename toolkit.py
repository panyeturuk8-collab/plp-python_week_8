import time


# Tool 1: Manages an in-memory task list so users can add, view, and remove items while the program runs.
def run_task_list(tasks):
    print("\n--- Quick Task List ---")
    while True:
        print("\nWhat would you like to do with your tasks?")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Back to main menu")

        action = input("Enter choice (1-4): ").strip()

        if action == "1":
            if not tasks:
                print("Your task list is currently empty.")
            else:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"  {index}. {task}")

        elif action == "2":
            new_task = input("Enter a new task: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"Added '{new_task}'! You now have {len(tasks)} task(s).")
            else:
                print("Task cannot be blank. Nothing was added.")

        elif action == "3":
            if not tasks:
                print("No tasks to remove.")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"  {index}. {task}")
                choice = input("Enter the task number to remove: ").strip()
                if choice.isdigit():
                    num = int(choice)
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        print(f"Removed '{removed}'.")
                    else:
                        print(f"Please choose a number between 1 and {len(tasks)}.")
                else:
                    print("Please enter a valid number.")

        elif action == "4":
            print("Returning to the main menu...")
            break

        else:
            print("Invalid choice. Please pick a number from 1 to 4.")


# Tool 2: Collects expense amounts in a loop, sums them, and uses conditionals to compare against a target budget.
def run_expense_check():
    print("\n--- Daily Expense & Budget Check ---")
    budget_input = input("Enter your daily budget target (e.g., 1000): ").strip()

    try:
        daily_budget = float(budget_input)
        if daily_budget <= 0:
            print("Please enter a budget greater than 0.")
            return
    except ValueError:
        print("That wasn't a valid number. Returning to main menu.")
        return

    expenses = []
    print("Enter each expense amount. Type 'done' when finished.")

    while True:
        entry = input("Expense amount (or 'done'): ").strip().lower()
        if entry == "done":
            break
        try:
            amount = float(entry)
            if amount < 0:
                print("Expense amount cannot be negative. Try again.")
            else:
                expenses.append(amount)
                print(f"Recorded {amount:.2f}.")
        except ValueError:
            print("Invalid input. Enter a number or 'done'.")

    total_spent = 0.0
    for item in expenses:
        total_spent += item

    difference = abs(daily_budget - total_spent)

    print(f"\nTotal items logged: {len(expenses)}")
    print(f"Total spent: {total_spent:.2f} | Target budget: {daily_budget:.2f}")

    if total_spent < daily_budget:
        print(f"Great job! You are {difference:.2f} under your daily budget.")
    elif total_spent == daily_budget:
        print("Spot on! You matched your daily budget exactly.")
    else:
        print(f"Heads up! You are {difference:.2f} over your daily budget.")


# Tool 3: Runs a countdown loop in seconds so the user can time a short focus or study sprint.
def run_countdown_timer():
    print("\n--- Study Session Timer ---")
    raw_seconds = input("Enter countdown duration in seconds (e.g., 10): ").strip()

    if not raw_seconds.isdigit():
        print("Please enter a whole number of seconds.")
        return

    seconds_left = int(raw_seconds)
    if seconds_left <= 0:
        print("Duration must be greater than 0 seconds.")
        return

    print(f"Starting timer for {seconds_left} second(s)... Press Ctrl+C to stop early.")
    try:
        while seconds_left > 0:
            print(f"Time remaining: {seconds_left}s")
            time.sleep(1)
            seconds_left -= 1
        print("Time's up! Great focus session.")
    except KeyboardInterrupt:
        print("\nTimer stopped early.")


def show_menu():
    print("\n========================================")
    print("        PERSONAL MINI-TOOLKIT")
    print("========================================")
    print("1. Quick Task List")
    print("2. Daily Expense & Budget Check")
    print("3. Study Session Timer")
    print("4. Quit")
    print("----------------------------------------")


def main():
    print("Welcome to your Personal Mini-Toolkit!")
    print("Pick a tool below to get started whenever you're ready.")

    # Shared list persists across menu visits during the current session
    session_tasks = []

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            run_task_list(session_tasks)
        elif choice == "2":
            run_expense_check()
        elif choice == "3":
            run_countdown_timer()
        elif choice == "4":
            print("\nThanks for using the Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print(f"\n'{choice}' is not a valid option. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
