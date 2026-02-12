import reflex as rx
import os

class State(rx.State):
    is_maintenance: bool = False
    is_processing: bool = False
    audit_data: list[dict] = []

    def handle_upload(self, files: list[rx.UploadFile]):
        self.is_processing = True
        yield
        
        # Check if the AI model exists before running
        if os.path.exists("best.pt"):
            # Simulated detection logic using your 'best.pt' weights
            self.audit_data = [
                {"timestamp": "00:12", "brand": "Aramco", "confidence": "98%"},
                {"timestamp": "01:05", "brand": "Pirelli", "confidence": "92%"},
            ]
        else:
            self.audit_data = [{"timestamp": "Error", "brand": "Model Missing", "confidence": "0%"}]
            
        self.is_processing = False
