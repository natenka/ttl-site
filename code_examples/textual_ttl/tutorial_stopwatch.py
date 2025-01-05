from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.widgets import Button, Digits, Footer, Header


class TimeDisplay(Digits):
    """A widget to display elapsed time"""


class Stopwatch(HorizontalGroup):
    """A stopwatch widget"""

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed"""


    def compose(self) -> ComposeResult:
        """Create child widgets of a stopwatch"""
        # self.styles.background = "blue"
        yield Button("Start", id="start", variant="success")
        yield Button("Stop", id="stop", variant="error")
        yield Button("Reset", id="reset")
        yield TimeDisplay("00:00:00.00")


class StopwatchApp(App):
    CSS_PATH = "stopwatch03.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets"""
        yield Header() # bar with a title
        yield Footer() # bar at the bottom with bound keys
        yield VerticalScroll(Stopwatch(), Stopwatch(), Stopwatch())

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode"""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    app = StopwatchApp()
    app.run()
