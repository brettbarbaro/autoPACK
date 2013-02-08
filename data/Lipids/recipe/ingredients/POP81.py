#include as follow : execfile('pathto/POP81.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP81= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP81.sph',
radii = [[2.5299999999999998, 1.29, 3.9300000000000002, 3.4100000000000001, 2.4100000000000001, 2.9500000000000002, 1.27, 3.5099999999999998]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP81.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, -1.0],
name = 'POP81',
positions = [[(-8.7100000000000009, -1.45, -2.0), (5.5999999999999996, -2.3700000000000001, -2.6499999999999999), (-4.1200000000000001, -0.76000000000000001, -15.630000000000001), (2.6899999999999999, -0.56999999999999995, -14.69), (5.8899999999999997, 0.02, -9.1799999999999997), (-5.5, -1.3400000000000001, -7.9000000000000004), (6.5499999999999998, 0.16, -4.46), (2.0600000000000001, 2.3300000000000001, -18.690000000000001)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP81)