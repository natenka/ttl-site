from __future__ import annotations

from functools import partial
from typing import Any
import json

from textual._on import on
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container, Grid, Horizontal, VerticalScroll
from textual.widgets import Footer, Header, Static, DataTable
from textual.widgets.option_list import Option
from textual.reactive import reactive, var
from textual.highlight import highlight


def load_topics(questions_file):
    with open(questions_file) as f:
        q_dict = json.load(f)
        return q_dict


class ChangingThemeApp(App):
    CSS_PATH = "pynenguk_quiz_draft.tcss"

    def compose(self) -> ComposeResult:
        self.title = "Theme Sandbox"

        yield Header(show_clock=True)
        with VerticalScroll(id="widget-list", can_focus=False) as container:
            yield DataTable()
        yield Footer()

    def on_mount(self) -> None:
        self.theme = "textual-dark"
        question_dict = {
            "description": "Яке значення буде у змінної result в останньому рядку?",
            "code": "string = 'interface'\nresult = string[3]",
            "answers": {
                "1": "'t'",
                "2": "'inte'",
                "3": "'int'",
                "4": "'e'",
                "5": "'r'",
                "6": "Помилка",
            },
            "correct_answer": "4",
            "multiple_choices": False,
        }

        table = self.query_one(DataTable)
        table.add_columns(f"Питання 1 з 30\n{question_dict['description']}\n")
        table.add_row(question_dict['description'])
        table.add_row(question_dict["code"])
        table.add_row(question_dict["answers"])
        table.add_row("Enter number: ")


app = ChangingThemeApp()
if __name__ == "__main__":
    app.run()
