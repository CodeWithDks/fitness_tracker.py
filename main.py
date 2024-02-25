class User:
  def __init__(self, username, password, age, weight, height, fitness_goal):
      self.username = username
      self.password = password
      self.age = age
      self.weight = weight
      self.height = height
      self.fitness_goal = fitness_goal
      self.workouts = []
      self.meals = []

  def record_workout(self, workout):
      self.workouts.append(workout)

  def log_meal(self, meal):
      self.meals.append(meal)

  def display_progress(self):
      # Calculate and display user's progress towards fitness goal
      pass


class Workout:
  def __init__(self, type, duration, calories_burned):
      self.type = type
      self.duration = duration
      self.calories_burned = calories_burned


class Meal:
  def __init__(self, name, calories):
      self.name = name
      self.calories = calories


def main():
  print("Welcome to Fitness Tracker App!")

  # User Registration
  username = input("Enter username: ")
  password = input("Enter password: ")
  age = int(input("Enter age: "))
  weight = float(input("Enter weight (in kg): "))
  height = float(input("Enter height (in cm): "))
  fitness_goal = input("Enter fitness goal: ")

  user = User(username, password, age, weight, height, fitness_goal)

  # Main Menu
  while True:
      print("\nMain Menu:")
      print("1. Record Workout")
      print("2. Log Meal")
      print("3. Display Progress")
      print("4. Exit")

      choice = input("Enter your choice: ")

      if choice == "1":
          type = input("Enter workout type: ")
          duration = float(input("Enter duration (in minutes): "))
          calories_burned = float(input("Enter calories burned: "))
          workout = Workout(type, duration, calories_burned)
          user.record_workout(workout)
          print("Workout recorded successfully!")

      elif choice == "2":
          name = input("Enter meal name: ")
          calories = float(input("Enter calories: "))
          meal = Meal(name, calories)
          user.log_meal(meal)
          print("Meal logged successfully!")

      elif choice == "3":
          user.display_progress()

      elif choice == "4":
          print("Thank you for using Fitness Tracker App!")
          break

      else:
          print("Invalid choice. Please try again.")


if __name__ == "__main__":
  main()
