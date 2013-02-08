#include as follow : execfile('pathto/POP47.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP47= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP47.sph',
radii = [[2.6499999999999999, 2.4500000000000002, 2.8399999999999999, 2.48, 2.3100000000000001, 4.4199999999999999, 2.4199999999999999, 2.5600000000000001]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP47.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, -1.0],
name = 'POP47',
positions = [[(0.56999999999999995, -1.3100000000000001, -18.760000000000002), (5.0999999999999996, 0.40999999999999998, -5.2000000000000002), (2.1099999999999999, 0.76000000000000001, -22.73), (5.4000000000000004, -1.3200000000000001, -11.06), (-2.5299999999999998, 0.79000000000000004, -17.84), (-6.1399999999999997, 0.97999999999999998, -4.6500000000000004), (3.9900000000000002, -2.2599999999999998, -16.100000000000001), (-4.6799999999999997, 0.070000000000000007, -12.119999999999999)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP47)