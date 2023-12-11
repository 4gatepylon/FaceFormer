import open3d as o3d


# NOTE you will need Werkzeug version 2 not 3 (you should use poetry or something like that) as well as a brew
# installation (check the requirements)
#
# TODO(Adriano) set up poetry or generally a better solution because we cannot be pip installing and uninstalling :/
def display_ply(filepath):
    # Load the PLY file
    mesh = o3d.io.read_triangle_mesh(filepath)

    # Check if the mesh contains vertex colors
    if mesh.has_vertex_colors():
        # If it does, use it as is
        o3d.visualization.draw_geometries([mesh])
    else:
        # If not, create a default visualization
        mesh.compute_vertex_normals()
        o3d.visualization.draw_geometries([mesh], mesh_show_back_face=True)


# Replace 'your_file.ply' with the path to your PLY file
display_ply("FLAME_sample.ply")
