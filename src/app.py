"""Invoice routing for Northwind Harbor Logistics"""

class InvoiceRouter:
    """Internal service for invoice-router."""

    def status(self) -> str:
        return "ok"


if __name__ == "__main__":
    print(InvoiceRouter().status())
