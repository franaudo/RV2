from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino

from compas.geometry import subtract_vectors
from compas.geometry import scale_vector
from compas.geometry import Translation

from compas_rv2.datastructures import ForceDiagram
from compas_rv2.rhino import get_scene


__commandname__ = "RV2force_create"


HERE = compas_rhino.get_document_dirname()


def RunCommand(is_interactive):

    scene = get_scene()
    if not scene:
        return

    form = scene.get("form")

    if not form:
        return

    force = ForceDiagram.from_formdiagram(form.datastructure)

    bbox = force.bounding_box()

    a = bbox[0]
    b = bbox[1]

    ab = subtract_vectors(b, a)
    ab = scale_vector(ab, 1.5)

    T = Translation(ab)

    force.transform(T)

    scene.add(force, name='force')
    scene.update()


# ==============================================================================
# Main
# ==============================================================================

if __name__ == "__main__":

    RunCommand(True)
