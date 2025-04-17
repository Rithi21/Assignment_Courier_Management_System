from abc import ABC, abstractmethod

class ICourierUserService(ABC):
    
    @abstractmethod
    def placeOrder(self, courierObj):
        pass

    @abstractmethod
    def getOrderStatus(self, trackingNumber):
        pass

    @abstractmethod
    def cancelOrder(self, trackingNumber):
       pass

    @abstractmethod
    def getAssignedOrder(self, courierStaffId):
        pass
