#include as follow : execfile('pathto/DPO104.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
DPO104= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/DPO104.sph',
radii = [[3.2599999999999998, 3.6400000000000001, 2.3999999999999999, 2.3500000000000001, 3.73, 2.5, 2.8500000000000001, 2.52]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/DPO104.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'DPO104',
positions = [[(-2.5499999999999998, -5.3700000000000001, -14.6), (-4.4500000000000002, -8.9499999999999993, -7.8099999999999996), (-0.14999999999999999, 2.6299999999999999, -20.260000000000002), (-1.0, -2.0600000000000001, -20.289999999999999), (2.0600000000000001, -0.76000000000000001, -25.370000000000001), (1.52, 6.5099999999999998, -3.9300000000000002), (1.6100000000000001, 5.1500000000000004, -15.19), (2.2799999999999998, 7.4299999999999997, -9.9800000000000004)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(DPO104)