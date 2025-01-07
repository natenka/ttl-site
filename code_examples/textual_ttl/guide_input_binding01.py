from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.color import Color
from textual.widgets import Footer, Static


class Bar(Static):
    pass


class BindingApp(App):
    CSS_PATH = "binding01.tcss"
    BINDINGS = [
        ("r", "add_bar('red')", "Add Red"),
        ("g", "add_bar('green')", "Add Green"),
		# textual.textualize.io/api/binding/#textual.binding.Binding
		# dataclass
        Binding("b", "add_bar('blue')", "Add Blue"),
		# priority means bindings will be checked prior to the
		# bindings of the focused widget
		Binding("ctrl+q", "quit", "Quit", show=False, priority=True),
    ]

    def compose(self) -> ComposeResult:
        yield Footer()

    def action_add_bar(self, color: str) -> None:
        bar = Bar(color)
        bar.styles.background = Color.parse(color).with_alpha(0.5)
        self.mount(bar)
		# move with added widgets to the end of scroll
        self.call_after_refresh(self.screen.scroll_end, animate=False)


if __name__ == "__main__":
    app = BindingApp()
    app.run()
