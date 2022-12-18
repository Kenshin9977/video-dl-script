import logging

import fire

from gui_flet import videodl_gui
from updater.updater import update_app
from videodl_logger import videodl_logger

logger = logging.getLogger()

if __name__ == "__main__":
    fire.Fire(videodl_logger)
    logger.debug("Updating the app")
    update_succeeded = update_app()
    if update_succeeded:
        logger.debug("GUI's startup")
        videodl_gui()

# TODO: Sign updates
# TODO: Autoinstall ffmpeg if missing on MacOS and Linux
