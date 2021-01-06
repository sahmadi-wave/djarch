
from .orchestration import BaseDomainService

class TestService(BaseDomainService):
    def __init__(self)->None:
        self.test_data = 'testing testing testing'
        super().__init__()
    
    def regular_service_method(self) -> None:
        print(f'[{self.__class__.__name__}] Using shared service and client')
        self.shared_services.some_shared_service.greet(self.__class__.__name__)
        self.shared_clients.some_shared_client.greet(self.__class__.__name__)

        print(f'[{self.__class__.__name__}] Using domain client')
        self.clients.test_client.regular_client_method()

