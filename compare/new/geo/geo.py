from enum import Enum

MARK_MESH_SIZE = 'mesh_size'
MARK_HARD_HEIGHT = 'hard_height'
MARK_SPACE_HEIGHT = 'space_height'
MARK_SOFT_HEIGHT = 'soft_height'


class GeoModuleType(Enum):
    Point = 0
    Line = 1
    LineLoop = 2
    PlaneSurface = 3
    SurfaceLoop = 4
    Volume = 5
    PhysicalVolume = 6
    # Point, Line, Line Loop, Plane Surface, Surface Loop, Volume, Physical Volume
    _index_list = [0, 0, 0, 0, 0, 0, 0]

    def get_next_index(self):
        index = GeoModuleType._index_list.value[self.value]
        index += 1
        GeoModuleType._index_list.value[self.value] = index
        # print('%s - %d' % (self, index))
        return index


class GeoModule:
    def __init__(self, module_type):
        self.module_type = module_type
        self.index = module_type.get_next_index()

    def geo_format(self):
        pass


class OriginalPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point(GeoModule):
    def __init__(self, x, y, z):
        super().__init__(GeoModuleType.Point)
        self.x = x
        self.y = y
        self.z = z

    def geo_format(self):
        return 'Point(%d) = {%f, %f, %s, %s};' % (self.index, self.x, self.y, self.z, MARK_MESH_SIZE)


class Line(GeoModule):
    def __init__(self, start_point, end_point):
        super().__init__(GeoModuleType.Line)
        self.start_point = start_point
        self.end_point = end_point

    def geo_format(self):
        return 'Line(%d) = {%d, %d};' % (self.index, self.start_point.index, self.end_point.index)


class LineLoop(GeoModule):
    def __init__(self, lines):
        super().__init__(GeoModuleType.LineLoop)
        self.lines = lines
        self.directions = [1 for line in self.lines]

    def geo_format(self):
        line_str = []
        for i, line in enumerate(self.lines):
            direction_index = line.index * self.directions[i]
            line_str.append(str(direction_index))
        return 'Line Loop(%d) = {%s};' % (self.index, ', '.join(line_str))


class PlaneSurface(GeoModule):
    def __init__(self, line_loop):
        super().__init__(GeoModuleType.PlaneSurface)
        self.line_loop = line_loop

    def geo_format(self):
        return 'Plane Surface(%d) = {%s};' % (self.index, self.line_loop.index)


class SurfaceLoop(GeoModule):
    def __init__(self, surfaces):
        super().__init__(GeoModuleType.SurfaceLoop)
        self.surfaces = surfaces

    def geo_format(self):
        surface_str = []
        for surface in self.surfaces:
            surface_str.append(str(surface.index))
        return 'Surface Loop(%d) = {%s};' % (self.index, ', '.join(surface_str))


class Volume(GeoModule):
    def __init__(self, surface_loop):
        super().__init__(GeoModuleType.Volume)
        self.surface_loop = surface_loop

    def geo_format(self):
        return 'Volume(%d) = {%s};' % (self.index, self.surface_loop.index)


class PhysicalVolume(GeoModule):
    def __init__(self, volume):
        super().__init__(GeoModuleType.PhysicalVolume)
        self.volume = volume

    def geo_format(self):
        return 'Physical Volume(%d) = {%s};' % (self.index, self.volume.index)


class CylinderType(Enum):
    Hard = ['0.0', MARK_HARD_HEIGHT]
    Soft = ['%s + %s' % (MARK_HARD_HEIGHT, MARK_SPACE_HEIGHT),
            '%s + %s + %s' % (MARK_HARD_HEIGHT, MARK_SPACE_HEIGHT, MARK_SOFT_HEIGHT)]


