class Device(object):

    def __init__(self, id: int, type: str, subtype: str):
        self.id = id
        self.type = type
        self.subtype = subtype

    def serialize(self):
        to_serialize = {
            'id': self.id,
            'type': self.type,
            'subtype': self.subtype
        }
        return to_serialize
