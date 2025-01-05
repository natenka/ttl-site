import json

from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.reactive import reactive
from textual.widgets import Button, Footer, Header, Static


def load_topics(questions_file):
    with open(questions_file) as f:
        q_dict = json.load(f)
        return list(q_dict.keys())


topics = load_topics("questions.json")


class TopicText(Button):
    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        self.select()

    def select(self) -> None:
        self.add_class("selected")


class Topics(VerticalScroll):
    pass


class TermQuiz(App):
    CSS_PATH = "quiz_style.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        topics_list = [
            TopicText(f"{topic_id:<4} {text}", id=f"topic_{topic_id}")
            for topic_id, text in enumerate(topics, 1)
        ]
        yield Topics(*topics_list, id="topics")


if __name__ == "__main__":
    app = TermQuiz()
    app.run()
