
# This is an example of a Client within a regular (non-shared) Domain.
# 
# The base class BaseClient is imported from the shared Domain where
# access is provided to all shared clients.

from shared.orchestration import LayerComponent

class TestClient(LayerComponent):
    def __init__(self)->None:
        super().__init__()

    def regular_client_method(self)->None:
        print(f'[{self.__class__.__name__}] Calling shared client method from client')
        self.shared_clients.some_shared_client.greet(self.__class__.__name__)
    