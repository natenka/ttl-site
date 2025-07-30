# Previous versions
# with text pquiz_widget_topic_selection_optionlist_show_all_q.py
# without focus pquiz_widget_topic_selection_optionlist_show_all_q_rich.py

# Basic version
# without nice preview of questions
# pquiz_widget_topic_selection_optionlist.py

from __future__ import annotations

import json

from textual import on
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import VerticalScroll
from textual.widgets import Footer, Header, OptionList, Static, Pretty
from textual.widgets.option_list import Option
from textual.reactive import reactive, var

from rich import box
from rich.padding import Padding
from rich.syntax import Syntax
from rich.style import Style
from rich.table import Table


def load_topics(questions_file):
    with open(questions_file, encoding="utf-8") as f:
        q_dict = json.load(f)
        return q_dict


def create_questions_preview(questions_list: List[Dict[str, Any]]) -> Table:
    table = Table(
        "Огляд питань розділу\n(натисніть Enter, щоб відкрити питання обраного розділу)",
        box=box.SIMPLE,
        padding=(1, 1, 0, 1),
        header_style=Style(color="red", bold=True),
    )
    for question_dict in questions_list:
        table.add_row(question_dict.get("description"))
        code = question_dict.get("code")
        if code:
            table.add_row(Syntax(code, "python"))
        answers = "\n".join(question_dict.get("answers", {}).values())
        if question_dict.get("code_in_answer"):
            answers = Syntax(answers, "python")
        table.add_row(Padding(answers, (0, 5)))
        table.add_row()
    return table


class QuestionsPreview(Static, can_focus=True):
    pass


class QuizTopicSelectionApp(App):
    CSS_PATH = "pynenguk_quiz_draft_focus.tcss"

    current_topic: reactive[str] = reactive("")
    topics = load_topics("questions.json")

    def compose(self) -> ComposeResult:
        yield OptionList(
            *[Option(name, id=name) for name in self.topics], id="topic-list"
        )
        with VerticalScroll(id="widget-list", can_focus=False) as container:
            yield QuestionsPreview(id="questions", expand=True)
        yield Footer()

    @on(OptionList.OptionHighlighted, selector="#topic-list")
    def _change_topic(self, event: OptionList.OptionHighlighted) -> None:
        self.current_topic = event.option.id
        code_view = self.query_one("#questions", QuestionsPreview)

        table = create_questions_preview(self.topics[self.current_topic])
        code_view.update(table)


if __name__ == "__main__":
    app = QuizTopicSelectionApp()
    app.run()
