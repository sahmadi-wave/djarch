from shared.orchestration import LayerComponent
from .clients import TestClient

class DomainClients:
    test_client: TestClient = TestClient()

domain_clients = DomainClients()

class BaseDomainService(LayerComponent):
    def __init__(self) -> None:
        self.clients = domain_clients
        super().__init__()
