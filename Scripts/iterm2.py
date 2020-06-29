#!/usr/bin/env python3.7

import sys
import iterm2
# This script was created with the "basic" environment which does not support adding dependencies
# with pip.

async def main(connection):
    app = await iterm2.async_get_app(connection)
    session = app.current_terminal_window.current_tab.current_session
    await session.async_send_text(sys.stdin.read())

iterm2.run_until_complete(main)
