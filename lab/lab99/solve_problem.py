import numpy as np
import porepy as pp
import pygeon as pg
import scipy.sparse as sps


def solve_problem(sd, perm_mu):
    """
    Solves a flow problem using the Two-Point Flux Approximation (TPFA) method.

    Args:
        sd (pp.Grid): The grid object containing the spatial discretization.
        perm_mu (np.ndarray): The permeability value for the medium over the liquid viscosity.

    Returns:
        np.ndarray: The solution vector containing the cell pressures.
        float: The total flow rate at the outflow boundary.
    """
    key = "flow"

    # set up the data for the flow problem
    data = {}

    # Permeability tensor of the medium over the liquid viscosity
    sot = pp.SecondOrderTensor(perm_mu * np.ones(sd.num_cells))

    # Boundary conditions
    b_faces = sd.tags["domain_boundary_faces"].nonzero()[0]
    b_face_centers = sd.face_centers[:, b_faces]

    # define outflow and inflow type boundary conditions, left and right boundary
    out_flow = np.isclose(b_face_centers[1, :], np.amax(sd.nodes[1]))

    # define the labels and values for the boundary faces
    labels = np.array(["dir"] * b_faces.size)

    # set the inflow boundary condition
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

    # compute the total flow rate at the outflow boundary
    mat_discr = data[pp.DISCRETIZATION_MATRICES][key]
    q = mat_discr["flux"] @ cell_p_tpfa + mat_discr["bound_flux"] @ bc_val

    # return the pressure solution and the total flow rate at the outflow boundary
    return cell_p_tpfa, np.sum(q[b_faces[out_flow]])
