class MobilePhone:
    def __init__(self, name, imei, processor, memory):
        self.__name = name
        self.__imei = imei
        self.processor = processor
        self.feeding_habit = memory


        if self.processor in ['HiSilicon K3V3', 'MediaTek MT6592']:
            self.sim_slots = 2
        elif sef.processor in ['Broadcom BCM21664']:
            self.sim_slots =4
        elif self.name in ['Oneplus', 'Samsung', 'Nokia'] and self.processor == 'Snapdragon':
            self.sim_slots = 1


    def dial_connection(self, receiver):
        # Dialing logic
        # connect to recepient
        return receiver.__imei

    def is_dual_sim(self):
        if self.sim_slots > 1:
            return False
        else:
            return True

    def set_imei_number(self, imei):
        self.__imei = imei

    def show_imei_number(self):
        return self.imei

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def set_processor(self, processor):
        self.processor = processor

    def get_processor(self):
        return self.no_of_legs

    def send_message(self, recipient, message):
        self.message= message
        dial_connection(recipient)
        #logic to send after getting recipients imei