class Cylinder:
    def __init__(self, vertices):
        super().__init__()
        # crete point by vertices
        self.vertices = vertices
        point_list = []
        for vertice in vertices:
            point = OriginalPoint(vertice[0], vertice[1])
            point_list.append(point)
        self.hard_layer = self.create_physical(point_list, CylinderType.Hard)
        self.soft_layer = self.create_physical(point_list, CylinderType.Soft)

    def create_physical(self, points, c_type):
        original_point_length = len(points)
        # bottom points
        bottom_points = []
        for point in points:
            bottom_points.append(Point(point.x, point.y, c_type.value[0]))
        # top points
        top_points = []
        for point in points:
            top_points.append(Point(point.x, point.y, c_type.value[1]))
        # bottom surface
        bottom_surface = self.create_surface(bottom_points)
        # top surface
        top_surface = self.create_surface(top_points)
        # vertical lines
        vertical_lines = []
        for i in range(original_point_length):
            top_point = top_points[i]
            bottom_point = bottom_points[i]
            vertical_lines.append(Line(bottom_point, top_point))
        # vertical surfaces
        vertical_surfaces = []
        top_lines = top_surface.line_loop.lines
        bottom_lines = bottom_surface.line_loop.lines
        for i in range(original_point_length):
            top_line = top_lines[i]
            bottom_line = bottom_lines[i]
            left_line = vertical_lines[i]
            right_line = vertical_lines[(i+1) % original_point_length]
            line_loop = LineLoop([bottom_line, right_line, top_line, left_line])
            line_loop.directions = [1, 1, -1, -1]
            vertical_surfaces.append(PlaneSurface(line_loop))
        all_surface = []
        all_surface.extend(vertical_surfaces)
        all_surface.extend((bottom_surface, top_surface))
        # Surface Loop -> Volume -> Physical Volume
        surface_loop = SurfaceLoop(all_surface)
        volume = Volume(surface_loop)
        physical = PhysicalVolume(volume)
        return physical

    def create_surface(self, points):
        # create line
        line_list = []
        for i in range(len(points) - 1):
            line_list.append(Line(points[i], points[i+1]))
        line_list.append(Line(points[-1], points[0]))
        # create line loop
        line_loop = LineLoop(line_list)
        # create plane surface
        plane_surface = PlaneSurface(line_loop)
        return plane_surface


class Cube:
    def __init__(self, vertice_list):
        super().__init__()
        self.vertice_list = vertice_list
        self.cylinders = []
        for vertices in vertice_list:
            cylinder = Cylinder(vertices)
            self.cylinders.append(cylinder)

    def get_modules(self, physical):
        geo_modules = []
        volume = physical.volume
        surface_loop = volume.surface_loop
        top_surface = surface_loop.surfaces[-1]
        bottom_surface = surface_loop.surfaces[-2]
        # get points from top and bottom
        for line in bottom_surface.line_loop.lines:
            geo_modules.append(line.start_point)
        for line in top_surface.line_loop.lines:
            geo_modules.append(line.start_point)
        # get lines from top and bottom
        for line in bottom_surface.line_loop.lines:
            geo_modules.append(line)
        for line in top_surface.line_loop.lines:
            geo_modules.append(line)
        # get lines from vertical
        for i in range(len(surface_loop.surfaces) - 2):
            # left vertical line
            geo_modules.append(surface_loop.surfaces[i].line_loop.lines[-1])
        # get line_loop and surface
        for surface in surface_loop.surfaces:
            geo_modules.append(surface.line_loop)
            geo_modules.append(surface)
        geo_modules.append(surface_loop)
        geo_modules.append(volume)
        geo_modules.append(physical)
        return geo_modules

    def write(self):
        with open('test.geo', 'w', encoding='utf-8') as f:
            f.write('%s = %s; \n' % (MARK_MESH_SIZE, '2.0'))
            f.write('%s = %s; \n' % (MARK_HARD_HEIGHT, '6.0'))
            f.write('%s = %s; \n' % (MARK_SPACE_HEIGHT, '0.2'))
            f.write('%s = %s; \n' % (MARK_SOFT_HEIGHT, '6.0'))
            for cylinder in self.cylinders:
                modules = self.get_modules(cylinder.hard_layer)
                for geo_module in modules:
                    f.write('%s\n' % geo_module.geo_format())
            for cylinder in self.cylinders:
                modules = self.get_modules(cylinder.soft_layer)
                for geo_module in modules:
                    f.write('%s\n' % geo_module.geo_format())


def read_points(file_name='Point.txt'):
        region_point_list = []
        with open(file_name, 'r', encoding='utf-8') as f:
            first_line = True
            for line in f:
                if first_line:
                    first_line = False
                    continue
                point_list = []
                line_token = line.split(' ')
                for token in line_token:
                    if len(token) == 0:
                        continue
                    tokens = token.split(',')
                    point_list.append((float(tokens[0].strip()), float(tokens[1].strip())))
                region_point_list.append(point_list)
        return region_point_list


region_point_list = read_points()
cube = Cube(region_point_list)
cube.write()