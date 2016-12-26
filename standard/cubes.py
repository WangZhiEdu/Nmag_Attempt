import math
import time
import nmag
from nmag.common import *
from nmag import SI, every, at

# mesh file
mesh_file = 'cubes.nmesh.h5'

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

# --------------------------------------------------------------------------- #
Mat_Hard = nmag.MagMaterial(name='Mat_Hard',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
Mat_Soft = nmag.MagMaterial(name='Mat_Soft',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
# --------------------------------------------------------------------------- #

# Max Apply Field
H_max = 2*ku_hard*1e4/ms_hard
H_max = H_max*1e3/(4*math.pi)  # koe to A/m
print('H_max %f' % H_max)

# Hysteresis Apply Field List
Hs = nmag.vector_set(direction=[0, 0, 1],
                     norm_list=[-1.0, -0.8, [], 0.0, 0.01, [], 1.0],
                     units=H_max*SI('A/m'))

# create a simulation
sim = nmag.Simulation()
# load mesh
sim.load_mesh('%s'%mesh_file,
              [('Mat_Hard', Mat_Hard), ('Mat_Soft', Mat_Soft)],
              unit_length=SI(1e-9, 'm'))
# set initial magnetisation
sim.set_m([0, 0, 1])


def my_save(sim):
    # only save these Terms and Subfields
    H_ext = sim.get_subfield_average_siv('H_ext')
    print('Save fields of stage %d with H_ext %s' %(sim.stage, str(H_ext)))
    sim.save_data(fields=['id', 'time', 'step', 'stage_time', 'stage_step', 'H_ext', 'M', 'm'])


def my_stage(sim):
    # run the function before every stage start
    H_ext = sim.get_subfield_average_siv('H_ext')
    print('Set new H_ext of stage %d with H_ext %s' %(sim.stage, str(H_ext)))
    def set_H(position):
        x = position[0]
        y = position[1]
        z = position[2]
        return H_ext
    sim.set_H_ext(set_H, unit=SI(1,'A/m'))

# start time
start_time = time.time()
# start hysteresis
sim.hysteresis(Hs, save=[(my_save, at('convergence'))],
               do=[(my_stage, every('stage', 1) & at('stage_step', 0))])
# print simulate time
use_time = (time.time() - start_time) / 60
print('Use Time %f min' % use_time)