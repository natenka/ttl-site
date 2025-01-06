import json

from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.message import Message
from textual.reactive import reactive
from textual.widgets import Button, Footer, Header, Static
from textual import events

from rich import inspect

def load_topics(questions_file):
    with open(questions_file) as f:
        q_dict = json.load(f)
        return q_dict


class TopicText(Static):
    class Selected(Message):
        def __init__(self, topic: str) -> None:
            self.topic = topic
            super().__init__()

    def __init__(self, topic: str) -> None:
        self.topic = topic
        super().__init__()

    def on_click(self) -> None:
        self.post_message(self.Selected(self.topic))

    def render(self) -> str:
        return str(self.topic)


class TermQuiz(App):
    CSS_PATH = "quiz_style.tcss"
    TOPICS = load_topics("questions.json")

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Static("Виберіть тему та натисніть Enter", id="intro")
        topics_list = [TopicText(topic) for topic in self.TOPICS]
        yield from topics_list

    def on_topic_text_selected(self, message: TopicText.Selected) -> None:
        selected_topic = message.topic
        topics = self.query("TopicText")
        for top in topics:
            if top.topic != selected_topic:
                top.remove()
        for top in topics:
            top.styles.animate("background", "green", duration=0.1)


if __name__ == "__main__":
    app = TermQuiz()
    app.run()
