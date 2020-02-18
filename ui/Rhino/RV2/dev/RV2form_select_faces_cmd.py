from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_rhino.ui import CommandMenu
from compas_rv2.rhino import get_rv2
from compas_rv2.rhino import select_boundary_faces
from compas_rv2.rhino import select_parallel_faces


__commandname__ = "RV2form_select_faces"


HERE = compas_rhino.get_document_dirname()


config = {
    "message": "FormDiagram Select Faces",
    "options": [
        {"name": "Boundary", "action": select_boundary_faces},
        {"name": "Parallel", "action": select_parallel_faces}
    ]
}


def RunCommand(is_interactive):
    RV2 = get_rv2()
    if not RV2:
        return

    rhinoform = RV2["scene"]["form"]
    if not rhinoform:
        return

    settings = RV2["settings"]

    menu = CommandMenu(config)
    action = menu.select_action()

    if not action:
        return

    action["action"](rhinoform)


# ==============================================================================
# Main
# ==============================================================================

if __name__ == "__main__":

    RunCommand(True)