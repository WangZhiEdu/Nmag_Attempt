import math
import time
import nmag
from nmag.common import *
from nmag import SI, every, at

# mesh file
mesh_file = 'cube_4.nmesh.h5'

# height
hard_h = 6.0
soft_h = 4.0
# Saturation Magnetization -- M
ms_hard = 0.5e6
M_hard = SI(ms_hard, 'A/m')
M_soft = SI(0.75e6, 'A/m')
# Exchange coupling strength -- A
A_hard = SI(1.2e-11, "J/m")
A_soft = SI(1e-11, "J/m")
# Anisotropy -- K
KA_hard = [0, 0.05, -1.0]
KA_soft = [0, 0, -1.0]
Stability_constant = 55*1.38e-23*350  # Stability Constant
Area_constant = 25e-27  # Area Constant = area * 1e-9
ku_soft = 2.5e5
ku_hard = (Stability_constant/Area_constant-ku_soft*soft_h)/hard_h
print('ku_hard %f' % ku_hard)
K_hard = SI(ku_hard, "J/m^3")
K_soft = SI(ku_soft, "J/m^3")
# LLG damping
LLG_damping = 1.0

# create a simulation
sim = nmag.Simulation()
# --------------------------------------------------------------------------- #
H_1 = nmag.MagMaterial(name='H_1',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_2 = nmag.MagMaterial(name='S_2',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_3 = nmag.MagMaterial(name='H_3',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_4 = nmag.MagMaterial(name='S_4',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
sim.load_mesh("%s"%mesh_file, [("H_1", H_1),
		("S_2", S_2),
		("H_3", H_3),
		("S_4", S_4)],
		unit_length = SI(1e-9,"m"))
# --------------------------------------------------------------------------- #

# Max Apply Field
H_max = 2*ku_hard*1e4/ms_hard
H_max = H_max*1e3/(4*math.pi)  # koe to A/m
print('H_max %f' % H_max)


# set initial magnetisation
sim.set_m([0, 0, 1])
sim.set_params(stopping_dm_dt=2*degrees_per_ns)

def my_save(sim):
    sim.save_data(fields=['id', 'time', 'step', 'stage_time', 'stage_step', 'H_ext', 'M', 'm'])

sim.relax(save=[(my_save, at('convergence'))])

def set_H(position):
    # positions unit is nm
    x = position[0] / 1e-9
    y = position[1] / 1e-9
    z = position[2] / 1e-9
    if y < 10:
        return [0, 0, 0]
    return [0, 0, -H_max]
sim.set_H_ext(set_H, unit=SI(1, 'A/m'))
sim.relax(save=[(my_save, at('convergence'))])
print('------make H_ext reserve------')
def set_H(position):
    # positions unit is nm
    x = position[0] / 1e-9
    y = position[1] / 1e-9
    z = position[2] / 1e-9
    if y < 10:
        return [0, 0, 0]
    return [0, 0, H_max]
sim.set_H_ext(set_H, unit=SI(1, 'A/m'))
sim.relax(save=[(my_save, at('convergence'))])