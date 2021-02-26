from app.domain.device import *

devices = [Device(1, 'Mutlevel', 'Blinds'),
           Device(2, 'Thermostat', 'Default'),
           Device(3, 'Switch', 'Default')]


class DeviceRepo:
    def __init__(self, data: [Device] = None):
        if not data:
            self.devices = devices
        else:
            self.devices = data

    def all(self):
        return self.devices

    def get_by_id(self, id):
        for device in self.devices:
            if device.id == int(id):
                return device

    def update_device(self, device: Device):
        for dev in self.devices:
            if dev.id == device.id:
                index = self.devices.index(dev)
                self.devices[index] = device
                return device

    def create(self, device: Device):
        devices.append(device)
        return device
