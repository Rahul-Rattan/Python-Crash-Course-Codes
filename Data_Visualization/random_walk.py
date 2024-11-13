from random import choice

class RandomWalk:
    """A class to generate random walks"""
    def __init__(self, num_points=5000):
        self.num_points=num_points

        #All walks starts at 0,0
        self.x_value=[0]
        self.y_value=[0]

    def fill_walk(self):
        """Calculate all the points in the walk."""
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_value)<self.num_points:
            # Decide which direction to go, and how far to go.
            x_direction=choice([1,-1])
            x_distance=choice([0,1,2,3,4])
            x_step=x_distance*x_direction

            y_direction=choice([1,-1])
            y_distance=choice([0,1,2,3,4])
            y_step=y_distance*y_direction

            #Reject moves that go no where
            if x_step==0 and y_step==0:
                continue

            #Calculate new positions
            x=self.x_value[-1]+x_step
            y=self.y_value[-1]+y_step

            self.x_value.append(x)
            self.y_value.append(y)

            

