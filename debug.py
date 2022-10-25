import logging
import traceback

import debugpy

logger = logging.getLogger(__name__)


def connect_to_debugger(use_listen: bool = False):
    """Connect to VS Code debugger using debugpy.

    :param use_listen: Use listen instead of connect.
    """
    address = 5678
    try:
        if use_listen:
            debugpy.listen(address)
        else:
            debugpy.connect(address)
    except Exception:
        logger.warning(traceback.format_exc())
