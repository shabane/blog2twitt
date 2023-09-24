"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
import reflex as rx


docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    blog: str = ''
    posts = []

    @rx.var
    def blog_count(self):
        return len(self.blog)

    def convert(self):
        self.posts = []
        post_count = len(self.blog)//280
        posts_count = len(self.posts)/280
        tch = 272 # mines template chars [xx/yy]
        start_on = 0
        i = 1

        if post_count <= 1:
            self.posts.append(f'[{i}/{post_count+1}] {self.blog[start_on:]}')
            return
        else:
            for i in range(1, post_count+1):
                self.posts.append(f'[{i}/{post_count+1}] {self.blog[start_on:i*tch]}')
                start_on = i*tch
        self.posts.append(f'[{i+1}/{post_count+1}] {self.blog[start_on:]}')



def colored_box(txt: str) -> rx.component:
    return rx.box(
        rx.text(txt),
        border='solid 1px #1ABC9C',
        padding='1%',
        font_size='2em',
        _hover={
                'color': '#85929E',
            },
        margin_top='1%',
        width='100%',
        )

def index() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.text_area(
                placeholder='write your blog here...',
                height='300px',
                font_size='2em',
                on_change=State.set_blog,
                ),
            rx.button(
                'Convert',
                margin_top='1%',
                bg_color='#3498DB',
                color='#FFF',
                on_click=State.convert
                ),
            rx.text(
                f'chars: {State.blog_count}',
            ),
            width='70%',
            margin_top='3%',
            height='90%',
            text_align='center',
        ),
        rx.vstack(
            rx.foreach(
                State.posts,
                colored_box,
            ),
            width='60%',
        ),
        margin_bottom='10px',
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
