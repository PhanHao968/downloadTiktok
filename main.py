# #13547a
# #80d0c7
# #0f172a s-9
# #475569 s-6
from datetime import datetime
import pyperclip
import re
import clipboard
import requests
import flet as flet
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

    # def page_resize(e):
    #     pw.value = f"{page.width} px"
    #     pw.update()
    #
    # page.on_resize = page_resize
    #
    # pw = Text(bottom=50, right=50, style="displaySmall")
    # page.overlay.append(pw)

    #
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
        # open(name, "wb").write(r.content)
        return open(name, "wb").write(r.content)

    #
    def paste_click(e):
        url_tiktok = pyperclip.paste()
        url_tiktok_textField.value = url_tiktok
        page.update()

    #
    def delete_click(e):
        url_tiktok_textField.value = ""
        page.update()

    #
    def on_button(e):
        str_input = str(url_tiktok_textField.value)

        if str_input == "":
            url_paste.visible = True
            url_paste.update()
            url_delete.visible = False
            url_delete.update()
        else:
            url_paste.visible = False
            url_paste.update()
            url_delete.visible = True
            url_delete.update()

        return on_button

    #
    _nav = Container(
        ResponsiveRow([
            Column(col={"xs": 12, "sm": 12, "md": 12, "xl": 12},
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

                           ], alignment="spaceBetween")
                       )
                   ]
                   )
        ]),
    )

    # titles
    _title = ResponsiveRow(
        alignment="center",
        controls=[
            Container(
                col={"xs": 12, "sm": 10, "md": 10, "xl": 12},
                alignment=alignment.top_center,
                padding=30,
                content=Text('Tải Video TikTok Miễn Phí.',
                             size=40,
                             weight="w600",
                             text_align="center",
                             ),
            )
        ],
    )

    #
    url_tiktok_textField = TextField(
        border=InputBorder.NONE,
        content_padding=padding.only(
            top=0, bottom=0, right=20, left=20),
        hint_style=TextStyle(
            size=16, color='#9DB2BF'
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

    #
    url_paste = Container(
        # col={"sm": 2, "md": 2, "lg": 2, "xl": 2},
        visible=True,
        height=49,
        width=70,
        bgcolor="blue600",
        border_radius=10,
        padding=0,
        content=TextButton("Paste", on_click=paste_click, height=50),
    )
    url_delete = Container(
        visible=False,
        height=49,
        width=70,
        bgcolor="blue600",
        border_radius=10,
        content=TextButton("Delete", on_click=delete_click, height=50)
    )
    url_download = Container(
        # col={"sm": 10, "md": 8, "lg": 1, "xl": 1},
        visible=True,
        height=50,
        width=90,
        bgcolor="blue600",
        border_radius=10,
        padding=0,
        content=TextButton("Download", on_click=download_video, height=50, width=70),
    )

    # 7/6/23
    _item = [url_paste, url_delete]
    _item_row = ResponsiveRow(alignment="center")

    _container_input = Container(
        alignment=alignment.center,

        bgcolor="white",
        padding=2,
        border_radius=10,
        col={"sm": 10, "md": 10, "lg": 6, "xl": 5},
        content=Row([
            url_tiktok_textField,
            url_paste,
            url_delete,
        ], alignment="spaceBetween"),
        on_hover=on_button,
    )

    #
    _container_download = Container(
        # alignment=alignment.center,
        bgcolor="white",
        padding=2,
        border_radius=10,
        col={"sm": 10, "md": 10, "lg": 1.2, "xl": 1},
        content=url_download
    )

    _container_item = Container(
        alignment=alignment.center,
        padding=20,
        content=_item_row
    )


    _item_row.controls.append(_container_input)
    _item_row.controls.append(_container_download)



    # main column
    _main_col = Column(horizontal_alignment="center", scroll="auto")
    _main_col.controls.append(_nav)
    _main_col.controls.append(Container(padding=padding.only(top=75)))
    _main_col.controls.append(_title)
    _main_col.controls.append(_container_item)

    # bg container
    _backround = Container(
        height=page.height,
        expand=True,
        margin=-10,
        gradient=LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=["#13547a", "#0f172a"],
        ),
        content=_main_col,
    )

    page.add(_backround)
    # page_resize(None)


if __name__ == "__main__":
    flet.app(target=main)
