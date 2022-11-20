import json

#a)

class point: #defining the class
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def getX(self): 
        return self.x
    
    def getY(self):
        return self.y

def get_json_str(p):
    a = {"__class__":"Point", "x": p.getX(),"y": p.getY()} #turns the class inputted the class into a dictionary
    return json.dumps(a, indent =1 ) #turns the dictionary into a JSON string

P = point(1,2)
z = get_json_str(P)

print(z)

#b)

def read_json_str(s):
    b = json.loads(s) #turns the JSON string back into the Python dictionary
    Xpoint = b["x"]
    Ypoint = b["y"] #variables Xpoint and Ypoint has the"x" and "y" values from the dictionary as its values
    print(f"({Xpoint},{Ypoint})") 

read_json_str(z)




