#include as follow : execfile('pathto/POP37.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP37= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP37.sph',
radii = [[4.0499999999999998, 2.0, 0.94999999999999996, 3.0099999999999998, 2.5899999999999999, 4.3300000000000001, 0.77000000000000002, 1.5600000000000001]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP37.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'POP37',
positions = [[(0.14999999999999999, 1.6899999999999999, 17.690000000000001), (-1.1000000000000001, -0.93000000000000005, 22.120000000000001), (-1.79, -4.6699999999999999, 21.629999999999999), (2.6000000000000001, -1.8700000000000001, 3.71), (-0.91000000000000003, 1.48, 5.8399999999999999), (0.76000000000000001, -0.42999999999999999, 11.34), (-2.98, -3.46, 22.59), (-0.45000000000000001, 4.0099999999999998, 1.9399999999999999)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP37)