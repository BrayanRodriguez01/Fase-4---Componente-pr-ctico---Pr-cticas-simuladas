# Excepciones personalizadas del sistema

class ClienteInvalidoError(Exception):
    pass


class ServicioNoDisponibleError(Exception):
    pass


class ReservaInvalidaError(Exception):
    pass
