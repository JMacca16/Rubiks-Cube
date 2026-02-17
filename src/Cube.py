import numpy as np

class cube:
    # Top defined as White Face, Front Defined as Red
    def __init__(self):
        self.faces = {
            "White" : np.full((3,3), 0), #White (0)
            "Yellow" : np.full((3,3), 1), #Yellow (1)
            "Red" : np.full((3,3), 2), #Red (2)
            "Orange" : np.full((3,3), 4), #Orange (4)
            "Blue" : np.full((3,3), 5), #Blue (5)
            "Green" : np.full((3,3), 6) #Green (6)
        }

    def face_turn_clockwise(self, face: str):
        self.faces[face] = np.rot90(self.faces[face], -1)

        if face == 'White':
            # Top Row Moves (Red <- Blue <- Orange <- Green <- Red)
            temp_red = self.faces['Red'][0, :].copy()
            self.faces['Red'][0, :] = self.faces['Blue'][0, :]
            self.faces['Blue'][0, :] = self.faces['Orange'][0, :]
            self.faces['Orange'][0, :] = self.faces['Green'][0, :]
            self.faces['Green'][0, :] = temp_red

        if face == 'Yellow':
            # Bottom Row Moves (Red <- Green <- Orange <- Blue <- Red
            temp_red = self.faces['Yellow'][2, :].copy()
            self.faces['Green'][2, :] = self.faces['Orange']

        if face == 'Red':
            # Left Row Moves (White <- Blue
            temp_red = self.faces['Red'][0, :].copy()
            self.faces['White'][2, :] = self.faces['Green'][:, 2]

    def face_turn_anticlockwise(self, face: list):
        self.faces[face] = np.rot90(self.faces[face], -1)


    def print_face(self,face):
        curr_face = self.faces[face]
        print(f"{curr_face[0][0]} {curr_face[0][1]} {curr_face[0][2]}\n"
              f"{curr_face[1][0]} {curr_face[1][1]} {curr_face[1][2]}\n"
              f"{curr_face[2][0]} {curr_face[2][1]} {curr_face[2][2]}\n")

    def print_cube(self):
        for colour in self.faces:
            curr_face = self.faces[colour]
            print(f"{colour}:\n"
                  f"{curr_face[0][0]} {curr_face[0][1]} {curr_face[0][2]}\n"
                  f"{curr_face[1][0]} {curr_face[1][1]} {curr_face[1][2]}\n"
                  f"{curr_face[2][0]} {curr_face[2][1]} {curr_face[2][2]}\n")


my_cube = cube()
my_cube.face_turn_clockwise('White')
my_cube.print_cube()
