while True:
    print("==============================")
    print("\nPYTHON LEARNING SYSTEM ")
    print("==============================")

    print("\n📙PRELIM LESSON")
    print("1. Fundamentals of Programming")
    print("2. Python Basic Syntax")
    print("3. Printing Output")
    print("4. Python Comments")
    print("5. Variables and Data Types")
    print("6. Arithmetic Operators")
    print("7. Basic Input and Output")

    print("\n📘MIDTERM LESSON")
    print("8. Conditional Statement")
    print("9. If-elif-else Statement")
    print("10. Logical Operator")

    print("\n📕FINAL LESSON")
    print("11. Introduction to Iteration and Loop")
    print("12. For Loop")
    print("13. While Loop")

    print("\n📝 QUIZ TIME!!! ")
    print("14. Matching Type Quiz (Lessons 1-13)")

    print("\n0. Exit")
    print("==============================")
    
    try:
        lesson = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 14.")
        continue

    print("==============================")
    if lesson == 0:
        print("Exiting....")
        break

    # PRELIM LESSON
    elif lesson == 1:
        print("📙 FUNDAMENTALS OF PROGRAMMING")
        print("* Python is a high-level, interpreted programming language.")
        print("* It is beginner-friendly and widely used for data analysis, web development, and AI.")
    elif lesson == 2:
        print("📙 PYTHON BASIC SYNTAX")
        print("* Syntax refers to the set of rules that tells us how to correctly write a program in Python.")
        print("* Example:")
        print('  print("Hello, Python!")')
    elif lesson == 3:
        print("📙 PRINTING OUTPUT")
        print("* The print() function displays information on the screen.")
        print("* Example:")
        print('  print("Hi, World!")')
    elif lesson == 4:
        print("📙 PYTHON COMMENTS")
        print("* Comments are ignored by the interpreter.")
        print("* They help explain the code to humans.")
        print("* Example:")
        print("  # This is a comment")
    elif lesson == 5:
        print("📙 VARIABLES AND DATA TYPES")
        print("* A variable is like a container that stores data.")
        print("* Example:")
        print("  age = 25           # int")
        print("  name = 'Alice'     # str")
        print("  pi = 3.14          # float")
        print("  is_student = True  # bool")
        print("\nData Types:")
        print("* int   - Integer (whole number)")
        print("* float - Decimal numbers")
        print("* str   - String (text)")
        print("* bool  - Boolean (True or False)")
    elif lesson == 6:
        print("📙 ARITHMETIC OPERATORS")
        print("* Arithmetic refers to basic math operations.")
        print("Common Arithmetic Operators:")
        print("Operation        Symbol    Example     Result")
        print("Addition           +         5+2          7")
        print("Subtraction        -         5-2          3")
        print("Multiplication     *         5*2         10")
        print("Division           /         5/2         2.5")
        print("Floor Division     //        5//2        2")
        print("Modulus            %         5%2         1")
        print("Exponentiation     **        5**2        25")
    elif lesson == 7:
        print("📙 BASIC INPUT AND OUTPUT")
        print("* The input() function takes user input as a string.")
        print("* Example:")
        print('  name = input("Enter your name: ")')
        print('  print("Hello,", name)')

    # MIDTERM LESSON
    elif lesson == 8:
        print("📘 CONDITIONAL STATEMENT")
        print("* Conditional statements help your program make decisions.")
        print("* Example:")
        print("  age = 18")
        print("  if age == 18:")
        print('   print("You are a debutant!")')

    elif lesson == 9:
        print("📘 IF-ELIF-ELSE STATEMENT")
        print("* If-Elif-Else Statement allows a program to make decisions based on different conditions.")
        print("\nExample 1: Basic if-else")
        print('  age = int(input("Enter your age: "))')
        print("  if age >= 18:")
        print('   print("You are an adult.")')
        print("  else:")
        print('   print("You are a minor.")')
        print("\nExample 2: if-elif-else")
        print('  grade = int(input("Enter your grade: "))')
        print("  if grade >= 90:")
        print('   print("Excellent!")')
        print("  elif grade >= 75:")
        print('   print("Good job!")')
        print("  else:")
        print('   print("Needs improvement.")')
        print("\nExample 3: Nested Condition")
        print('  num = int(input("Enter a number: "))')
        print("  if num > 0:")
        print('   print("Positive number")')
        print("   if num % 2 == 0:")
        print('    print("It is even")')
        print("  else:")
        print('   print("It is odd")')
        print("  else:")
        print('   print("Zero or negative number")')

    elif lesson == 10:
        print("📘 LOGICAL OPERATOR")
        print("* Logical Operators combine two or more conditions and return True or False.")
        print("3 types of Logical Operators:")
        print("* and - Both conditions must be True")
        print("  Example:")
        print("  age = 20")
        print("  if age >= 18 and age <= 60:")
        print('      print("Allowed")')
        print("* or - At least one condition must be True")
        print("  Example:")
        print('  day = "Saturday"')
        print('  if day == "Saturday" or day == "Sunday":')
        print('      print("It\'s the weekend!")')
        print("* not - Reverses the result")
        print("  Example:")
        print("  is_raining = False")
        print("  if not is_raining:")
        print(' print("You can go outside.")')

    # FINAL LESSON
    elif lesson == 11:
        print("📕 INTRODUCTION TO ITERATION AND LOOP")
        print("* Iteration is the process of repeating a set of instructions until a condition is met.")
        print("* Python uses 'for' loops and 'while' loops to perform iteration.")
    elif lesson == 12:
        print("📕 FOR LOOP")
        print("* Repeats instructions for each item in a sequence.")
        print("* Example:")
        print("  for number in range(3):")
        print('      print("Hello!")')
    elif lesson == 13:
        print("📕 WHILE LOOP")
        print("* Repeats instructions while a condition is True.")
        print("* Example:")
        print("  count = 1")
        print("  while count <= 3:")
        print('      print("Hello!")')
        print("      count += 1")

    # MATCHING TYPE QUIZ
    elif lesson == 14:
        print("📝 MATCHING TYPE QUIZ (LESSONS 1-13)")
        print("Directions: Match each topic in Column A with its description in Column B.")
        print("Type the letter (A-M) for each item.\n")

        choices = [
            "A. Repeats instructions while a given condition remains True (e.g., while count <= 3:)",
            "B. A container that stores values like int, float, str, and bool",
            "C. Operators like and, or, and not used to combine multiple conditions",
            "D. The print() function used to display information on the screen",
            "E. The general concept of repeating a block of code multiple times",
            "F. High-level, interpreted language used in AI, web development, and data analysis",
            "G. Allows a program to choose between multiple conditions using if, elif, and else",
            "H. Symbols like +, -, *, /, //, %, and ** used for basic math",
            "I. Text starting with # that is ignored by the interpreter and explains code to humans",
            "J. Repeats instructions for each item in a sequence (e.g., for number in range(3):)",
            "K. The set of rules that tells us how to write a Python program properly",
            "L. Uses a single if check to help a program make a basic decision",
            "M. Uses the input() function to get user data as a string"
        ]

        print("--- COLUMN B (CHOICES) ---")
        for choice in choices:
            print(choice)
        print("--------------------------\n")

        questions = [
            ("1. Fundamentals of Programming", "F"),
            ("2. Python Basic Syntax", "K"),
            ("3. Printing Output", "D"),
            ("4. Python Comments", "I"),
            ("5. Variables and Data Types", "B"),
            ("6. Arithmetic Operators", "H"),
            ("7. Basic Input and Output", "M"),
            ("8. Conditional Statement", "L"),
            ("9. If-elif-else Statement", "G"),
            ("10. Logical Operator", "C"),
            ("11. Introduction to Iteration and Loop", "E"),
            ("12. For Loop", "J"),
            ("13. While Loop", "A")
        ]

        score = 0
        for question, correct_answer in questions:
            user_ans = input(f"{question}: ").strip().upper()
            if user_ans == correct_answer:
                print("   ✅ Correct!\n")
                score += 1
            else:
                print(f"   ❌ Incorrect. The correct answer is {correct_answer}.\n")

        print("==============================")
        print(f"QUIZ COMPLETE! Your Score: {score}/{len(questions)}")
        print("==============================")

    else:
        print("Invalid choice. Please enter a number between 0 and 14.")
        