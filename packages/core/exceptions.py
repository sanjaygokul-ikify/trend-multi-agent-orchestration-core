class OrchestrationError(Exception):
    pass

class InvalidEventError(OrchestrationError):
    pass

class StateInconsistencyError(OrchestrationError):
    pass
