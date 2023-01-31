import pygame
pygame.init()


screen_width = 1500
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


class Vertex:
    static_id=0
    def __init__(self, x, y, incident_edge=None):
        self.x = x
        self.y = y
        self.incident_edge = incident_edge
        self.id=self.static_id
        self.static_id+=1

class Edge:
    static_id=0
    def __init__(self, origin, twin, next_edge, prev_edge, incident_face):
        self.origin = origin
        self.twin = twin
        self.next_edge = next_edge
        self.prev_edge = prev_edge
        self.incident_face = incident_face
        self.id=self.static_id
        self.static_id+=1

class Face:
    static_id=0
    def __init__(self, edge_start):
        self.edge_start=edge_start
        self.id=self.static_id
        self.static_id+=1

class DCEL:
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.faces = []

    def add_vertex(self, x, y):
        new_vertex = Vertex(x, y)
        self.vertices.append(new_vertex)
        return new_vertex

    def add_edge(self, origin, twin = None, next_edge = None, prev_edge = None, incident_face=None):
        new_edge = Edge(origin, twin, next_edge, prev_edge, incident_face)
        self.edges.append(new_edge)
        origin.incident_edge = new_edge
        return new_edge

    def add_face(self, edge_start):
        new_face = Face(edge_start)
        self.faces.append(new_face)
        return new_face


def drawgrid(width, rows, surface):
    sizebtwn = width // rows 
    print(sizebtwn)

    for i in range(0, width, sizebtwn):
        x, y = i, i
        color = (211, 211, 211) # (255, 255, 255)
        pygame.draw.line(surface, color, (x, 0), (x, width))
        pygame.draw.line(surface, color, (0, y), (width, y))


class Current:
    def __init__(self, start_vertex = None, end_vertex = None):
        self.start = start_vertex
        self.end = end_vertex
        self.last_edge = None
        self.face_first_vertex = None
        self.face = None
        self.face_edges = []
        self.face_vertices = []


current = Current()
dcel = DCEL()

class View:
    def update(self, sizebtwn, surface):
        x, y = pygame.mouse.get_pos()

        print("x:", x, " y:", y)
        
        ix = x // sizebtwn
        iy = y // sizebtwn

        mouseX = ix * sizebtwn
        mouseY = iy * sizebtwn

        #self.cx, self.cy = ix * sizebtwn, iy * sizebtwn

        mouseX = x
        mouseY = y

        offsetX = x % sizebtwn
        offsetY = y % sizebtwn

        if (offsetX > (sizebtwn/2)):
            if(offsetY > (sizebtwn/2)): # bottom right corner
                mouseX += sizebtwn - offsetX
                mouseY += sizebtwn - offsetY

            elif (offsetY < (sizebtwn/2)): # top right corner
                mouseX += sizebtwn - offsetX
                mouseY -= offsetY

        elif (offsetX < (sizebtwn/2)):
            if(offsetY < (sizebtwn/2)): # top left corner
                mouseX -= offsetX
                mouseY -= offsetY

            elif (offsetY > (sizebtwn/2)): # bottom right corner
                mouseX -= offsetX
                mouseY += sizebtwn - offsetY

        print(mouseX, ' ', mouseY)

        self.cx, self.cy = mouseX, mouseY
        self.circle = pygame.Rect(self.cx, self.cy, sizebtwn, sizebtwn)
        
    def draw_edge(self, surface):
        if len(current.face_vertices) == 0:
            current.start_vertex = dcel.add_vertex(self.cx, self.cy)
            current.face_vertices.append(current.start_vertex)
            current.face_first_vertex = Vertex(self.cx, self.cy)
        else:
            current.end_vertex = dcel.add_vertex(self.cx, self.cy)
            if current.end_vertex.x == current.face_first_vertex.x and current.end_vertex.y == current.face_first_vertex.y:
                face = dcel.add_face(current.face_edges[0])
                for edge in current.face_edges:
                    edge.incident_face = face
                current.face_edges.clear()
                current.face_vertices.clear()
                
            pygame.draw.line(surface, (255, 0, 0), (current.start_vertex.x, current.start_vertex.y), (current.end_vertex.x, current.end_vertex.y))
            #origin, twin, next_edge, prev_edge, incident_face=None
            edge = dcel.add_edge(origin=current.start_vertex, prev_edge=current.last_edge)
            edge.twin = dcel.add_edge(origin=current.end_vertex, twin=edge)

            if current.last_edge is not None:
                edge.twin.next_edge = current.last_edge.twin
                current.last_edge.next_edge = edge

            current.face_edges.append(edge)
            #current.last_edge.next_edge = edge
            current.last_edge = edge
            current.start_vertex = Vertex(current.end_vertex.x, current.end_vertex.y)
            current.end_vertex = None
        
        

    def draw_vertex(self, surface):
        color = (0, 0, 0) # (255, 255, 255)
        vertex_radius = 3
        pygame.draw.circle(surface, color, (self.cx, self.cy), vertex_radius)
        self.draw_edge(surface)
        

view = View()
run = True

screen.fill((255, 255, 255)) # 0
print(screen.get_width())

num_of_cols = 100
drawgrid(screen.get_width(), num_of_cols, screen)
#pygame.display.flip()


while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            view.update(screen.get_width() // num_of_cols, screen)
            
            view.draw_vertex(screen)

    pygame.display.flip()