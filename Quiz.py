def START(questions):
    score = 0
    missing = 0
    # one by one read the question and answer from the object
    for question, answer in questions.items():
        print(question)
        user_answer = (
            input("Your answer: ").strip().capitalize()
        )  # convert the input of the user into the capitalize

        # check user enter answer is correct or not
        if user_answer == answer:
            print("Correct!\n")
            score += 1
        else:
            if user_answer == "":
                # calculate the maximum empty attempt and then break the Quiz
                if missing == 6:
                    print(f"☹️ : You missed maximum questions, try again next time")
                    break
                else:
                    missing += 1
                    print(f"you missed {missing} question \n")
            else:
                #  if user enter answer is wrong 
                print(
                    f"{user_answer} is wrong answer, Here is the correct answer: {answer}\n"
                )

                # calculate the score and verify either user passed or failed
    scored = ((score * len(quiz_questions)) / 100) * 100
    if scored <= 3:
        print(f"😐: Failed!, You need to improve your knowledge")
    else:
        print(f"Quiz completed! You scored {scored}% ")


# question  object
quiz_questions = {
    "1) What is the capital city of Australia?": "Canberra",
    "2) Which river is the longest in South America?": "The amazon river",
    "3) What is the highest mountain peak in North America?": "Denali",
    "4) Which country is known as the 'Land of the Midnight Sun'?": "Norway",
    "5) What is the largest lake in Africa by surface area?": "Lake victoria",
    "6) Which ocean is the warmest?": "The indian ocean",
    "7) What is the longest river entirely within Germany?": "The rhine river",
    "8) Which city is considered the birthplace of democracy?": "Athens greece",
    "9) What is the largest island in the Mediterranean Sea?": "Sicily",
    "10) Which country is the smallest in the world by land area?": "Vatican city",
}

# Call the function to start the quiz
START(quiz_questions)
