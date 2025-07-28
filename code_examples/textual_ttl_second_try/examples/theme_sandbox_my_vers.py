from __future__ import annotations

from functools import partial
from typing import Any
import json

from textual._on import on
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container, Grid, Horizontal, VerticalScroll
from textual.widgets import (
    Footer,
    Header,
    Label,
    ListItem,
    ListView,
    OptionList,
    Select,
    SelectionList,
    Switch,
    TabbedContent,
    TextArea,
    Tree,
    Static
)
from textual.widgets._masked_input import MaskedInput
from textual.widgets._toggle_button import ToggleButton
from textual.widgets.option_list import Option
from textual.widgets.text_area import Selection
from textual.reactive import reactive, var


def load_topics(questions_file):
    with open(questions_file) as f:
        q_dict = json.load(f)
        return q_dict


class TopicList(OptionList):
    def on_mount(self) -> None:
        TOPICS = load_topics("questions.json")
        self.add_options(
            [Option(name, id=name) for name in TOPICS]
        )


class ChangingThemeApp(App[None]):
    CSS = """
    TopicList {
        height: 1fr;
        width: 30%;
        dock: left;
        margin-bottom: 1;
    }
    TextArea {
        height: 8;
        scrollbar-gutter: stable;
    }

    ListView {
        height: auto;

    }
    #label-variants {
        & > Label {
            padding: 0 1;
            margin-right: 1;
        }
    }

    #widget-list {
        & > OptionList {
            height: 6;
        }
        & > RadioSet {
            height: 6;
        }
    }
    #widget-list {
    }
    #widget-list > * {
        margin: 1 2;
    }
    """

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
        self.theme = "textual-light"

    @on(TopicList.OptionHighlighted, selector="#topic-list")
    def _change_theme(self, event: TopicList.OptionHighlighted) -> None:
        self.current_topic = event.option.id
        # self.app.theme = "textual-dark"
        code_view = self.query_one("#code", Static)
        # code_view.update(self.topics[self.current_topic])
        code_view.update(str(self.topics[self.current_topic]))


app = ChangingThemeApp()
if __name__ == "__main__":
    app.run()
