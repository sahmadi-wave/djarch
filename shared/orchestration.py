from shared import clients, services

class SharedServices:
    """ registry of shared services """
    some_shared_service: services.SomeSharedService = services.SomeSharedService()

shared_services = SharedServices()

class SharedClients:
    """ registry of shared clients """
    some_shared_client: clients.SomeSharedClient = clients.SomeSharedClient()

shared_clients = SharedClients()

class LayerComponent:
    """
    This is the base class that regular Domain components will use.
    
    By subclassing LayerComponent, shared Clients and Services are provided
    without the need for manual imports while ensuring that the component 
    abides by our layer communication rules (i.e. only "shared" components are made available)
    """
    def __init__(self) -> None:
        self.shared_clients = shared_clients
        self.shared_services = shared_services
