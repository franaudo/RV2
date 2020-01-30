from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import scriptcontext as sc

import compas_rhino
from compas_rhino.etoforms import TextForm
from compas_rv2.rhino import RhinoFormDiagram
from compas_rv2.rhino import RhinoForceDiagram


__commandname__ = "RV2equilibrium_horizontal"


HERE = compas_rhino.get_document_dirname()


def RunCommand(is_interactive):
    if "RV2" not in sc.sticky:
        form = TextForm('Initialise the plugin first!', 'RV2')
        form.show()
        return

    RV2 = sc.sticky["RV2"]
    settings = RV2["settings"]
    rhinoform = RV2["scene"]["form"]
    rhinoforce = RV2["scene"]["force"]

    proxy = sc.sticky["RV2.proxy"]

    if not rhinoform:
        return

    if not rhinoforce:
        return

    if not proxy:
        return

    proxy.package = "compas_rv2.equilibrium"
    horizontal = proxy.horizontal_nodal_proxy

    formdata, forcedata = horizontal(rhinoform.diagram.data, rhinoforce.diagram.data)

    rhinoform.diagram.data = formdata
    rhinoforce.diagram.data = forcedata

    rhinoform.draw(settings)
    rhinoforce.draw(settings)


# ==============================================================================
# Main
# ==============================================================================

if __name__ == "__main__":

    RunCommand(True)
