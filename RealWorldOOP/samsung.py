
from RealWorldOOP import MobilePhone

class Samsung(MobilePhone):
    def CameraClick(self):
        return 'Normal Camera view'

    def CameraClick(self, CameraMode):
        # Polmorphism of cameraclick doing same operation with dofferent inputs
        return 'Paranormal camera view'

