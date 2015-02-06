import sys

if sys.version_info[0] == 2:
    raise ImportWarning("GitGadget does not support Sublime Text 2.")
else:
    def plugin_loaded():
        from .common import util
        util.determine_syntax_files()

    from .common.log import GgDisplayPanelCommand
    from .common.debug import GsReloadModulesDebug
    from .commands import *
