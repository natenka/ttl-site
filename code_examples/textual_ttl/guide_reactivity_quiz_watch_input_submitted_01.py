import json
import re

from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.message import Message
from textual.reactive import reactive
from textual.widgets import Button, Footer, Header, Input, Static
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
    CSS_PATH = "quiz_style_02.tcss"
    TOPICS = load_topics("questions.json")

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Input(placeholder="Виберіть тему", id="intro")
        topics_list = [TopicText(topic) for topic in self.TOPICS]
        yield VerticalScroll(*topics_list, id="topics")

    def remount_topics(self, topics):
        self.query_one("#topics").remove()

        topics_list = [TopicText(topic) for topic in topics]
        # self.mount(VerticalScroll(*topics_list, id="topics"))
        self.mount(VerticalScroll(*topics_list))

    def highlight_selected_topic(self, selected_topic: str):
        # self.query_one("#topics").remove()
        # new_topic = TopicText(selected_topic)
        # self.mount(new_topic)

        self.remount_topics([selected_topic])
        # new_topic.styles.animate("background", "green", duration=0.1)

    def on_topic_text_selected(self, message: TopicText.Selected) -> None:
        self.highlight_selected_topic(message.topic)

    def on_input_submitted(self, event: Input.Submitted) -> None:
        search_topic = event.value
        matched_topics = ""
        # self.query_one(Input).value = ""


if __name__ == "__main__":
    app = TermQuiz()
    app.run()
