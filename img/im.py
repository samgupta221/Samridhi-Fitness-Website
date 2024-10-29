import curses
import time

def main(stdscr):
    # Set up the screen
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)

    # Set up the message and the box
    msg = "Gauri, Happy Valentine's Day!"
    box = "+" + "-" * len(msg) + "+"
    message_box = box + "\n" + msg + "\n" + box

    # Set up the starting position
    start_x = (sw - len(msg)) // 2
    x = start_x

    # Display the message and move it left and right
    while True:
        # Clear the screen
        w.clear()

        # Display the message
        w.addstr(sh // 2, x, message_box)
        w.refresh()

        # Wait for a short time
        time.sleep(0.1)

        # Move the message left or right
        if x == start_x:
            x += 1
        elif x == start_x - 2:
            x += 1
        else:
            x -= 1

if _name_ == "_main_":
    curses.wrapper(main)