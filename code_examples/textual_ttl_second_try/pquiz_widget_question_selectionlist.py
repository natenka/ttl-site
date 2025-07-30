# To enable syntax highlighting, you'll need to install the syntax
# extra dependencies:
# pip install textual[syntax]
from __future__ import annotations

from functools import partial
from typing import Any

from textual import on
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import VerticalScroll
from textual.widgets import (
    Footer,
    Header,
    TextArea,
    Label,
    SelectionList,
    Pretty,
    Rule,
)
from textual.reactive import reactive, var
from textual.events import Mount

# Test data
question_dict = {
    "description": "Яке значення буде у змінної result в останньому рядку?",
    "code": (
        "data = {'hostname': 'london_r1', 'ip': '10.255.0.1', 'vendor': 'Cisco'}\n"
        "keys = data.keys()\ndel data['ip']\nprint(keys)"
    ),
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


class Question(VerticalScroll):
    def compose(self) -> ComposeResult:
        yield Label("Питання 1 з 30")
        yield Label(question_dict["description"])
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

    def on_mount(self) -> None:
        # При відображенні запитання, фокус одразу на блоці відповідей
        self.query_one(SelectionList).focus()

    @on(SelectionList.SelectedChanged)
    def update_selected_view(self) -> None:
        # виводить список вибраних варіантів відповіді
        self.query_one(Pretty).update(self.query_one(SelectionList).selected)


class QuizQuestionsApp(App):
    CSS_PATH = "pynenguk_quiz_draft_selectionlist.tcss"
    BINDINGS = [
        Binding("enter", "check_answers", "Check answers", priority=True),
    ]

    def compose(self) -> ComposeResult:
        yield Question(id="question-widget", can_focus=False)
        yield Footer()

    def action_check_answers(self) -> None:
        # Робимо вигляд, що робиться щось корисне після Enter
        # тут має бути перевірка чи правильні відповіді
        self.mount(Rule(line_style="heavy"))
        self.call_after_refresh(self.screen.scroll_end, animate=False)


if __name__ == "__main__":
    app = QuizQuestionsApp()
    app.run()
