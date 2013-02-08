#include as follow : execfile('pathto/LPO125.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
LPO125= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/LPO125.sph',
radii = [[1.9099999999999999, 4.9299999999999997, 2.3900000000000001, 1.5700000000000001, 2.3599999999999999, 2.5600000000000001, 3.4199999999999999, 4.5300000000000002]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/LPO125.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'LPO125',
positions = [[(-0.34000000000000002, 10.369999999999999, 12.890000000000001), (-3.7200000000000002, -8.5700000000000003, 6.2599999999999998), (0.68999999999999995, 7.5999999999999996, 16.77), (0.20000000000000001, 10.44, 8.5299999999999994), (0.52000000000000002, -0.67000000000000004, 24.239999999999998), (1.47, 2.29, 18.920000000000002), (2.6499999999999999, -1.9299999999999999, 21.609999999999999), (-0.31, -3.77, 14.77)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(LPO125)