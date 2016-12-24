mesh_size = 2.0; 
hard_height = 6.0; 
space_height = 0.2; 
soft_height = 4.0;
Point(1) = {-2.500000, 0.000000, 0.0, mesh_size};
Point(2) = {2.500000, 0.000000, 0.0, mesh_size};
Point(3) = {2.500000, 2.500000, 0.0, mesh_size};
Point(4) = {-2.500000, 2.500000, 0.0, mesh_size};
Point(5) = {-2.500000, 0.000000, hard_height, mesh_size};
Point(6) = {2.500000, 0.000000, hard_height, mesh_size};
Point(7) = {2.500000, 2.500000, hard_height, mesh_size};
Point(8) = {-2.500000, 2.500000, hard_height, mesh_size};
Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 1};
Line(5) = {5, 6};
Line(6) = {6, 7};
Line(7) = {7, 8};
Line(8) = {8, 5};
Line(9) = {1, 5};
Line(10) = {2, 6};
Line(11) = {3, 7};
Line(12) = {4, 8};
Line Loop(3) = {1, 10, -5, -9};
Plane Surface(3) = {3};
Line Loop(4) = {2, 11, -6, -10};
Plane Surface(4) = {4};
Line Loop(5) = {3, 12, -7, -11};
Plane Surface(5) = {5};
Line Loop(6) = {4, 9, -8, -12};
Plane Surface(6) = {6};
Line Loop(1) = {1, 2, 3, 4};
Plane Surface(1) = {1};
Line Loop(2) = {5, 6, 7, 8};
Plane Surface(2) = {2};
Surface Loop(1) = {3, 4, 5, 6, 1, 2};
Volume(1) = {1};
Physical Volume(1) = {1};
Point(9) = {-2.500000, 0.000000, hard_height + space_height, mesh_size};
Point(10) = {2.500000, 0.000000, hard_height + space_height, mesh_size};
Point(11) = {2.500000, 2.500000, hard_height + space_height, mesh_size};
Point(12) = {-2.500000, 2.500000, hard_height + space_height, mesh_size};
Point(13) = {-2.500000, 0.000000, hard_height + space_height + soft_height, mesh_size};
Point(14) = {2.500000, 0.000000, hard_height + space_height + soft_height, mesh_size};
Point(15) = {2.500000, 2.500000, hard_height + space_height + soft_height, mesh_size};
Point(16) = {-2.500000, 2.500000, hard_height + space_height + soft_height, mesh_size};
Line(13) = {9, 10};
Line(14) = {10, 11};
Line(15) = {11, 12};
Line(16) = {12, 9};
Line(17) = {13, 14};
Line(18) = {14, 15};
Line(19) = {15, 16};
Line(20) = {16, 13};
Line(21) = {9, 13};
Line(22) = {10, 14};
Line(23) = {11, 15};
Line(24) = {12, 16};
Line Loop(9) = {13, 22, -17, -21};
Plane Surface(9) = {9};
Line Loop(10) = {14, 23, -18, -22};
Plane Surface(10) = {10};
Line Loop(11) = {15, 24, -19, -23};
Plane Surface(11) = {11};
Line Loop(12) = {16, 21, -20, -24};
Plane Surface(12) = {12};
Line Loop(7) = {13, 14, 15, 16};
Plane Surface(7) = {7};
Line Loop(8) = {17, 18, 19, 20};
Plane Surface(8) = {8};
Surface Loop(2) = {9, 10, 11, 12, 7, 8};
Volume(2) = {2};
Physical Volume(2) = {2};
