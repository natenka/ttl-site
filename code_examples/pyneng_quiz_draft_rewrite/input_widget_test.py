import json

from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.reactive import reactive
from textual.widgets import Button, Footer, Header, Input, Static
from textual import events


def load_topics(questions_file):
    with open(questions_file) as f:
        q_dict = json.load(f)
        return list(q_dict.keys())


topics = load_topics("questions.json")



class TermQuiz(App):
    CSS_PATH = "quiz_style.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Static("Введіть номер теми та натисніть Enter", id="intro")
        yield Input()
        topics_list = [
            f"{topic_id:<4} {text}"
            for topic_id, text in enumerate(topics, 1)
        ]
        yield Static("\n".join(topics_list), id="questions")



if __name__ == "__main__":
    app = TermQuiz()
    app.run()
