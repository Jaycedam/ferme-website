id = 0

def set_current_id(new_id):
    global id 
    id = new_id

def get_current_id():
    global id
    print("Se ha retornado el id de: " + str(id))
    return id
