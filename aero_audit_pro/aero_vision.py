import reflex as rx
from .state import State 

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("AeroVision Dashboard", size="9", weight="bold"),
            rx.hstack(
                rx.text("AI-Powered F1 Brand Audit Beta", color_scheme="gray"),
                rx.badge(State.model_status, color_scheme="green"),
                spacing="3",
            ),
            
            rx.cond(
                State.is_maintenance,
                rx.vstack(
                    rx.text("🏎️ AI engine tuning in progress..."),
                    rx.badge("Maintenance Mode", color_scheme="orange"),
                ),
                rx.vstack(
                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell("Time"),
                                rx.table.column_header_cell("Brand"),
                                rx.table.column_header_cell("Confidence"),
                            ),
                        ),
                        rx.table.body(
                            rx.foreach(
                                State.audit_data,
                                lambda item: rx.table.row(
                                    rx.table.cell(item["timestamp"]),
                                    rx.table.cell(rx.badge(item["brand"], color_scheme="blue")),
                                    rx.table.cell(item["confidence"]),
                                ),
                            ),
                        ),
                        width="100%",
                        variant="surface",
                    ),
                    rx.upload(
                        rx.vstack(
                            rx.button("Select F1 Footage", icon="upload"),
                            rx.text("Drop video files here"),
                        ),
                        id="f1_upload",
                        border="1px dashed var(--gray-8)",
                        padding="3em",
                        width="100%",
                    ),
                    rx.button(
                        "Start Audit",
                        on_click=State.handle_upload(rx.upload_files(upload_id="f1_upload")),
                        loading=State.is_processing,
                        color_scheme="grass",
                        width="100%",
                    ),
                    width="100%",
                    spacing="6",
                ),
            ),
            spacing="8",
            padding="2em",
            max_width="800px",
        ),
        width="100%",
    )

app = rx.App(theme=rx.theme(appearance="dark", accent_color="blue"))
app.add_page(index, title="AeroVision | Dashboard")
