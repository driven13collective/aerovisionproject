import reflex as rx

class State(rx.State):
    is_maintenance: bool = False
    is_processing: bool = False
    audit_data: list[dict] = []

    def handle_upload(self, files: list[rx.UploadFile]):
        self.is_processing = True
        yield
        # Simulated F1 audit data for driven13collective beta
        self.audit_data = [
            {"timestamp": "00:12", "brand": "Aramco", "confidence": "98%"},
            {"timestamp": "01:05", "brand": "Pirelli", "confidence": "92%"},
            {"timestamp": "02:30", "brand": "Oracle", "confidence": "95%"},
        ]
        self.is_processing = False
