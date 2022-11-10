import operator
import random
import emoji
answer = 0
question = "Let's Start To The Quiz"


def createQuestion():
    newquestion = ""
    ops = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul, }
    num1 = random.randint(0, 11)
    num2 = random.randint(1, 11)
    op = random.choice(list(ops.values()))
    if op == operator.add:
        newquestion = str(num1)+"+"+str(num2)
    elif op == operator.sub:
        newquestion = str(num1)+"-"+str(num2)
    elif op == operator.mul:
        newquestion = str(num1)+"x"+str(num2)
    global answer
    answer = op(num1, num2)
    return newquestion


while True:
    print(question)
    if question != "Let's Start To The Quiz":
        inanswer = input("Your Answer:")
        try:
            if float(inanswer) == float(answer):
                print("---------------------- God Damn, Right! ----------------------")
                print(str(answer))
                question = createQuestion()
            else:
                print("Sorry...")
                print(str(answer))
                question = createQuestion()
                continue
        except:
            print("Sorry...")
            question = createQuestion()
            continue
    else:
        question = createQuestion()
        continue
