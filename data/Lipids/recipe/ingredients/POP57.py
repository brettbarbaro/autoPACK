#include as follow : execfile('pathto/POP57.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP57= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP57.sph',
radii = [[2.8100000000000001, 3.7999999999999998, 3.6200000000000001, 2.9300000000000002, 2.0499999999999998, 2.3599999999999999, 1.9099999999999999, 2.8999999999999999]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP57.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, -1.0],
name = 'POP57',
positions = [[(-0.46000000000000002, -0.56999999999999995, 19.280000000000001), (-6.6100000000000003, -2.04, 5.0700000000000003), (-3.3599999999999999, -2.1499999999999999, 12.539999999999999), (6.8499999999999996, 2.5699999999999998, 3.4100000000000001), (3.6299999999999999, 1.4099999999999999, 19.010000000000002), (5.2699999999999996, 1.51, 9.0700000000000003), (4.71, 2.02, 14.23), (-3.1000000000000001, -0.42999999999999999, 21.440000000000001)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP57)