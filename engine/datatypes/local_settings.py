
    
class StationData:
    Process = str()
    Site = str()
    StationName = str()
    FocusFactory = str()
    ProductType = str()
    Language = str()

class Sequence:
    File = str()
    
class ConnectionString:
    Server = str()

class StationSettings:
    StationData = StationData()
    Sequence = Sequence()
    ConnectionString = ConnectionString() 
    
class InstrumentSettings:
    pass

class TestSettings:
    pass