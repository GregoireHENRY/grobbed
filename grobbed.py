#!/usr/bin/env python

import time
from pathlib import Path

# from pudb import set_trace as bp  # noqa:F401
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from urlpath import URL as Url
from webdriver_manager.firefox import GeckoDriverManager

CONFIG_PATH = Path("config.yaml")


def read_yaml(PATH: Path) -> dict:
    with PATH.open("r") as STREAM:
        return yaml.safe_load(STREAM)


def moves_to_pgn(MOVES: list) -> str:
    """
    Convert moves to pgn.

    >>> MOVES = ['d4', 'Nf6', 'c4', 'e6', 'g4', 'd5', 'g5', 'Ne4']

    >>> moves_to_pgn(MOVES)
    '1.d4 Nf6 2.c4 e6 3.g4 d5 4.g5 Ne4'
    """
    IT = iter(MOVES)
    return " ".join(
        (
            f"{INDEX + 1}.{MOVE1} {MOVE2}"
            for INDEX, (MOVE1, MOVE2) in enumerate(zip(IT, IT))
        )
    )


def parse_move_list(MOVE_LIST: str) -> list:
    """
    Parse move list.

    >>> MOVE_LIST = "'1.\nd4\n-11:33.0\nNf6\n-11:58.0\n2.\nc4\n11.0\ne6\n28.0\n3.\ng4\n21.0\nd5\n8:18.0\n4.\ng5\n36.0\nNe4\n2:16.0"

    >>> parse_move_list(MOVE_LIST)
    ['d4', 'Nf6', 'c4', 'e6', 'g4', 'd5', 'g5', 'Ne4']
    """

    return [
        ELEMENT
        for INDEX, ELEMENT in enumerate(MOVE_LIST.split("\n"))
        if INDEX % 5 in (1, 3)
    ]


def main() -> None:
    CONFIG = read_yaml(CONFIG_PATH)
    PAIR = 2

    OPTIONS = Options()
    OPTIONS.add_argument("--headless")

    print("Initialising...")
    SERVICE = Service(GeckoDriverManager(log_level=0).install())
    with webdriver.Firefox(service=SERVICE, options=OPTIONS) as DRIVER:
        TABS = {}
        WAIT = WebDriverWait(DRIVER, 10.0)

        for INDEX, URL in enumerate(CONFIG["URL"]):
            # Open URL.
            URL = Url(URL)
            print(f"Opening {URL}.")
            if INDEX:
                TAB = f"tab{INDEX}"
                DRIVER.execute_script(f"window.open('about:blank', '{TAB}');")
                DRIVER.switch_to.window(TAB)
            else:
                TAB = DRIVER.window_handles[0]
            DRIVER.get(str(URL))

            # Hide sidebar.
            DRIVER.find_element(By.CLASS_NAME, "sidebar-toggle").click()

            # Select move list.
            TABS[TAB] = WAIT.until(
                EC.presence_of_element_located((By.CLASS_NAME, "vertical-move-list"))
            )

        print()
        index = 0
        while True:
            for TAB in list(TABS.keys()):
                DRIVER.switch_to.window(TAB)
                URL = Url(DRIVER.current_url)
                print(f"Getting new moves of {URL.name} ({index})")
                MOVES = parse_move_list(TABS[TAB].text)

                MAX_INDEX = min(PAIR * CONFIG["BEFORE_TURN"], len(MOVES))
                if CONFIG["MOVE"] in MOVES[:MAX_INDEX]:
                    print()
                    print("/!\\ " * 10)
                    print("ALERT GROB!")
                    print(f"{URL.name}")
                    print("/!\\ " * 10)
                    print()
                    print(moves_to_pgn(MOVES))
                    print()
                    TABS.pop(TAB)

            time.sleep(CONFIG["SLEEP"])
            index += 1


if __name__ == "__main__":
    main()
