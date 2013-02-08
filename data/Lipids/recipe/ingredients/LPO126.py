#include as follow : execfile('pathto/LPO126.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
LPO126= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/LPO126.sph',
radii = [[3.77, 3.1499999999999999, 3.1099999999999999, 2.5800000000000001, 3.1499999999999999, 1.24, 2.98, 2.5]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/LPO126.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'LPO126',
positions = [[(-1.97, 2.02, 18.43), (0.44, -0.35999999999999999, 14.68), (-1.3600000000000001, 1.47, 9.6199999999999992), (-2.0299999999999998, -0.67000000000000004, -2.27), (3.8100000000000001, -4.4299999999999997, 1.9399999999999999), (3.6000000000000001, -1.3500000000000001, 12.210000000000001), (-2.0299999999999998, 1.52, 2.9900000000000002), (3.5099999999999998, -1.0600000000000001, 7.6500000000000004)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(LPO126)