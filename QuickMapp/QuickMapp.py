"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def feature_button(name: str):
    return rx.flex(
        name,
        color="#848496",
        size="2",
        padding=".25em 1em",
        background="linear-gradient(#131217, #131217) padding-box, linear-gradient(to bottom right, #8F93BC 5%, #656484 15%, #232329) border-box;",
        border="1px solid transparent;",
        font_size=".8em",
        border_radius="50px",
    )


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),

        rx.vstack(
            rx.heading("Write Once, Run Anywhere", size="9"),

            rx.hstack(
                feature_button("iOS"),
                feature_button("Android"),
                feature_button("macOS"),
                feature_button("Windows "),
                justify="start",
                width="100%",
            ),
            rx.chakra.text(
                "We build native, cross-platform desktop,web and mobile apps",
                text_align="left",
                background_image="linear-gradient(95deg, #D6D6ED 42.14%, #727280 63.21%)",
                font_size=["24px", "30px", "40px", "54px", "54px", "54px"],
                background_clip="text",
                font_weight="bold",
                line_height="1",

            ),
            rx.chakra.text(
                "Ready to get started?",
                text_align="left",
                color="#6C6C81",
                font_size=["24px", "30px", "40px", "54px", "54px", "54px"],
                font_weight="bold",
                line_height="1",
                max_width=["200px", "300px", "400px", "650px", "650px", "650px"],
            ),
            rx.text(
                "📅",
                rx.code(f"Schedule a call with QuickMapp to discuss your project."),
                size="5",
            ),
            rx.link(
                rx.button("Schedule a call"),
                href="https://calendar.app.google/34gY3WvUnv1p1UAk6",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),

        # rx.logo(),

        rx.link(
            rx.button(
                "Linkedin",
                border_radius="1em",
                box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
                background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
                box_sizing="border-box",
                color="white",
                opacity=1,
                _hover={
                    "opacity": 0.5,
                },
            ),
            href="https://www.linkedin.com/company/quickmapp/",
            is_external=True,
        ),
    )

app = rx.App()
app.add_page(index)
