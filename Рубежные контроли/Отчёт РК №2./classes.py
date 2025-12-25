class StoredProcedure:
    def __init__(self, id, name, db_id):
        self.id = id
        self.name = name
        self.db_id = db_id

class Database:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class StoredProcedureDatabase:
    def __init__(self, sp_id, db_id):
        self.sp_id = sp_id
        self.db_id = db_id