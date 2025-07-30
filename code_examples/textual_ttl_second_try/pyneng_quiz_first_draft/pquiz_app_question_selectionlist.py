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
    Static,
    TextArea,
    Input,
    Label,
    SelectionList,
    Pretty,
    Rule,
)
from textual.reactive import reactive, var
from textual.highlight import highlight
from textual.events import Mount


def load_topics(questions_file):
    with open(questions_file, encoding="utf-8") as f:
        q_dict = json.load(f)
        return q_dict


class ChangingThemeApp(App):
    CSS_PATH = "pynenguk_quiz_draft_selectionlist.tcss"
    # Individual bindings may be marked as a priority, which means they will be
    # checked prior to the bindings of the focused widget
    BINDINGS = [
        Binding("enter", "check_answers", "Check answers", priority=True),
    ]
    # enter binding made inside checkbox
    # https://textual.textualize.io/widgets/checkbox/

    def compose(self) -> ComposeResult:
        self.title = "Theme Sandbox"
        question_dict = {
            "description": "Яке значення буде у змінної result в останньому рядку?",
            "code": "data = {'hostname': 'london_r1', 'ip': '10.255.0.1', 'vendor': 'Cisco'}\nkeys = data.keys()\ndel data['ip']\nprint(keys)",
            "answers": {
                "1": "'t'",
                "2": "'inte'",
                "3": "'int'",
                "4": "'e'",
                "5": "'r'",
                "6": "Помилка",
                "7": "result = data.setdefault(200)",
                "8": "result = data.get(200)",
                "9": "result = data[200]",
            },
            "correct_answer": "4",
            "multiple_choices": False,
        }

        yield Header(show_clock=True)

        with VerticalScroll(id="widget-list", can_focus=False) as container:
            yield Label("Питання 1 з 30")
            yield Label(question_dict["description"])
            # To enable syntax highlighting, you'll need to install the syntax
            # extra dependencies:
            # pip install textual[syntax]
            # ДОДАТИ перевірку на те чи є код в питанні
            yield TextArea.code_editor(
                question_dict["code"],
                language="python",
                read_only=True,
                show_cursor=False,
                compact=True,
            )
            yield Label("Виберіть правильні відповіді за допомогою миші або пробілом")
            reverse_key_value = {v: k for k, v in question_dict["answers"].items()}
            yield SelectionList(*reverse_key_value.items())
            yield Pretty([])
        yield Footer()

    def action_check_answers(self) -> None:
        # Роюимо вигляд, що робиться щось корисне після Enter
        # тут має бути перевірка чи правильні відповіді
        self.mount(Rule(line_style="heavy"))
        self.call_after_refresh(self.screen.scroll_end, animate=False)

    def on_mount(self) -> None:
        self.query_one(SelectionList).focus()

    @on(Mount)
    @on(SelectionList.SelectedChanged)
    def update_selected_view(self) -> None:
        # виводить список вибраних варіантів відповіді
        self.query_one(Pretty).update(self.query_one(SelectionList).selected)


app = ChangingThemeApp()
if __name__ == "__main__":
    app.run()
