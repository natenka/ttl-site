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

from rich.syntax import Syntax


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
        create_content = ""
        for question_dict in self.topics[self.current_topic]:
            create_content += f"\n{question_dict['description']}\n{question_dict['code']}\n\n\t"
            create_content += "\n\t".join(question_dict["answers"].values())
            create_content += "\n\n\n"
        # code_view.update(create_content)
        code_view.update(Syntax(create_content, "python"))


app = ChangingThemeApp()
if __name__ == "__main__":
    app.run()
