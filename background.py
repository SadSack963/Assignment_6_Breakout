import constants as c

from turtle import Turtle


def draw_gradient(start_color, target_color):
    tim = Turtle()
    tim.color(start_color)
    tim.penup()
    tim.goto(-c.WIDTH / 2, c.HEIGHT / 2)  # Move to top left of screen
    tim.pendown()

    # Get the incremental change in color RGB values from Start to Target
    # This is the amount that the RGB values must change as we move down the screen line by line
    delta_color_list = [(target_component - start_color[index]) / c.HEIGHT for index, target_component in enumerate(target_color)]

    direction = 1  # Turtle direction of travel (left to right)
    for line, y_coord in enumerate(range(c.HEIGHT // 2, -c.HEIGHT // 2, -1)):
        tim.forward(c.WIDTH * direction)  # Draw a line
        # Calculate the new RGB values ready for the next line
        calc_color = [int(start_color[index] + delta * line) for index, delta in enumerate(delta_color_list)]
        new_color = tuple(calc_color)  # Convert list to tuple
        tim.color(new_color)
        tim.sety(y_coord)  # Move the turtle down a line
        direction *= -1  # Change the turtle direction of travel


# GRADIENT REALLY SLOWS DOWN BALL ANIMATION
# =========================================
# start_color = level_layout.levels[next_level]["start_color"]
# target_color = level_layout.levels[next_level]["target_color"]
# draw_gradient(start_color, target_color)


if __name__ == "__main__":
    from turtle import Screen

    START_COLOR = (128, 255, 255)
    TARGET_COLOR = (60, 50, 160)
    WIDTH = 600
    HEIGHT = 400

    screen = Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.colormode(255)
    screen.tracer(0)

    draw_gradient(START_COLOR, TARGET_COLOR)

    screen.update()

    screen.exitonclick()
