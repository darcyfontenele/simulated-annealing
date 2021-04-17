class TSI:
    name = None
    type = None
    comment = None
    dimension = None
    ewt = None
    ewf = None
    ldr = None
    ews = None
    matrix = None

    def __init__(self, name, type, comment, dimension, ewt, ewf, ldr, ews, matrix):
        self.name = name
        self.type = type
        self.comment = comment
        self.dimension = dimension
        self.ewt = ewt
        self.ewf = ewf
        self.ldr = ldr
        self.ews = ews
        self.matrix = matrix