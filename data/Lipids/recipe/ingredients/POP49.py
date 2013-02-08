#include as follow : execfile('pathto/POP49.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP49= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP49.sph',
radii = [[2.2200000000000002, 2.8599999999999999, 2.4399999999999999, 1.5800000000000001, 1.29, 3.8300000000000001, 4.54, 2.6600000000000001]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP49.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, -1.0],
name = 'POP49',
positions = [[(-5.4299999999999997, -2.3100000000000001, -9.4399999999999995), (-2.9500000000000002, -0.40999999999999998, -18.010000000000002), (-5.7699999999999996, -3.79, -4.3399999999999999), (-5.4400000000000004, -1.3700000000000001, -14.039999999999999), (6.8799999999999999, 2.1699999999999999, -2.1800000000000002), (3.9700000000000002, 0.69999999999999996, -14.539999999999999), (0.77000000000000002, 0.78000000000000003, -22.420000000000002), (5.79, 2.4100000000000001, -7.2300000000000004)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP49)