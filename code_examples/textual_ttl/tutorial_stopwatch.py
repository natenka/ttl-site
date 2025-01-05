from textual.app import App, ComposeResult
from textual.widgets import Footer, Header


class StopwatchApp(App):
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets"""
        yield Header() # bar with a title
        yield Footer() # bar at the bottom with bound keys

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode"""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    app = StopwatchApp()
    app.run()
