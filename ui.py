def quiz():
    print("\n\n\nQuestion 1: How do you typically react in high-pressure situations?\n" + \
    '\nA: I become assertive and take charge.\n'+\
    'B: I become introspective and detail-oriented.\n'+\
    "C: I remain optimistic and try to keep the mood light.\n"+\
    "D: I stay calm and go with the flow.\n"+\
    "x: Pause & return to main menu")
    
    x = input("Enter Input: ")
    if x == 'x':
        main()
    
    print('\n\n\nResults: You are The Idealist\n\n'+\
        "You can continue to the main menu or enter '2' to learn about the temerament based on your result.")
    print("You can also enter '3' to retake the quiz, perhaps with different questions or length...")

    print("\n1: Continue to menu")
    print("2: Learn about 'The Idealist'")
    print("x: Retake quiz")
    x = input("Enter Input: ")
    if x == '1':
        main()
    elif x == 'x':
        length()



def length():
    print('\n\n\n')
    print('Select Quiz Length\n')
    print("Here you may select the length of the quiz of the quiz.\nMore questions means a longer, more accurate quiz.\nLess questions means a shorter, less accurate quiz")
    print("The quiz will start when you select the question number.")

    print("\nEnter the number of questions you'd like on the quiz, or...")
    print("Enter 'x' to exit to the starting menu\n")

    print("10: Ten question quiz (start)")
    print("25: Twenty-five question quiz (start)")
    print("50: Fifty question quiz (start)")
    print("x: Return to menu")
    x = input("Enter Input: ")
    if x == 'x':
        main()
    elif 10 <= int(x) <= 50:
        quiz()


def main():
    print('\n\n\nFour Temperaments Quiz\n')
    print("To proceed through the quiz and learn your temperament type, enter '1' to proceed through the questions, then come back to this menu and enter '2' to learn more!")
    print("\nEnter '1' to simply access the quiz.")
    print("Enter '2' to get more info instead of taking the quiz\n")
    
    print("1: TAKE QUIZ (start new / resume paused)")
    print("2: About the Quiz")
    print("x: Quit")
    x = input("Enter Input: ")

    if x == '1':
        length()
    elif x == 'x':
        return
    return 0

if __name__=="__main__": 
    main() 