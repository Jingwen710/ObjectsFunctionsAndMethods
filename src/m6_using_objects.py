"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Jingwen Wu.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # Done: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------
    window = rg.RoseWindow()

    center_point = rg.Point(100, 200)
    radius = 25
    circle = rg.Circle(center_point, radius)
    circle.fill_color = 'blue'
    circle.attach_to(window)

    center_point_new = rg.Point(200, 250)
    radius_new = 10
    circle = rg.Circle(center_point_new, radius_new)
    circle.attach_to(window)

    window.render()

    window.close_on_mouse_click()


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # ------------------------------------------------------------------
    # Done: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------
    window = rg.RoseWindow()

    point_x = 200
    point_y = 200
    center_point = rg.Point(point_x, point_y)
    radius = 40
    circle = rg.Circle(center_point, radius)
    circle.outline_thickness = 5
    circle.fill_color = 'blue'
    circle.attach_to(window)

    point1 = rg.Point(10, 10)
    point2 = rg.Point(100, 100)
    rectangle = rg.Rectangle(point1, point2)
    rectangle.outline_thickness = 10
    rectangle.attach_to(window)
    center = rectangle.get_center()
    window.render()

    window.close_on_mouse_click()

    print(circle.outline_thickness)
    print(circle.fill_color)
    print(center_point)
    print(point_x)
    print(point_y)
    print(rectangle.outline_thickness)
    print(rectangle.fill_color)
    print(center)
    print(center.x)
    print(center.y)


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # Done: 4. Implement and test this function.
    # ------------------------------------------------------------------
    window = rg.RoseWindow()

    start_point = rg.Point(100, 100)
    end_point = rg.Point(200, 200)
    line = rg.Line(start_point, end_point)
    line.thickness = 20
    line.attach_to(window)
    center = line.get_midpoint()

    start_new = rg.Point(150, 150)
    end_new = rg.Point(200, 100)
    line = rg.Line(start_new, end_new)
    line.attach_to(window)

    window.render()
    window.close_on_mouse_click()

    print(center)
    print(center.x)
    print(center.y)


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
