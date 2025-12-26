from pydantic import BaseModel


class InvoiceBase(BaseModel):
    Cuit: int
    PtoVta: int
    CbteTipo: int


class InvoiceQueryRequest(InvoiceBase):
    CbteNro: int

class LastAuthorizedInvoiceRequest(InvoiceBase):
    pass
