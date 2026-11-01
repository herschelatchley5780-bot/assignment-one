# Name: gu zhewen
# Assignment One

"""A colourful Turtle drawing and a keyword-based question answering bot.

Run this file with Python 3 in a desktop terminal, then choose a menu option.
Only Python's standard library is used.
"""

import math
import re
import turtle


def draw_star(pen, length):
    """Draw a five-pointed star using five equal sides."""
    for side in range(5):
        pen.forward(length)
        pen.right(144)


def turtle_drawing():
    """Draw Rainbow Orbit with changing colours, lengths and angles."""
    screen = turtle.Screen()
    screen.setup(width=920, height=780)
    screen.title("Assignment One | Rainbow Orbit")
    screen.bgcolor("#0b1226")
    screen.tracer(0)

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    colours = ["#43e8d8", "#60a5fa", "#a78bfa",
               "#f472b6", "#fb923c", "#fde047"]

    # Outer loop changes the colour, size and rotation of each star.
    pen.pensize(2)
    for index in range(36):
        length = 155 + index * 3
        pen.pencolor(colours[index % len(colours)])
        pen.penup()
        pen.goto(0, -15)
        pen.setheading(index * 10)
        pen.pendown()
        draw_star(pen, length)

    # Place smaller stars around the orbit using a second structured loop.
    for index in range(18):
        angle = math.radians(index * 20)
        pen.penup()
        pen.goto(305 * math.cos(angle), 305 * math.sin(angle) - 15)
        pen.setheading(index * 20 + 90)
        pen.pencolor(colours[index % len(colours)])
        pen.pendown()
        draw_star(pen, 12 + (index % 3) * 5)

    pen.penup()
    pen.goto(0, 335)
    pen.pencolor("#f1f5f9")
    pen.write("RAINBOW ORBIT", align="center", font=("Arial", 23, "bold"))
    pen.goto(0, -365)
    pen.pencolor("#cbd5e1")
    pen.write("36 stars | 6 colours | changing side lengths", align="center",
              font=("Arial", 12, "normal"))
    screen.update()
    print("Drawing complete. Close the drawing window to return to the menu.")
    screen.mainloop()
    # Turtle sets this flag to False when the window is closed.
    # Reset it so that selecting the drawing again can create a fresh window.
    turtle.TurtleScreen._RUNNING = True


def answer_question(question):
    """Return one answer; when several keywords occur, use the order below."""
    # Match whole words so that 'ai' does not accidentally match 'rain'.
    words = re.findall(r"[a-z0-9]+", question.lower())
    if "hku" in words:
        return "HKU stands for The University of Hong Kong."
    elif "robot" in words or "robots" in words:
        return "A robot is a programmable machine that can sense and act."
    elif "jetson" in words:
        return ("Jetson Nano is a small NVIDIA computer for edge AI, "
                "including image classification and object detection.")
    elif "ai" in words:
        return ("AI means Artificial Intelligence. It enables computers to "
                "perform tasks such as image or speech recognition.")
    elif "human" in words or "humans" in words:
        return ("Humans learn from experience and use reasoning and "
                "creativity to solve problems.")
    elif "hello" in words or "hi" in words:
        return "Hello! Ask me about HKU, robot, jetson, ai or human."
    elif not words:
        return "Please type a question."
    else:
        return "Sorry, I do not understand. Try HKU, robot, jetson, ai or human."


def qa_bot():
    """Keep receiving questions with input() until the user chooses to exit."""
    print("\nQuestion Answering Bot")
    print("Keywords: HKU, robot, jetson, ai, human")
    print("If several keywords occur, priority is HKU > robot > jetson > ai > human.")
    print("Type quit, exit or bye to return to the menu.")
    while True:
        question = input("You: ").strip()
        if question.lower() in ("quit", "exit", "bye"):
            print("Bot: Goodbye!")
            break
        else:
            print("Bot:", answer_question(question))


def main():
    """Offer both assignment tasks in a single Python file."""
    while True:
        print("\nAssignment One")
        print("1. Turtle Drawing")
        print("2. QA Bot")
        print("0. Exit")
        choice = input("Choose 1, 2 or 0: ").strip()
        if choice == "1":
            turtle_drawing()
        elif choice == "2":
            qa_bot()
        elif choice == "0":
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 0.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nProgram ended.")

