#include as follow : execfile('pathto/POP43.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP43= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP43.sph',
radii = [[1.8300000000000001, 2.0600000000000001, 2.48, 1.3100000000000001, 6.0800000000000001, 4.3399999999999999, 1.03, 3.2999999999999998]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP43.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, -1.0],
name = 'POP43',
positions = [[(-2.0, -4.9000000000000004, 22.649999999999999), (-1.05, -0.70999999999999996, 20.0), (1.23, 0.28000000000000003, 22.18), (1.73, -6.54, 23.359999999999999), (-1.24, 2.6499999999999999, 7.0199999999999996), (2.8100000000000001, 3.2999999999999998, 15.85), (-0.029999999999999999, -6.1799999999999997, 23.399999999999999), (-0.93999999999999995, 1.4399999999999999, 14.300000000000001)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP43)