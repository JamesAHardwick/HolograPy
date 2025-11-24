"""
HolograPy
=========

A collection of utilities for 3D grid generation, acoustic modeling,
and holographic field synthesis.
"""

from .utils import (
    compute_grid_2d,
    compute_grid_3d,
    GF_forward_model,
    PM_forward_model,
    wgs,
    char_to_array,
    plot_transducers_plotly,
    plot_plane_points_plotly,
    plot_plane_edges_plotly,
    plot_vector_arrow_plotly,
    transformation_matrix,
    rotate_vector_in_plane,
    make_transformation
)

__all__ = [
    "compute_grid_2d",
    "compute_3d_grid",
    "GF_forward_model",
    "PM_forward_model",
    "wgs",
    "char_to_array",
    "plot_transducers_plotly",
    "plot_plane_points_plotly",
    "plot_plane_edges_plotly",
    "plot_vector_arrow_plotly",
    "transformation_matrix",
    "rotate_vector_in_plane",
    "make_transformation"
]

__version__ = "0.1.0"
