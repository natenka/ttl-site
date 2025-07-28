from __future__ import annotations

from functools import partial
from typing import Any
import json

from textual._on import on
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container, Grid, Horizontal, VerticalScroll
from textual.widgets import (
    Button,
    Collapsible,
    DataTable,
    Footer,
    Header,
    Input,
    Label,
    ListItem,
    ListView,
    MarkdownViewer,
    OptionList,
    ProgressBar,
    RadioSet,
    RichLog,
    Select,
    SelectionList,
    Switch,
    TabbedContent,
    TextArea,
    Tree,
)
from textual.widgets._masked_input import MaskedInput
from textual.widgets._toggle_button import ToggleButton
from textual.widgets.option_list import Option
from textual.widgets.text_area import Selection


LOREM_IPSUM = """\
 Sed euismod, nunc sit amet aliquam lacinia, nisl nisl aliquam nisl, nec aliquam nisl nisl sit amet lorem.
"""

EXAMPLE_MARKDOWN = """\
- Tables!
"""

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


class ColorSample(Label):
    pass


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
        Binding(
            "ctrl+a",
            "toggle_panel",
            "Toggle panel",
            tooltip="Add or remove the panel class from the widget gallery",
        ),
        Binding(
            "ctrl+b",
            "toggle_border",
            "Toggle border",
            tooltip="Add or remove the borders from widgets",
        ),
    ]

    def action_toggle_dark(self) -> None:
        self.theme = "textual-light" if self.theme == "textual-dark" else "textual-dark"

    def watch_theme(self, theme_name: str) -> None:
        print(theme_name)

    def compose(self) -> ComposeResult:
        self.title = "Theme Sandbox"
        self.all_topics = load_topics("questions.json")
        self.current_topic = ""
        self.current_topic_questions = None

        yield Header(show_clock=True)
        yield TopicList(id="topic-list")
        with VerticalScroll(id="widget-list", can_focus=False) as container:
            yield TextArea(self.current_topic)
            yield ListView(
                ListItem(Label(self.current_topic)),
                ListItem(Label("Two")),
                ListItem(Label("Three")),
            )
        yield Footer()

    def on_mount(self) -> None:
        self.theme = "textual-light"

    @on(TopicList.OptionHighlighted, selector="#topic-list")
    def _change_theme(self, event: TopicList.OptionHighlighted) -> None:
        self.current_topic = event.option.id
        # self.query_one(ListView).


app = ChangingThemeApp()
if __name__ == "__main__":
    app.run()
