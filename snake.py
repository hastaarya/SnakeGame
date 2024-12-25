from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self): #initialize segment to store the new segment to be created
        self.segments = []
        self.create_snake() #create starting snake
        self.head = self.segments[0] #set head so we dont need to use self.segments[0] everytime

    def create_snake(self):
        for position in STARTING_POSITIONS: #create snakes from the starting coordinates
            self.add_segment(position)

    def add_segment(self, position): #add segment by creating a new turtle class, setup color to white, removing the lines
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment) #append the newly created segment to a lists

    def extend(self):
        self.add_segment(self.segments[-1].position()) #extend the tail by adding segments to the very back of the segment

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1): #using reverse loop so that the previous coordinate of the segment could follow the route made by snake head
            new_x = self.segments[seg_num - 1].xcor() #setting new coordinates with the previous coordinate of snake head
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE) #move snake forward

    def up(self): #turtle going up
        if self.head.heading() != DOWN: #if snake currently not facing down only then would it be allowed to go up
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN) #go down
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)#go left
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT) # go right

    def reset_snake(self):        
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake() #create starting snake
        self.head = self.segments[0] #set head so we dont need to use self.segments[0] everytime