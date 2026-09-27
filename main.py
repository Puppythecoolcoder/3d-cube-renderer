#import pygame here
import pygame
pygame.init()

#import math
import math

#variables

ww = 1260
wh = 680

#defining object

class Cube:

    side = 0

    class Vertex:
        coords = [0, 0, 0]

        viewAngle = [0, 0, 0]

        def rotateX(self, ang):
            return [self.coords[0],
                    self.coords[1]*math.cos(ang)+self.coords[2]*math.sin(ang),
                    self.coords[1]*(-math.sin(ang))+self.coords[2]*math.cos(ang)] 

        def rotateY(self, ang):
            return [self.coords[0]*math.cos(ang)-self.coords[2]*math.sin(ang),
                    self.coords[1],
                    self.coords[0]*math.sin(ang)+self.coords[2]*math.cos(ang)]

        def rotateZ(self, ang):
            return [self.coords[0]*math.cos(ang)+self.coords[1]*math.sin(ang),
                    self.coords[0]*(-math.sin(ang))+self.coords[1]*math.cos(ang),
                    self.coords[2]]

        def project(self, FOV=300, camera_distance=300):
            x, y, z = self.coords
            z_cam = z + camera_distance
            if z_cam != 0:
                return [x*FOV/z_cam + ww/2, y*FOV/z_cam + wh/2]
            else:
                return [x + ww/2, y + wh/2]


    
    class Origin:
        coords = []


cube = Cube()

origin = Cube.Origin()



#down layer
a1 = Cube.Vertex()
a2 = Cube.Vertex()
a3 = Cube.Vertex()
a4 = Cube.Vertex()

#up layer
b1 = Cube.Vertex()
b2 = Cube.Vertex()
b3 = Cube.Vertex()
b4 = Cube.Vertex()

vertices = [a1, a2, a3, a4, b1, b2, b3, b4]

#function for rotating whole cube

def rotateCubeX(ang):
    for i in vertices:
        i.coords = i.rotateX(ang)

def rotateCubeY(ang):
    for i in vertices:
        i.coords = i.rotateY(ang)

def rotateCubeZ(ang):
    for i in vertices:
        i.coords = i.rotateZ(ang)



#coordinates of origin and vertices of the cube

origin.coords = [0, 0, 0]


cube.side = 50

#lower layer
a1.coords = [origin.coords[0]-cube.side/2, origin.coords[1]-cube.side/2, origin.coords[2]-cube.side/2]
a2.coords = [origin.coords[0]+cube.side/2, origin.coords[1]-cube.side/2, origin.coords[2]-cube.side/2]
a3.coords = [origin.coords[0]+cube.side/2, origin.coords[1]-cube.side/2, origin.coords[2]+cube.side/2]
a4.coords = [origin.coords[0]-cube.side/2, origin.coords[1]-cube.side/2, origin.coords[2]+cube.side/2]

#upper layer
b1.coords = [origin.coords[0]-cube.side/2, origin.coords[1]+cube.side/2, origin.coords[2]-cube.side/2]
b2.coords = [origin.coords[0]+cube.side/2, origin.coords[1]+cube.side/2, origin.coords[2]-cube.side/2]
b3.coords = [origin.coords[0]+cube.side/2, origin.coords[1]+cube.side/2, origin.coords[2]+cube.side/2]
b4.coords = [origin.coords[0]-cube.side/2, origin.coords[1]+cube.side/2, origin.coords[2]+cube.side/2]

cube.viewAngle =[0, 0, 0]



#creating window

window = pygame.display.set_mode((1280, 680))
clock = pygame.time.Clock()
running = True

while running:
    #check if window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    #refreshes the screen

    window.fill('black')

    #render cube

    rotateCubeZ(math.radians(1))
    rotateCubeY(math.radians(1))

    pygame.draw.line(window, (255, 255, 255), (a1.project()[0], a1.project()[1]), (a2.project()[0], a2.project()[1]))
    pygame.draw.line(window, (255, 255, 255), (a2.project()[0], a2.project()[1]), (a3.project()[0], a3.project()[1]))
    pygame.draw.line(window, (255, 255, 255), (a3.project()[0], a3.project()[1]), (a4.project()[0], a4.project()[1]))
    pygame.draw.line(window, (255, 255, 255), (a4.project()[0], a4.project()[1]), (a1.project()[0], a1.project()[1]))
    pygame.draw.line(window, (255, 255, 255), (b1.project()[0], b1.project()[1]), (b2.project()[0], b2.project()[1]))
    pygame.draw.line(window, (255, 255, 255), (b2.project()[0], b2.project()[1]), (b3.project()[0], b3.project()[1]))
    pygame.draw.line(window, (255, 255, 255), (b3.project()[0], b3.project()[1]), (b4.project()[0], b4.project()[1]))
    pygame.draw.line(window, (255, 255, 255), (b4.project()[0], b4.project()[1]), (b1.project()[0], b1.project()[1]))
    pygame.draw.line(window, (255, 255, 255), (a1.project()[0], a1.project()[1]), (b1.project()[0], b1.project()[1]))
    pygame.draw.line(window, (255, 255, 255), (a2.project()[0], a2.project()[1]), (b2.project()[0], b2.project()[1]))
    pygame.draw.line(window, (255, 255, 255), (a3.project()[0], a3.project()[1]), (b3.project()[0], b3.project()[1]))
    pygame.draw.line(window, (255, 255, 255), (a4.project()[0], a4.project()[1]), (b4.project()[0], b4.project()[1]))    
    

    #put the masterpiece on screen

    pygame.display.flip()



    clock.tick(60)

pygame.quit()




#x axis rotation
#[1, 0, 0]
#[0, cos x, -sin x ]
#[0, sin x, cos x]

#y axis rotation
#[cos x, 0, sin x]
#[0, 1, 0]
#[-sin x, 0, cos x]

#z axis rotation
#[cos x, -sin x, 0]
#[sin x, cos x, 0]
#[0, 0, 1]