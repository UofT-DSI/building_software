import numpy as np
from pytest import approx

def load_from_file(filename):
    radii = np.loadtxt(filename)
    return radii

def calc_area_circle(radii):
    areas = np.pi * radii**2
    return areas

def test_load_and_calculate():
    #### Generate test case ####
    # save list of radii
    np.array([5.2, 1.1, 9.3, 11.4, 19.2]).savetxt('radii.txt')

    #### Run function ####
    # load list of radii
    radii_list = load_from_file('radii.txt')

    # calculate area
    area_list = calc_area_circle(radii_list)

    #### Test result ####
    assert area_list == approx([84.95, 3.8, 271.7, 408.3, 1158.1])
