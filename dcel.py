# class Vertex:
#     static_id=0
#     def __init__(self, x, y, incident_edge=None):
#         self.x = x
#         self.y = y
#         self.incident_edge = incident_edge
#         self.id=self.static_id
#         self.static_id+=1

# class Edge:
#     static_id=0
#     def __init__(self, origin, twin, next_edge, prev_edge, incident_face):
#         self.origin = origin
#         self.twin = twin
#         self.next_edge = next_edge
#         self.prev_edge = prev_edge
#         self.incident_face = incident_face
#         self.id=self.static_id
#         self.static_id+=1

# class Face:
#     static_id=0
#     def __init__(self, edge_start):
#         self.edge_start=edge_start
#         self.id=self.static_id
#         self.static_id+=1

# class DCEL:
#     def __init__(self):
#         self.vertices = []
#         self.edges = []
#         self.faces = []

#     def add_vertex(self, x, y):
#         new_vertex = Vertex(x, y)
#         self.vertices.append(new_vertex)
#         return new_vertex

#     def add_edge(self, origin, twin, next_edge, prev_edge, incident_face=None):
#         new_edge = Edge(origin, twin, next_edge, prev_edge, incident_face)
#         self.edges.append(new_edge)
#         origin.incident_edge = new_edge
#         return new_edge

#     def add_face(self, edge_start):
#         new_face = Face(edge_start)
#         self.faces.append(new_face)
#         return new_face


# import turtle

# wn = turtle.Screen()

# t = turtle.Turtle()

# # t.forward(25)
# # print(t.xcor(), ',', t.ycor())


# dcel = DCEL()




# def fxn(x, y):
#     global first_vertex, prev_edge
#     if len(dcel.vertices) == 0:
#         t.penup()
#         # Create a new Vertex object and add it to the dcel's vertices list
#         first_vertex = dcel.add_vertex(x, y)
#         t.goto(x, y)
#         t.write(str(x)+","+str(y))
#         t.pendown()
#     else:
#         # Create a new Vertex object and add it to the dcel's vertices list
#         second_vertex = dcel.add_vertex(x, y)
#         t.dot()
#         t.goto(x, y)
#         t.write(str(x)+","+str(y))
#         # Create a new Edge object and add it to the dcel's edges list
#         new_edge = dcel.add_edge(first_vertex, None, None, prev_edge)
        
#         # Create a twin edge object and add it to the dcel's edges list
#         twin_edge = dcel.add_edge(second_vertex, None, None, new_edge)
#         new_edge.twin = twin_edge
        
#         # Assign next and previous edges
#         if prev_edge:
#             prev_edge.next_edge = new_edge
#             new_edge.prev_edge = prev_edge
#         prev_edge = twin_edge
        
#         # Create a new Face object and add it to the dcel's faces list
#         new_face = dcel.add_face(new_edge)
#         first_vertex = second_vertex


# # onclick action 
# wn.onclick(fxn)
# wn.mainloop()
