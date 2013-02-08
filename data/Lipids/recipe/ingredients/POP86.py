#include as follow : execfile('pathto/POP86.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP86= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP86.sph',
radii = [[0.76000000000000001, 1.3, 2.5299999999999998, 4.8200000000000003, 2.8100000000000001, 3.04, 2.3700000000000001, 4.7300000000000004]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP86.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, -1.0],
name = 'POP86',
positions = [[(-7.6399999999999997, 6.71, 3.2999999999999998), (-7.21, 5.5, 5.79), (-5.9800000000000004, 4.8899999999999997, 10.130000000000001), (4.8899999999999997, -0.20000000000000001, 16.670000000000002), (-0.070000000000000007, 0.77000000000000002, 18.890000000000001), (3.2000000000000002, -3.0099999999999998, 22.649999999999999), (-4.4100000000000001, 1.8100000000000001, 14.529999999999999), (0.77000000000000002, -3.4300000000000002, 8.4299999999999997)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP86)