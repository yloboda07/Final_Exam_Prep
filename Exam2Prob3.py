from pgl import GWindow, GCompound, GArc

COLORS = ["red", "green", "blue", "orange"] #colors 
GW_WIDTH = 500 # width of window 
GW_HEIGHT = 500 # height of window 
CHART_RADIUS = 150 # radius of pie chart 
HIGHLIGHT_THICKNESS = 10 # line thickness when clicked

gw = GWindow(GW_WIDTH, GW_HEIGHT)

def create_pie_chart(data):
    def down_action(e):
        vx, vy = e.get_x(), e.get_y()
        obj = gw.get_element_at(vx, vy)
        if obj != None:
            obj.send_to_front()
            obj.set_line_width(10)
    def up_action(e):
        vx, vy = e.get_x(), e.get_y()
        obj = gw.get_element_at(vx, vy)
        if obj != None:
            obj.set_line_width(1)
    gw = GWindow(GW_WIDTH, GW_HEIGHT) 
    start = 0 
    i = 0
    for entry in data: 
        stride = int(entry/100*360) 
        x = GW_WIDTH / 2- CHART_RADIUS 
        y = GW_HEIGHT / 2- CHART_RADIUS 
        arc = GArc(x, y, 2*CHART_RADIUS,2*CHART_RADIUS, start, stride) 
        arc.set_filled(True) 
        arc.set_fill_color(COLORS[i % len(COLORS)]) 
        gw.add(arc) 
        start += stride 
        i += 1
    gw.add_event_listener("mousedown", down_action)
    gw.add_event_listener("mouseup", up_action)

create_pie_chart([50, 30, 20])





















# def create_pie_chart(list_of_percents):
#     arc = GArc(GW_WIDTH/2-CHART_RADIUS/2, GW_HEIGHT/2-CHART_RADIUS/2, 
#     CHART_RADIUS, CHART_RADIUS, 
#     0, 360*list_of_percents[0]/100)
#     arc.set_filled(True)
#     arc.set_fill_color(COLORS[0])
#     gw.add(arc)
#     for i in range (1,len(list_of_percents)):
#         arc_end = arc.get_end_point()
#         ax = arc_end.get_x()
#         ay = arc_end.get_y()
#         sweep_angle = arc.get_sweep_angle()
#         start_angle = arc.get_start_angle()
#         arc_angle = sweep_angle + start_angle
#         print(ax,ay)
#         percent = list_of_percents[i]
#         arc = GArc(ax, ay, CHART_RADIUS, CHART_RADIUS, arc_angle, 360*percent/100)
#         arc.set_location(ax, ay)
#         arc.set_filled(True)
#         arc.set_fill_color(COLORS[i])
#         gw.add(arc)

# create_pie_chart([10, 10, 10, 10, 50, 10])