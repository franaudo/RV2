from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas.geometry import Point
from compas.geometry import Scale
from compas.geometry import Translation
from compas.geometry import Rotation

from .meshobject import MeshObject


__all__ = ["PatternObject"]


class PatternObject(MeshObject):
    """Scene object for patterns in RV2.
    """

    SETTINGS = {
        'layer': "RV2::Pattern",
        'show.vertices': True,
        'show.edges': True,
        'show.faces': False,
        'color.vertices': [255, 255, 255],
        'color.vertices:is_anchor': [255, 0, 0],
        'color.vertices:is_fixed': [0, 0, 255],
        'color.vertices:is_constrained': [0, 255, 255],
        'color.edges': [0, 0, 0],
        'color.faces': [200, 200, 200],
        'from_surface.density.U': 10,
        'from_surface.density.V': 10,
    }

    @property
    def vertex_xyz(self):
        """dict : The view coordinates of the mesh object."""
        origin = Point(0, 0, 0)
        if self.anchor is not None:
            xyz = self.mesh.vertex_attributes(self.anchor, 'xyz')
            point = Point(* xyz)
            T1 = Translation.from_vector(origin - point)
            S = Scale.from_factors([self.scale] * 3)
            R = Rotation.from_euler_angles(self.rotation)
            T2 = Translation.from_vector(self.location)
            X = T2 * R * S * T1
        else:
            S = Scale.from_factors([self.scale] * 3)
            R = Rotation.from_euler_angles(self.rotation)
            T = Translation.from_vector(self.location)
            X = T * R * S
        mesh = self.mesh.transformed(X)
        vertex_xyz = {vertex: mesh.vertex_attributes(vertex, 'xyz') for vertex in mesh.vertices()}
        return vertex_xyz

    def draw(self):
        """Draw the objects representing the force diagram.
        """
        layer = self.settings['layer']
        self.artist.layer = layer
        self.artist.clear_layer()
        self.clear()
        if not self.visible:
            return
        self.artist.vertex_xyz = self.vertex_xyz

        # ======================================================================
        # Groups
        # ------
        # Create groups for vertices, edges, and faces.
        # These groups will be turned on/off based on the visibility settings of the diagram
        # ======================================================================

        group_vertices = "{}::vertices".format(layer)
        group_edges = "{}::edges".format(layer)
        group_faces = "{}::faces".format(layer)

        if not compas_rhino.rs.IsGroup(group_vertices):
            compas_rhino.rs.AddGroup(group_vertices)

        if not compas_rhino.rs.IsGroup(group_edges):
            compas_rhino.rs.AddGroup(group_edges)

        if not compas_rhino.rs.IsGroup(group_faces):
            compas_rhino.rs.AddGroup(group_faces)

        # ======================================================================
        # Vertices
        # --------
        # Draw the vertices and add them to the vertex group.
        # ======================================================================

        vertices = list(self.mesh.vertices())
        color = {vertex: self.settings['color.vertices'] for vertex in vertices}
        color_fixed = self.settings['color.vertices:is_fixed']
        color_anchor = self.settings['color.vertices:is_anchor']
        color.update({vertex: color_fixed for vertex in self.mesh.vertices_where({'is_fixed': True})})
        color.update({vertex: color_anchor for vertex in self.mesh.vertices_where({'is_anchor': True})})

        guids = self.artist.draw_vertices(vertices, color)
        self.guid_vertex = zip(guids, vertices)
        compas_rhino.rs.AddObjectsToGroup(guids, group_vertices)

        if self.settings['show.vertices']:
            compas_rhino.rs.ShowGroup(group_vertices)
        else:
            compas_rhino.rs.HideGroup(group_vertices)

        # ======================================================================
        # Edges
        # -----
        # Draw the edges and add them to the edge group.
        # ======================================================================

        edges = list(self.mesh.edges())
        color = {edge: self.settings['color.edges'] for edge in edges}

        guids = self.artist.draw_edges(edges, color)
        self.guid_edge = zip(guids, edges)
        compas_rhino.rs.AddObjectsToGroup(guids, group_edges)

        if self.settings['show.edges']:
            compas_rhino.rs.ShowGroup(group_edges)
        else:
            compas_rhino.rs.HideGroup(group_edges)

        # ======================================================================
        # Faces
        # -----
        # Draw the faces and add them to the face group.
        # ======================================================================

        faces = list(self.mesh.faces())
        color = {face: self.settings['color.faces'] for face in faces}

        guids = self.artist.draw_faces(faces, color)
        self.guid_face = zip(guids, faces)
        compas_rhino.rs.AddObjectsToGroup(guids, group_faces)

        if self.settings['show.faces']:
            compas_rhino.rs.ShowGroup(group_faces)
        else:
            compas_rhino.rs.HideGroup(group_faces)

        # self.redraw()


# ==============================================================================
# Main
# ==============================================================================

if __name__ == '__main__':
    pass
