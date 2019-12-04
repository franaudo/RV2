from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas_rv2.rhino import RhinoDiagram


__all__ = ["RhinoForceDiagram"]


class RhinoForceDiagram(RhinoDiagram):

    def draw(self, settings):
        self.artist.layer = settings.get("layers.force")
        self.artist.clear_layer()

        if settings.get("show.force.vertices", True):
            color = {}
            color.update({key: settings.get("color.force.vertices") for key in self.diagram.vertices()})
            # color.update({key: settings.get("color.force.vertices:is_fixed") for key in self.diagram.vertices_where({'is_fixed': True})})
            # color.update({key: settings.get("color.force.vertices:is_external") for key in self.diagram.vertices_where({'is_external': True})})
            # color.update({key: settings.get("color.force.vertices:is_anchor") for key in self.diagram.vertices_where({'is_anchor': True})})
            self.artist.draw_vertices(color=color)

        if settings.get("show.force.edges", True):
            keys = list(self.diagram.edges_where({'is_edge': True}))
            color = {}
            color.update({key: settings.get("color.force.edges") for key in keys})
            self.artist.draw_edges(keys=keys, color=color)

        if settings.get("show.force.faces", True):
            keys = list(self.diagram.faces_where({'is_loaded': True}))
            color = {}
            color.update({key: settings.get("color.force.faces") for key in keys})
            self.artist.draw_faces(keys=keys, color=color)

        self.artist.redraw()


# ==============================================================================
# Main
# ==============================================================================

if __name__ == '__main__':
    pass