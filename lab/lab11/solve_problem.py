import numpy as np
import porepy as pp
import pygeon as pg
import scipy.sparse as sps

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF


def solve_problem(sd, perm):
    """
    Solves a flow problem using the Two-Point Flux Approximation (TPFA) method.

    Args:
        sd (pp.Grid): The grid object containing the spatial discretization.
        perm (float): The permeability value for the medium.

    Returns:
        numpy.ndarray: The solution vector containing the cell pressures.
    """
    key = "flow"

    # set up the data for the flow problem
    data = {}

    # Permeability
    sot = pp.SecondOrderTensor(perm * np.ones(sd.num_cells))

    # Boundary conditions
    b_faces = sd.tags["domain_boundary_faces"].nonzero()[0]
    b_face_centers = sd.face_centers[:, b_faces]

    # define outflow and inflow type boundary conditions, left and right boundary
    out_flow = np.isclose(b_face_centers[1, :], np.amax(sd.nodes[1]))
    in_flow = np.isclose(b_face_centers[1, :], np.amin(sd.nodes[1]))

    # define the labels and values for the boundary faces
    labels = np.array(["dir"] * b_faces.size)

    bc_val = 1 - sd.face_centers[1]
    bc = pp.BoundaryCondition(sd, b_faces, labels)

    # Collect all parameters in a dictionary
    parameters = {"second_order_tensor": sot, "bc": bc, "bc_values": bc_val}
    data = pp.initialize_default_data(sd, {}, key, parameters)

    # construct the lhr and rhs from the discretization of the diffusion operator
    tpfa = pp.Tpfa(key)
    tpfa.discretize(sd, data)
    A_tpfa, b_tpfa = tpfa.assemble_matrix_rhs(sd, data)

    # solve the problem
    cell_p_tpfa = sps.linalg.spsolve(A_tpfa, b_tpfa)

    mat_discr = data[pp.DISCRETIZATION_MATRICES][key]
    q = mat_discr["flux"] @ cell_p_tpfa + mat_discr["bound_flux"] @ bc_val

    return cell_p_tpfa, np.sum(q[b_faces[out_flow]])


def generate_perm(sd, params, **kwargs):
    """
    Generate a permutation based on the given parameters.

    Args:
        sd (pp.Grid): The grid object containing the spatial discretization.
        params (list): Parameters required for generating the permeability.
        seed (int, optional): Seed for the random number generator to ensure reproducibility.
            Defaults to None.

    Returns:
        np.ndarray: The generated permeability.
    """
    # Set seed for reproducibility
    np.random.seed(kwargs.get("seed", None))

    # Gaussian Process with RBF kernel for simulation
    kernel = RBF(length_scale=params)
    gp = GaussianProcessRegressor(kernel=kernel, optimizer=None)

    # Fit the GP to random data
    space = np.arange(1, np.sqrt(sd.num_cells) + 1)
    xy = np.array(np.meshgrid(space, space)).T.reshape(-1, 2)
    gp.fit(xy, np.random.rand(xy.shape[0]))

    # Simulate predictions
    phi = gp.sample_y(xy, n_samples=1).flatten()
    phi = np.abs(phi)
    # Ensure porosity in [0, 1]
    # phi = np.clip(np.abs(phi), 0, 1)

    # Reference values for porosity and permeability
    perm_ref = kwargs.get("perm_ref", 1)

    # Use a Kozeni-Carman model to generate permeability
    perm = perm_ref * np.power(phi, 3) / np.square(1 - phi)

    return perm


def generate_(file_name):
    porosity = np.loadtxt(file_name, skip)

    dim = 2

    # creation of a Cartesian grid
    sd = pp.CartGrid([25] * dim, [1] * dim)

    # compute the geometrical properties of the grid
    sd.compute_geometry()

    return sd, porosity
