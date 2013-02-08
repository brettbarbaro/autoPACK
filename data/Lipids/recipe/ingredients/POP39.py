#include as follow : execfile('pathto/POP39.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP39= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP39.sph',
radii = [[1.9099999999999999, 2.71, 2.3500000000000001, 1.3200000000000001, 1.8700000000000001, 1.97, 5.54, 4.0499999999999998]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP39.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'POP39',
positions = [[(-5.6900000000000004, 5.4800000000000004, 8.1099999999999994), (-1.25, -3.1200000000000001, 23.52), (-1.6000000000000001, -0.14000000000000001, 19.129999999999999), (-4.4000000000000004, 5.1100000000000003, 11.869999999999999), (-3.0499999999999998, 2.71, 14.699999999999999), (-6.2699999999999996, 5.5300000000000002, 3.1499999999999999), (6.0, -2.6299999999999999, 8.6799999999999997), (4.21, -0.63, 18.5)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP39)