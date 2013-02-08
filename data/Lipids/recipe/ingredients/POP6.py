#include as follow : execfile('pathto/POP6.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP6= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP6.sph',
radii = [[2.4700000000000002, 2.8100000000000001, 1.8700000000000001, 3.54, 2.8799999999999999, 2.3799999999999999, 3.1299999999999999, 3.0099999999999998]],
cutoff_boundary = 0,
Type = 'MultiSphere',
cutoff_surface = 0,
gradient = '',
jitterMax = [0.5, 0.5, 0.10000000000000001],
packingPriority = 0,
rotAxis = [0.0, 2.0, 1.0],
nbJitter = 5,
molarity = 1.0,
rotRange = 6.2831,
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP6.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'POP6',
positions = [[(5.1799999999999997, 0.68000000000000005, -11.529999999999999), (-0.78000000000000003, 1.01, -22.66), (5.4800000000000004, -1.9099999999999999, -7.6100000000000003), (-4.3399999999999999, 1.1699999999999999, -2.8599999999999999), (1.6699999999999999, 1.45, -17.030000000000001), (-2.9900000000000002, 0.26000000000000001, -16.25), (4.4199999999999999, -3.8300000000000001, -2.4199999999999999), (-4.8499999999999996, -0.63, -9.8800000000000008)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP6)