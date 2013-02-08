#include as follow : execfile('pathto/POP23.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP23= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP23.sph',
radii = [[3.0099999999999998, 1.27, 1.6100000000000001, 3.8900000000000001, 2.5899999999999999, 2.9199999999999999, 4.6399999999999997, 1.53]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP23.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'POP23',
positions = [[(-0.19, -0.35999999999999999, 23.199999999999999), (-6.9800000000000004, 5.2300000000000004, 4.8600000000000003), (-6.3600000000000003, 3.0, 7.6799999999999997), (3.4900000000000002, -1.9099999999999999, 17.82), (-3.1699999999999999, 2.8599999999999999, 12.15), (-2.25, 2.3999999999999999, 19.02), (6.5999999999999996, -1.97, 9.1600000000000001), (-0.68000000000000005, -3.6699999999999999, 22.710000000000001)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP23)