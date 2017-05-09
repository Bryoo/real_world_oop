
from RealWorldOOP import MobilePhone


class Samsung(MobilePhone):     # samsung would inherit all properties and methods of MobilePhone hence inheritance
    def camera_click(self):
        return 'Normal Camera view'

    def camera_click(self, CameraMode):
        # Polmorphism of cameraclick doing same operation with different inputs
        return 'Paranormal camera view'


