from __future__ import annotations

from functools import partial
from typing import Any
import json

from textual._on import on
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container, Grid, Horizontal, VerticalScroll
from textual.widgets import Footer, Header, Tree, Static
from textual.widgets._masked_input import MaskedInput
from textual.widgets._toggle_button import ToggleButton
from textual.widgets.option_list import Option
from textual.reactive import reactive, var


def load_topics(questions_file):
    with open(questions_file) as f:
        q_dict = json.load(f)
        return q_dict


class TopicTree(Tree):
    def on_mount(self) -> None:
        TOPICS = load_topics("questions_tree.json")
        self.root.expand()
        for topic_name, subtopic in TOPICS.items():
            topic = self.root.add(topic_name, expand=True)
            for subname in subtopic:
                topic.add_leaf(subname)


class ChangingThemeApp(App):
    CSS_PATH = "pynenguk_quiz_draft_tree.tcss"

    BINDINGS = [
        Binding(
            "ctrl+d",
            "toggle_dark",
            "Toggle Dark",
            tooltip="Switch between light and dark themes",
        ),
    ]
    current_topic: reactive[str] = reactive("")
    topics = load_topics("questions_tree.json")

    def action_toggle_dark(self) -> None:
        self.theme = "textual-light" if self.theme == "textual-dark" else "textual-dark"

    def watch_theme(self, theme_name: str) -> None:
        print(theme_name)

    def compose(self) -> ComposeResult:
        self.title = "Theme Sandbox"
        self.all_topics = load_topics("questions.json")

        yield Header(show_clock=True)
        yield TopicTree("Доступні теми", id="topic-list")
        with VerticalScroll(id="widget-list", can_focus=False) as container:
            yield Static(id="code", expand=True)
        yield Footer()

    def on_mount(self) -> None:
        self.theme = "textual-dark"

    @on(TopicTree.NodeHighlighted, selector="#topic-list")
    def _change_topic(self, event: TopicTree.NodeHighlighted) -> None:
        self.current_topic = event.node.id
        code_view = self.query_one("#code", Static)
        # code_view.update(self.topics[self.current_topic])
        # code_view.update(str(self.topics[self.current_topic]))
        code_view.update(f"Long text {event.node} {event.control}")


app = ChangingThemeApp()
if __name__ == "__main__":
    app.run()
