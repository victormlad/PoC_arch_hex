from app.device_use_cases import device


class Api:
    def __init__(self):
        pass

    def get_all_devices(self):
        devices = device.get_all()
        return [dev.serialize() for dev in devices]

    def get_device(self, id):
        dev = device.get_by_id(id)
        return dev.serialize()

    def create_device(self, id, type, subtype):
        new_device = device.create(id, type, subtype)
        return new_device.serialize()

    def device_update(self, device_id, changes):
        dev = device.get_by_id(device_id)


api = None


# def start():
#     global api
#
#     api = Api()
#     return api
#
#
# def get_api():
#     return api
