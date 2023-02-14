class ContractException(Exception):
    pass

class InvalidAgeOldException(ContractException):
    pass

class InvalidAgeYoungException(ContractException):
    pass

class InvalidAgeException(ContractException):
    pass

class InvalidDurationException(ContractException):
    pass

class InvalidSalaryException(ContractException):
    pass
