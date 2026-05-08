from pgl import GWindow, GRect, GCompound, GLabel


SQUARE_SIZE = 60 
GWINDOW_WIDTH = 4 * SQUARE_SIZE 
GWINDOW_HEIGHT = 4 * SQUARE_SIZE 
SQUARE_FILL_COLOR = "LightGray" 
PUZZLE_FONT = "18px 'Sans-Serif'"
NROWS = 4
NCOLS = NROWS

def set_up_square():
    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    for row in range (NROWS):
        for col in range (NCOLS):
            grid = GCompound()
            square = GRect(SQUARE_SIZE*col,SQUARE_SIZE*row, SQUARE_SIZE, SQUARE_SIZE)
            square.set_filled(True)
            square.set_fill_color(SQUARE_FILL_COLOR)
            if col == 3 and row == 3:
                gw.remove(square)
            else:
                number = GLabel(f"{row*NCOLS+col+1}",SQUARE_SIZE*col,SQUARE_SIZE*row+SQUARE_SIZE)
                number.set_font(PUZZLE_FONT)
                number.move(SQUARE_SIZE/2-number.get_width()/2,-SQUARE_SIZE/2+number.get_width()/2)
                grid.add(square)
                grid.add(number)
                gw.add(grid)

    def change_configuration(event):
        mx, my = event.get_x(), event.get_y()
        current = gw.get_element_at(mx, my)
        if current is not None:
            for x, y in [(-1,0),(1,0),(0,-1),(0,1)]:
                cx = mx + SQUARE_SIZE*x
                cy = my + SQUARE_SIZE*y
                if ((0 < cx < GWINDOW_WIDTH) and
                (0 < cy < GWINDOW_HEIGHT)):
                    elem = gw.get_element_at(cx, cy)
                    if elem is None:
                        current.move(x*SQUARE_SIZE,y*SQUARE_SIZE)
                        return 
        

    gw.add_event_listener("click", change_configuration)
set_up_square()