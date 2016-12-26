import math
import time
import nmag
from nmag.common import *
from nmag import SI, every, at

# mesh file
mesh_file = 'cube_98.nmesh.h5'

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
H_5 = nmag.MagMaterial(name='H_5',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_6 = nmag.MagMaterial(name='S_6',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_7 = nmag.MagMaterial(name='H_7',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_8 = nmag.MagMaterial(name='S_8',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_9 = nmag.MagMaterial(name='H_9',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_10 = nmag.MagMaterial(name='S_10',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_11 = nmag.MagMaterial(name='H_11',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_12 = nmag.MagMaterial(name='S_12',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_13 = nmag.MagMaterial(name='H_13',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_14 = nmag.MagMaterial(name='S_14',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_15 = nmag.MagMaterial(name='H_15',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_16 = nmag.MagMaterial(name='S_16',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_17 = nmag.MagMaterial(name='H_17',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_18 = nmag.MagMaterial(name='S_18',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_19 = nmag.MagMaterial(name='H_19',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_20 = nmag.MagMaterial(name='S_20',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_21 = nmag.MagMaterial(name='H_21',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_22 = nmag.MagMaterial(name='S_22',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_23 = nmag.MagMaterial(name='H_23',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_24 = nmag.MagMaterial(name='S_24',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_25 = nmag.MagMaterial(name='H_25',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_26 = nmag.MagMaterial(name='S_26',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_27 = nmag.MagMaterial(name='H_27',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_28 = nmag.MagMaterial(name='S_28',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_29 = nmag.MagMaterial(name='H_29',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_30 = nmag.MagMaterial(name='S_30',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_31 = nmag.MagMaterial(name='H_31',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_32 = nmag.MagMaterial(name='S_32',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_33 = nmag.MagMaterial(name='H_33',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_34 = nmag.MagMaterial(name='S_34',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_35 = nmag.MagMaterial(name='H_35',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_36 = nmag.MagMaterial(name='S_36',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_37 = nmag.MagMaterial(name='H_37',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_38 = nmag.MagMaterial(name='S_38',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_39 = nmag.MagMaterial(name='H_39',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_40 = nmag.MagMaterial(name='S_40',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_41 = nmag.MagMaterial(name='H_41',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_42 = nmag.MagMaterial(name='S_42',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_43 = nmag.MagMaterial(name='H_43',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_44 = nmag.MagMaterial(name='S_44',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_45 = nmag.MagMaterial(name='H_45',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_46 = nmag.MagMaterial(name='S_46',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_47 = nmag.MagMaterial(name='H_47',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_48 = nmag.MagMaterial(name='S_48',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_49 = nmag.MagMaterial(name='H_49',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_50 = nmag.MagMaterial(name='S_50',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_51 = nmag.MagMaterial(name='H_51',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_52 = nmag.MagMaterial(name='S_52',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_53 = nmag.MagMaterial(name='H_53',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_54 = nmag.MagMaterial(name='S_54',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_55 = nmag.MagMaterial(name='H_55',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_56 = nmag.MagMaterial(name='S_56',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_57 = nmag.MagMaterial(name='H_57',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_58 = nmag.MagMaterial(name='S_58',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_59 = nmag.MagMaterial(name='H_59',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_60 = nmag.MagMaterial(name='S_60',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_61 = nmag.MagMaterial(name='H_61',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_62 = nmag.MagMaterial(name='S_62',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_63 = nmag.MagMaterial(name='H_63',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_64 = nmag.MagMaterial(name='S_64',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_65 = nmag.MagMaterial(name='H_65',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_66 = nmag.MagMaterial(name='S_66',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_67 = nmag.MagMaterial(name='H_67',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_68 = nmag.MagMaterial(name='S_68',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_69 = nmag.MagMaterial(name='H_69',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_70 = nmag.MagMaterial(name='S_70',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_71 = nmag.MagMaterial(name='H_71',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_72 = nmag.MagMaterial(name='S_72',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_73 = nmag.MagMaterial(name='H_73',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_74 = nmag.MagMaterial(name='S_74',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_75 = nmag.MagMaterial(name='H_75',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_76 = nmag.MagMaterial(name='S_76',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_77 = nmag.MagMaterial(name='H_77',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_78 = nmag.MagMaterial(name='S_78',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_79 = nmag.MagMaterial(name='H_79',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_80 = nmag.MagMaterial(name='S_80',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_81 = nmag.MagMaterial(name='H_81',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_82 = nmag.MagMaterial(name='S_82',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_83 = nmag.MagMaterial(name='H_83',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_84 = nmag.MagMaterial(name='S_84',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_85 = nmag.MagMaterial(name='H_85',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_86 = nmag.MagMaterial(name='S_86',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_87 = nmag.MagMaterial(name='H_87',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_88 = nmag.MagMaterial(name='S_88',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_89 = nmag.MagMaterial(name='H_89',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_90 = nmag.MagMaterial(name='S_90',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_91 = nmag.MagMaterial(name='H_91',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_92 = nmag.MagMaterial(name='S_92',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_93 = nmag.MagMaterial(name='H_93',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_94 = nmag.MagMaterial(name='S_94',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_95 = nmag.MagMaterial(name='H_95',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_96 = nmag.MagMaterial(name='S_96',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H_97 = nmag.MagMaterial(name='H_97',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S_98 = nmag.MagMaterial(name='S_98',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
sim.load_mesh("%s"%mesh_file, [("H_1", H_1),
		("S_2", S_2),
		("H_3", H_3),
		("S_4", S_4),
		("H_5", H_5),
		("S_6", S_6),
		("H_7", H_7),
		("S_8", S_8),
		("H_9", H_9),
		("S_10", S_10),
		("H_11", H_11),
		("S_12", S_12),
		("H_13", H_13),
		("S_14", S_14),
		("H_15", H_15),
		("S_16", S_16),
		("H_17", H_17),
		("S_18", S_18),
		("H_19", H_19),
		("S_20", S_20),
		("H_21", H_21),
		("S_22", S_22),
		("H_23", H_23),
		("S_24", S_24),
		("H_25", H_25),
		("S_26", S_26),
		("H_27", H_27),
		("S_28", S_28),
		("H_29", H_29),
		("S_30", S_30),
		("H_31", H_31),
		("S_32", S_32),
		("H_33", H_33),
		("S_34", S_34),
		("H_35", H_35),
		("S_36", S_36),
		("H_37", H_37),
		("S_38", S_38),
		("H_39", H_39),
		("S_40", S_40),
		("H_41", H_41),
		("S_42", S_42),
		("H_43", H_43),
		("S_44", S_44),
		("H_45", H_45),
		("S_46", S_46),
		("H_47", H_47),
		("S_48", S_48),
		("H_49", H_49),
		("S_50", S_50),
		("H_51", H_51),
		("S_52", S_52),
		("H_53", H_53),
		("S_54", S_54),
		("H_55", H_55),
		("S_56", S_56),
		("H_57", H_57),
		("S_58", S_58),
		("H_59", H_59),
		("S_60", S_60),
		("H_61", H_61),
		("S_62", S_62),
		("H_63", H_63),
		("S_64", S_64),
		("H_65", H_65),
		("S_66", S_66),
		("H_67", H_67),
		("S_68", S_68),
		("H_69", H_69),
		("S_70", S_70),
		("H_71", H_71),
		("S_72", S_72),
		("H_73", H_73),
		("S_74", S_74),
		("H_75", H_75),
		("S_76", S_76),
		("H_77", H_77),
		("S_78", S_78),
		("H_79", H_79),
		("S_80", S_80),
		("H_81", H_81),
		("S_82", S_82),
		("H_83", H_83),
		("S_84", S_84),
		("H_85", H_85),
		("S_86", S_86),
		("H_87", H_87),
		("S_88", S_88),
		("H_89", H_89),
		("S_90", S_90),
		("H_91", H_91),
		("S_92", S_92),
		("H_93", H_93),
		("S_94", S_94),
		("H_95", H_95),
		("S_96", S_96),
		("H_97", H_97),
		("S_98", S_98)],
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

# save initial data
sim.relax(save=[(my_save, at('convergence'))])

# make H_ext = -H_max where y > 10
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

# make H_ext = H_max where y > 10
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