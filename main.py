# #13547a
# #80d0c7
# #0f172a s-9
# #475569 s-6
import re
from datetime import datetime

import flet as flet
import requests
from flet import (
    Page,
    Column,
    Row,
    alignment,
    padding,
    ResponsiveRow,
    Container,
    Text,
    LinearGradient,
    CircleAvatar,
    TextField,
    TextButton,
    InputBorder,
    TextStyle,
)


def main(page: Page):
    def download_video(e):
        url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"
        video_url = url_tiktok_textField.value

        querystring = {"url": video_url}

        headers = {
            "X-RapidAPI-Key": "c222310903mshb5d1b8c262a58c6p16a432jsn6a46191623eb",
            "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring, allow_redirects=True)

        data = response.text
        video = data.replace('[', '')
        link = re.findall(r'{"video":"([^"]+)"', video)
        url_video = ''.join(link)

        now = datetime.now()
        name = f'tiktok_{now.strftime("%Y%m%d%H%M%S")}.mp4'

        r = requests.get(url_video)
        return open(name, "wb").write(r.content)

    #
    def paste_click(e):
        url_tiktok = page.get_clipboard()
        url_tiktok_textField.value = url_tiktok
        url_change.content = TextButton(
            "Delete",
            on_click=delete_click,
            height=50
        )
        page.update()

    def delete_click(e):
        url_tiktok_textField.value = ""
        url_change.content = TextButton(
            "Paste",
            on_click=paste_click,
            height=50
        )
        page.update()

    nav = Container(
        ResponsiveRow([
            Column(
                col={"xs": 12, "sm": 12, "md": 12, "xl": 12},
                controls=[
                    Container(
                        padding=20,
                        bgcolor="#DEDEDE",
                        content=Row([
                            CircleAvatar(
                                width=60,
                                height=60,
                                bgcolor="white",
                                content=
                                Text("TD",
                                     size=30,
                                     weight="w900",
                                     color="black",
                                     text_align="center",
                                     ),

                            ),
                        ],
                            alignment="spaceBetween")
                    )
                ]
            )
        ]),
    )

    title = ResponsiveRow(
        alignment="center",
        controls=[
            Container(
                col={"xs": 12, "sm": 10, "md": 10, "xl": 12},
                alignment=alignment.top_center,
                padding=30,
                content=Text(
                    'Tải Video TikTok Miễn Phí.',
                    size=40,
                    weight="w600",
                    text_align="center",
                ),
            )
        ],
    )

    url_tiktok_textField = TextField(
        disabled=True,
        border=InputBorder.NONE,
        content_padding=padding.only(
            top=0,
            bottom=0,
            right=20,
            left=20
        ),
        hint_style=TextStyle(
            size=16,
            color='#9DB2BF'
        ),
        text_style=TextStyle(
            size=18,
            color='black',
        ),
        hint_text='Dán liên kết Tiktok vào đây',
        cursor_color='black',
        width=386,
        height=50,
        col={"sm": 8, "md": 12, "lg": 10, "xl": 12},
    )

    url_change = Container(
        height=49,
        width=70,
        bgcolor="blue600",
        border_radius=10,
        padding=0,
        content=TextButton(
            "Paste",
            on_click=paste_click,
            height=50
        ),
    )

    url_download = Container(
        height=50,
        width=90,
        bgcolor="blue600",
        border_radius=10,
        padding=0,
        content=TextButton(
            "Download",
            on_click=download_video,
            height=50,
            width=70
        ),
    )

    container_input = Container(
        alignment=alignment.center,
        bgcolor="white",
        padding=2,
        border_radius=10,
        col={"sm": 10, "md": 10, "lg": 6, "xl": 5},
        content=Row([
            url_tiktok_textField,
            url_change
        ],
            alignment="spaceBetween"
        ),
    )

    container_download = Container(
        bgcolor="white",
        padding=2,
        border_radius=10,
        col={"sm": 10, "md": 10, "lg": 1.2, "xl": 1},
        content=url_download
    )

    item_row = ResponsiveRow(
        alignment="center",
        controls=[
            container_input,
            container_download
        ]
    )

    container_item = Container(
        alignment=alignment.center,
        padding=20,
        content=item_row
    )

    main_col = Column(
        horizontal_alignment="center",
        scroll="auto",
        controls=[
            nav,
            Container(
                padding=padding.only(top=75)
            ),
            title,
            container_item
        ]
    )

    app = Container(
        expand=True,
        margin=-10,
        gradient=LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=["#13547a", "#0f172a"],
        ),
        content=main_col,
    )

    page.add(app)


if __name__ == "__main__":
    flet.app(target=main, view=flet.WEB_BROWSER)
