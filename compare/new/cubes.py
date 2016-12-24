import math
import time
import nmag
from nmag.common import *
from nmag import SI, every, at

mesh_file = 'cubes.nmesh.h5'

sim = nmag.Simulation()
# height
hard_h = 4.0
soft_h = 6.0
# Saturation Magnetization -- M
ms_hard = 0.5e6
M_hard = SI(ms_hard, 'A/m')
M_soft = SI(1.2e6, 'A/m')
# Exchange coupling strength -- A
A_hard = SI(1.2e-11, "J/m")
A_soft = SI(2.8e-11, "J/m")
# Anisotropy -- K
Stability_constant = 55 * 1.38e-23 * 350  # Stability Constant
Area_constant = 25e-27  # Area Constant = area * 1e-9
ku_soft = 100.0
ku_hard = (Stability_constant / Area_constant - ku_soft * soft_h) / hard_h
print('ku_hard %f' % ku_hard)
K_hard = SI(ku_hard, "J/m^3")
K_soft = SI(ku_soft, "J/m^3")
# Max Apply Field
H_max = 2 * ku_hard * 1e4 / ms_hard
H_max = H_max * 1e3/(4*math.pi)  # koe to A/m
print('H_max %f' % H_max)
Mat_Hard = nmag.MagMaterial(name='Mat_Hard',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=[0, 0.05, -1.0], K1=K_hard),
    llg_damping=1.0)

Mat_Soft = nmag.MagMaterial(name='Mat_Soft',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=[0, 0, -1.0], K1=K_soft),
    llg_damping=1.0)

# load mesh
sim.load_mesh('%s'%mesh_file,
              [('Mat_Hard', Mat_Hard),('Mat_Soft', Mat_Soft)],
              unit_length=SI(1e-9, 'm'))

sim.set_m([0,0,1])

Hs = nmag.vector_set(direction=[0, 0, 1],
                     norm_list=[-1.0, -0.8, [], 0.0, 0.01, [], 1.0],
                     units=H_max*SI('A/m'))

def my_save(sim):
    # only save M, m, H_ext
    sim.save_data(fields=['M', 'm', 'H_ext'])


def print_time(sim):
    sim_time = float(sim.time/SI(1e-12, 's'))
    print('----SIM Time %f ps----' % sim_time)

# start time
start_time = time.time()

sim.hysteresis(Hs, save=[(my_save, at('convergence'))],
               do=[(print_time, every('time',SI(50e-12, 's')) | at('convergence'))])

use_time = (time.time() - start_time) / 60
print('Use Time %f min' % use_time)