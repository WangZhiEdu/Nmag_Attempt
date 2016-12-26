CUBE_NUM = 49
mat_hard_lines = None
mat_soft_lines = None
with open('mat_hard', 'r', encoding='utf-8') as f:
    mat_hard_line = f.read()
with open('mat_soft', 'r', encoding='utf-8') as f:
    mat_soft_line = f.read()
with open('cube_98.py', 'a', encoding='utf-8') as f:
    # Write MagMaterial
    for i in range(1, CUBE_NUM+1):
        physical_hard_index = i * 2 - 1
        physical_soft_index = i * 2
        mat_hard_name = 'H_%d' % physical_hard_index
        mat_soft_name = 'S_%d' % physical_soft_index
        mat_hard = mat_hard_line.replace('MAT_NAME', mat_hard_name)
        mat_soft = mat_soft_line.replace('MAT_NAME', mat_soft_name)
        f.write(mat_hard)
        f.write(mat_soft)
    # Write load mesh
    f.write('sim.load_mesh("%s"%mesh_file, [')
    mesh_list = []
    for i in range(1, CUBE_NUM+1):
        physical_hard_index = i * 2 - 1
        physical_soft_index = i * 2
        mat_hard_name = 'H_%d' % physical_hard_index
        mat_soft_name = 'S_%d' % physical_soft_index
        mesh_list.append('("%s", %s)' % (mat_hard_name, mat_hard_name))
        mesh_list.append('("%s", %s)' % (mat_soft_name, mat_soft_name))
    f.write(',\n\t\t'.join(mesh_list))
    f.write('],\n\t\tunit_length = SI(1e-9,"m"))\n')