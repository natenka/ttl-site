import json

from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.message import Message
from textual.widgets import Button, Footer, Header, Static
from textual import events


def load_topics(questions_file):
    with open(questions_file) as f:
        q_dict = json.load(f)
        return q_dict


class TopicText(Button):
    class Selected(Message):
        def __init__(self, topic: str) -> None:
            self.topic = topic
            super().__init__()

    def __init__(self, topic: str) -> None:
        self.topic = topic
        super().__init__()

    def on_button_pressed(self) -> None:
        self.post_message(self.Selected(self.topic))

    def render(self) -> str:
        chapter, *topic_words = self.topic.split(" ")
        return f"Розділ: {chapter:4} {' '.join(topic_words)}"


class TermQuiz(App):
    CSS_PATH = "quiz_style.tcss"
    TOPICS = load_topics("questions.json")

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Static("Виберіть тему та натисніть Enter", id="intro")
        topics_list = [TopicText(topic) for topic in self.TOPICS]
        yield VerticalScroll(*topics_list, id="topics")

    def on_topic_text_selected(self, message: TopicText.Selected) -> None:
        selected_topic = message.topic
        topics = self.query_one("#topics").remove()

        new_topic = TopicText(selected_topic)
        header = self.query_one("#intro")
        header.mount(new_topic)
        new_topic.styles.animate("background", "darkgreen", duration=0.1)


if __name__ == "__main__":
    app = TermQuiz()
    app.run()
