#include as follow : execfile('pathto/DPO106.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
DPO106= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/DPO106.sph',
radii = [[1.3200000000000001, 0.76000000000000001, 3.9100000000000001, 5.0700000000000003, 4.0700000000000003, 2.3399999999999999, 1.8799999999999999, 1.26]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/DPO106.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, -1.0],
name = 'DPO106',
positions = [[(-3.3900000000000001, -2.48, 6.54), (-3.9399999999999999, -1.73, 9.25), (2.5800000000000001, 3.77, 3.7400000000000002), (3.2799999999999998, 2.1299999999999999, 13.76), (0.71999999999999997, -0.56999999999999995, 21.190000000000001), (-2.9900000000000002, -3.1899999999999999, 15.890000000000001), (-5.6900000000000004, -2.6600000000000001, 11.73), (-3.5299999999999998, -1.22, 2.96)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(DPO106)