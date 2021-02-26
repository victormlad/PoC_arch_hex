from app.domain.devicerepo import DeviceRepo, Device

repo = DeviceRepo()


def get_all():
    devices = repo.all()
    return devices


def get_by_id(id):
    dev = repo.get_by_id(id)
    return dev


def update_device(device: Device):
    dev = repo.update_device(device)
    return dev


def create(id, type, subtype):
    new_device = Device(id, type, subtype)
    return repo.create(new_device)
