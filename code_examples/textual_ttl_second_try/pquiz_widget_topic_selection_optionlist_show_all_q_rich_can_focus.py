from __future__ import annotations

from functools import partial
from typing import Any
import json

from textual._on import on
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container, Grid, Horizontal, VerticalScroll
from textual.widgets import Footer, Header, OptionList, Static, Pretty
from textual.widgets.option_list import Option
from textual.reactive import reactive, var
from textual.highlight import highlight
from textual.content import Content

from rich import box
from rich.padding import Padding
from rich.syntax import Syntax
from rich.style import Style
from rich.table import Table


def load_topics(questions_file):
    with open(questions_file) as f:
        q_dict = json.load(f)
        return q_dict


class TopicList(OptionList):
    def on_mount(self) -> None:
        TOPICS = load_topics("questions.json")
        self.add_options([Option(name, id=name) for name in TOPICS])


class ChangingThemeApp(App):
    CSS_PATH = "pynenguk_quiz_draft.tcss"

    BINDINGS = [
        Binding(
            "ctrl+d",
            "toggle_dark",
            "Toggle Dark",
            tooltip="Switch between light and dark themes",
        ),
    ]
    current_topic: reactive[str] = reactive("")
    topics = load_topics("questions.json")

    def action_toggle_dark(self) -> None:
        self.theme = "textual-light" if self.theme == "textual-dark" else "textual-dark"

    def watch_theme(self, theme_name: str) -> None:
        print(theme_name)

    def compose(self) -> ComposeResult:
        self.title = "Theme Sandbox"
        self.all_topics = load_topics("questions.json")

        yield Header(show_clock=True)
        yield TopicList(id="topic-list")
        with VerticalScroll(id="widget-list", can_focus=False) as container:
            yield Static(id="code", expand=True)
        yield Footer()

    def on_mount(self) -> None:
        self.theme = "textual-dark"

    @on(TopicList.OptionHighlighted, selector="#topic-list")
    def _change_topic(self, event: TopicList.OptionHighlighted) -> None:
        self.current_topic = event.option.id
        code_view = self.query_one("#code", Static)

        table = Table(
            "Огляд питань розділу\n(натисніть Enter, щоб відкрити питання обраного розділу)",
            box=box.SIMPLE,
            padding=(1, 1, 0, 1),
            header_style=Style(color="red", bold=True)
        )
        for question_dict in self.topics[self.current_topic]:
            table.add_row(question_dict["description"])
            table.add_row(Syntax(question_dict["code"], "python"))
            answers = "\n".join(question_dict["answers"].values())
            if question_dict.get("code_in_answer"):
                answers = Syntax(answers, "python")
            table.add_row(Padding(answers, (0, 5)))
            table.add_row()
        code_view.update(table)


app = ChangingThemeApp()
if __name__ == "__main__":
    app.run()
