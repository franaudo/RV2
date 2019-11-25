from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

# check if the following exist
# - conda: ask user to install Anaconda/Miniconda

# insert local lib in path
# remove again after imports?

# start a proxy with the environment set to use the local libs?

import scriptcontext as sc

try:
    import compas        # noqa: F401
    import compas_rhino  # noqa: F401
    import compas_ags    # noqa: F401
    import compas_tna    # noqa: F401

except ImportError:
    # do something here to fix the problem
    pass

else:
    # replace this by from compas_cloud import Proxy
    from compas.rpc import Proxy
    from compas_rhino.etoforms import ImageForm


__commandname__ = "RV2init"


def RunCommand(is_interactive):
    sc.sticky["RV2"] = {
        # the names of the settings can be split at the dot to allow for grouping
        "session": {
            "cwd": None,
            "ext": 'rv2',
            "current": None
        },
        "settings": {
            "layers.form": "RV2::FormDiagram",
            "layers.force": "RV2::ForceDiagram",
            "layers.thrust": "RV2::ThrustNetwork"
        },
        "data": {
            "form": None,
            "force": None,
            "thrust": None
        }
        # solver settings?
    }

    Proxy()  # use a RV2-specific address (port)

    # display the "welcome" screen
    form = ImageForm('http://block.arch.ethz.ch/brg/images/cache/dsc02360_ni-2_cropped_1528706473_624x351.jpg')
    form.show()


# ==============================================================================
# Main
# ==============================================================================

if __name__ == '__main__':

    RunCommand(True)
