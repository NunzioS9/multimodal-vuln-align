Epoch 1/12
-----
train Loss: 2.5908 Acc: 0.1622
train Align Loss: 2.6527 Class Loss: 2.5642
train Top-3 Acc: 0.3355
train Metrics per class:
  CWE-119: {'precision': 0.174, 'recall': 0.091, 'f1': 0.119, 'support': 309}
  CWE-125: {'precision': 0.174, 'recall': 0.171, 'f1': 0.173, 'support': 315}
  CWE-190: {'precision': 0.118, 'recall': 0.123, 'f1': 0.121, 'support': 292}
  CWE-20: {'precision': 0.09, 'recall': 0.31, 'f1': 0.14, 'support': 294}
  CWE-200: {'precision': 0.09, 'recall': 0.02, 'f1': 0.033, 'support': 296}
  CWE-284: {'precision': 0.131, 'recall': 0.159, 'f1': 0.144, 'support': 301}
  CWE-362: {'precision': 0.071, 'recall': 0.071, 'f1': 0.071, 'support': 282}
  CWE-404: {'precision': 0.247, 'recall': 0.42, 'f1': 0.311, 'support': 283}
  CWE-415: {'precision': 0.24, 'recall': 0.163, 'f1': 0.194, 'support': 289}
  CWE-416: {'precision': 0.02, 'recall': 0.004, 'f1': 0.006, 'support': 273}
  CWE-476: {'precision': 0.147, 'recall': 0.083, 'f1': 0.106, 'support': 312}
  CWE-59: {'precision': 0.393, 'recall': 0.249, 'f1': 0.305, 'support': 301}
  CWE-732: {'precision': 0.185, 'recall': 0.294, 'f1': 0.227, 'support': 269}
  CWE-787: {'precision': 0.154, 'recall': 0.048, 'f1': 0.073, 'support': 294}
  CWE-79: {'precision': 0.262, 'recall': 0.256, 'f1': 0.259, 'support': 242}
val Loss: 2.5194 Acc: 0.1234
val Align Loss: 2.6144 Class Loss: 2.4786
val Top-3 Acc: 0.3648
val Metrics per class:
  CWE-119: {'precision': 0.5, 'recall': 0.063, 'f1': 0.111, 'support': 319}
  CWE-125: {'precision': 0.302, 'recall': 0.448, 'f1': 0.361, 'support': 87}
  CWE-190: {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'support': 45}
  CWE-20: {'precision': 0.25, 'recall': 0.012, 'f1': 0.024, 'support': 161}
  CWE-200: {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'support': 75}
  CWE-284: {'precision': 0.152, 'recall': 0.4, 'f1': 0.22, 'support': 30}
  CWE-362: {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'support': 43}
  CWE-404: {'precision': 0.113, 'recall': 0.929, 'f1': 0.202, 'support': 14}
  CWE-415: {'precision': 0.035, 'recall': 0.667, 'f1': 0.067, 'support': 15}
  CWE-416: {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'support': 55}
  CWE-476: {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'support': 40}
  CWE-59: {'precision': 0.179, 'recall': 1.0, 'f1': 0.303, 'support': 5}
  CWE-732: {'precision': 0.066, 'recall': 0.625, 'f1': 0.119, 'support': 8}
  CWE-787: {'precision': 0.038, 'recall': 0.08, 'f1': 0.051, 'support': 25}
  CWE-79: {'precision': 0.067, 'recall': 0.7, 'f1': 0.122, 'support': 10}
New best val acc: 0.1234, saving model.
test Loss: 2.5452 Acc: 0.1274
test Align Loss: 2.6554 Class Loss: 2.4980
test Top-3 Acc: 0.3266
test Metrics per class:
  CWE-119: {'precision': 0.465, 'recall': 0.062, 'f1': 0.109, 'support': 323}
  CWE-125: {'precision': 0.324, 'recall': 0.536, 'f1': 0.404, 'support': 84}
  CWE-190: {'precision': 1.0, 'recall': 0.022, 'f1': 0.043, 'support': 45}
  CWE-20: {'precision': 0.667, 'recall': 0.044, 'f1': 0.082, 'support': 182}
  CWE-200: {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'support': 80}
  CWE-284: {'precision': 0.214, 'recall': 0.375, 'f1': 0.273, 'support': 32}
  CWE-362: {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'support': 37}
  CWE-404: {'precision': 0.032, 'recall': 0.8, 'f1': 0.062, 'support': 5}
  CWE-415: {'precision': 0.027, 'recall': 0.889, 'f1': 0.052, 'support': 9}
  CWE-416: {'precision': 0.333, 'recall': 0.021, 'f1': 0.039, 'support': 48}
  CWE-476: {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'support': 37}
  CWE-59: {'precision': 0.208, 'recall': 0.556, 'f1': 0.303, 'support': 9}
  CWE-732: {'precision': 0.091, 'recall': 0.636, 'f1': 0.159, 'support': 11}
  CWE-787: {'precision': 0.064, 'recall': 0.115, 'f1': 0.082, 'support': 26}
  CWE-79: {'precision': 0.05, 'recall': 0.833, 'f1': 0.093, 'support': 6}

Epoch 2/12
-----
train Loss: 1.5610 Acc: 0.5480
train Align Loss: 1.6938 Class Loss: 1.5040
train Top-3 Acc: 0.7454
train Metrics per class:
  CWE-119: {'precision': 0.358, 'recall': 0.096, 'f1': 0.151, 'support': 250}
  CWE-125: {'precision': 0.368, 'recall': 0.495, 'f1': 0.422, 'support': 293}
  CWE-190: {'precision': 0.509, 'recall': 0.55, 'f1': 0.529, 'support': 309}
  CWE-20: {'precision': 0.294, 'recall': 0.12, 'f1': 0.171, 'support': 249}
  CWE-200: {'precision': 0.263, 'recall': 0.111, 'f1': 0.156, 'support': 270}
  CWE-284: {'precision': 0.575, 'recall': 0.613, 'f1': 0.594, 'support': 305}
  CWE-362: {'precision': 0.365, 'recall': 0.449, 'f1': 0.402, 'support': 294}
  CWE-404: {'precision': 0.793, 'recall': 0.975, 'f1': 0.875, 'support': 319}
  CWE-415: {'precision': 0.669, 'recall': 0.792, 'f1': 0.725, 'support': 312}
  CWE-416: {'precision': 0.187, 'recall': 0.047, 'f1': 0.075, 'support': 257}
  CWE-476: {'precision': 0.412, 'recall': 0.421, 'f1': 0.417, 'support': 311}
  CWE-59: {'precision': 0.849, 'recall': 0.986, 'f1': 0.912, 'support': 290}
  CWE-732: {'precision': 0.743, 'recall': 0.884, 'f1': 0.807, 'support': 310}
  CWE-787: {'precision': 0.363, 'recall': 0.463, 'f1': 0.407, 'support': 294}
  CWE-79: {'precision': 0.628, 'recall': 0.934, 'f1': 0.751, 'support': 289}
val Loss: 2.0971 Acc: 0.3552
val Align Loss: 2.4914 Class Loss: 1.9282
val Top-3 Acc: 0.6878
val Metrics per class:
  CWE-119: {'precision': 0.698, 'recall': 0.354, 'f1': 0.47, 'support': 319}
  CWE-125: {'precision': 0.508, 'recall': 0.356, 'f1': 0.419, 'support': 87}
  CWE-190: {'precision': 0.464, 'recall': 0.578, 'f1': 0.515, 'support': 45}
  CWE-20: {'precision': 0.363, 'recall': 0.205, 'f1': 0.262, 'support': 161}
  CWE-200: {'precision': 0.214, 'recall': 0.04, 'f1': 0.067, 'support': 75}
  CWE-284: {'precision': 0.253, 'recall': 0.7, 'f1': 0.372, 'support': 30}
  CWE-362: {'precision': 0.194, 'recall': 0.581, 'f1': 0.291, 'support': 43}
  CWE-404: {'precision': 0.737, 'recall': 1.0, 'f1': 0.848, 'support': 14}
  CWE-415: {'precision': 0.474, 'recall': 0.6, 'f1': 0.529, 'support': 15}
  CWE-416: {'precision': 0.176, 'recall': 0.109, 'f1': 0.135, 'support': 55}
  CWE-476: {'precision': 0.21, 'recall': 0.55, 'f1': 0.303, 'support': 40}
  CWE-59: {'precision': 0.308, 'recall': 0.8, 'f1': 0.444, 'support': 5}
  CWE-732: {'precision': 0.375, 'recall': 0.75, 'f1': 0.5, 'support': 8}
  CWE-787: {'precision': 0.117, 'recall': 0.48, 'f1': 0.187, 'support': 25}
  CWE-79: {'precision': 0.222, 'recall': 0.6, 'f1': 0.324, 'support': 10}
New best val acc: 0.3552, saving model.
test Loss: 2.0925 Acc: 0.3298
test Align Loss: 2.4797 Class Loss: 1.9265
test Top-3 Acc: 0.6692
test Metrics per class:
  CWE-119: {'precision': 0.612, 'recall': 0.279, 'f1': 0.383, 'support': 323}
  CWE-125: {'precision': 0.565, 'recall': 0.464, 'f1': 0.51, 'support': 84}
  CWE-190: {'precision': 0.5, 'recall': 0.533, 'f1': 0.516, 'support': 45}
  CWE-20: {'precision': 0.407, 'recall': 0.181, 'f1': 0.251, 'support': 182}
  CWE-200: {'precision': 0.375, 'recall': 0.075, 'f1': 0.125, 'support': 80}
  CWE-284: {'precision': 0.2, 'recall': 0.562, 'f1': 0.295, 'support': 32}
  CWE-362: {'precision': 0.169, 'recall': 0.595, 'f1': 0.263, 'support': 37}
  CWE-404: {'precision': 0.5, 'recall': 1.0, 'f1': 0.667, 'support': 5}
  CWE-415: {'precision': 0.333, 'recall': 0.778, 'f1': 0.467, 'support': 9}
  CWE-416: {'precision': 0.2, 'recall': 0.125, 'f1': 0.154, 'support': 48}
  CWE-476: {'precision': 0.204, 'recall': 0.568, 'f1': 0.3, 'support': 37}
  CWE-59: {'precision': 0.214, 'recall': 0.333, 'f1': 0.261, 'support': 9}
  CWE-732: {'precision': 0.417, 'recall': 0.909, 'f1': 0.571, 'support': 11}
  CWE-787: {'precision': 0.173, 'recall': 0.731, 'f1': 0.279, 'support': 26}
  CWE-79: {'precision': 0.122, 'recall': 0.833, 'f1': 0.213, 'support': 6}

Epoch 3/12
-----
train Loss: 1.0454 Acc: 0.7123
train Align Loss: 1.2608 Class Loss: 0.9530
train Top-3 Acc: 0.8743
train Metrics per class:
  CWE-119: {'precision': 0.421, 'recall': 0.264, 'f1': 0.325, 'support': 303}
  CWE-125: {'precision': 0.612, 'recall': 0.637, 'f1': 0.624, 'support': 278}
  CWE-190: {'precision': 0.78, 'recall': 0.821, 'f1': 0.8, 'support': 285}
  CWE-20: {'precision': 0.386, 'recall': 0.328, 'f1': 0.355, 'support': 329}
  CWE-200: {'precision': 0.526, 'recall': 0.352, 'f1': 0.422, 'support': 284}
  CWE-284: {'precision': 0.799, 'recall': 0.861, 'f1': 0.829, 'support': 281}
  CWE-362: {'precision': 0.496, 'recall': 0.785, 'f1': 0.608, 'support': 311}
  CWE-404: {'precision': 0.99, 'recall': 1.0, 'f1': 0.995, 'support': 296}
  CWE-415: {'precision': 0.927, 'recall': 0.98, 'f1': 0.953, 'support': 297}
  CWE-416: {'precision': 0.496, 'recall': 0.209, 'f1': 0.294, 'support': 273}
  CWE-476: {'precision': 0.63, 'recall': 0.732, 'f1': 0.678, 'support': 284}
  CWE-59: {'precision': 0.973, 'recall': 1.0, 'f1': 0.987, 'support': 293}
  CWE-732: {'precision': 0.948, 'recall': 0.993, 'f1': 0.97, 'support': 294}
  CWE-787: {'precision': 0.598, 'recall': 0.767, 'f1': 0.672, 'support': 266}
  CWE-79: {'precision': 0.913, 'recall': 0.986, 'f1': 0.948, 'support': 278}
val Loss: 1.9798 Acc: 0.3830
val Align Loss: 2.3763 Class Loss: 1.8099
val Top-3 Acc: 0.7307
val Metrics per class:
  CWE-119: {'precision': 0.736, 'recall': 0.21, 'f1': 0.327, 'support': 319}
  CWE-125: {'precision': 0.561, 'recall': 0.425, 'f1': 0.484, 'support': 87}
  CWE-190: {'precision': 0.446, 'recall': 0.556, 'f1': 0.495, 'support': 45}
  CWE-20: {'precision': 0.444, 'recall': 0.373, 'f1': 0.405, 'support': 161}
  CWE-200: {'precision': 0.242, 'recall': 0.427, 'f1': 0.309, 'support': 75}
  CWE-284: {'precision': 0.5, 'recall': 0.667, 'f1': 0.571, 'support': 30}
  CWE-362: {'precision': 0.345, 'recall': 0.465, 'f1': 0.396, 'support': 43}
  CWE-404: {'precision': 0.778, 'recall': 1.0, 'f1': 0.875, 'support': 14}
  CWE-415: {'precision': 0.471, 'recall': 0.533, 'f1': 0.5, 'support': 15}
  CWE-416: {'precision': 0.269, 'recall': 0.327, 'f1': 0.295, 'support': 55}
  CWE-476: {'precision': 0.169, 'recall': 0.675, 'f1': 0.27, 'support': 40}
  CWE-59: {'precision': 0.6, 'recall': 0.6, 'f1': 0.6, 'support': 5}
  CWE-732: {'precision': 0.462, 'recall': 0.75, 'f1': 0.571, 'support': 8}
  CWE-787: {'precision': 0.219, 'recall': 0.56, 'f1': 0.315, 'support': 25}
  CWE-79: {'precision': 0.6, 'recall': 0.6, 'f1': 0.6, 'support': 10}
New best val acc: 0.3830, saving model.
test Loss: 1.9407 Acc: 0.3865
test Align Loss: 2.3319 Class Loss: 1.7730
test Top-3 Acc: 0.7527
test Metrics per class:
  CWE-119: {'precision': 0.74, 'recall': 0.229, 'f1': 0.35, 'support': 323}
  CWE-125: {'precision': 0.569, 'recall': 0.44, 'f1': 0.497, 'support': 84}
  CWE-190: {'precision': 0.49, 'recall': 0.556, 'f1': 0.521, 'support': 45}
  CWE-20: {'precision': 0.466, 'recall': 0.302, 'f1': 0.367, 'support': 182}
  CWE-200: {'precision': 0.252, 'recall': 0.45, 'f1': 0.323, 'support': 80}
  CWE-284: {'precision': 0.476, 'recall': 0.625, 'f1': 0.541, 'support': 32}
  CWE-362: {'precision': 0.328, 'recall': 0.568, 'f1': 0.416, 'support': 37}
  CWE-404: {'precision': 0.571, 'recall': 0.8, 'f1': 0.667, 'support': 5}
  CWE-415: {'precision': 0.389, 'recall': 0.778, 'f1': 0.519, 'support': 9}
  CWE-416: {'precision': 0.346, 'recall': 0.375, 'f1': 0.36, 'support': 48}
  CWE-476: {'precision': 0.173, 'recall': 0.784, 'f1': 0.283, 'support': 37}
  CWE-59: {'precision': 0.375, 'recall': 0.333, 'f1': 0.353, 'support': 9}
  CWE-732: {'precision': 0.611, 'recall': 1.0, 'f1': 0.759, 'support': 11}
  CWE-787: {'precision': 0.235, 'recall': 0.615, 'f1': 0.34, 'support': 26}
  CWE-79: {'precision': 0.417, 'recall': 0.833, 'f1': 0.556, 'support': 6}

Epoch 4/12
-----
train Loss: 0.7752 Acc: 0.7994
train Align Loss: 1.0353 Class Loss: 0.6637
train Top-3 Acc: 0.9324
train Metrics per class:
  CWE-119: {'precision': 0.515, 'recall': 0.357, 'f1': 0.422, 'support': 294}
  CWE-125: {'precision': 0.703, 'recall': 0.708, 'f1': 0.705, 'support': 291}
  CWE-190: {'precision': 0.877, 'recall': 0.877, 'f1': 0.877, 'support': 285}
  CWE-20: {'precision': 0.537, 'recall': 0.388, 'f1': 0.45, 'support': 299}
  CWE-200: {'precision': 0.575, 'recall': 0.609, 'f1': 0.591, 'support': 284}
  CWE-284: {'precision': 0.905, 'recall': 0.958, 'f1': 0.931, 'support': 287}
  CWE-362: {'precision': 0.647, 'recall': 0.726, 'f1': 0.684, 'support': 252}
  CWE-404: {'precision': 1.0, 'recall': 1.0, 'f1': 1.0, 'support': 311}
  CWE-415: {'precision': 0.946, 'recall': 0.971, 'f1': 0.958, 'support': 309}
  CWE-416: {'precision': 0.594, 'recall': 0.644, 'f1': 0.618, 'support': 295}
  CWE-476: {'precision': 0.794, 'recall': 0.859, 'f1': 0.825, 'support': 305}
  CWE-59: {'precision': 0.993, 'recall': 1.0, 'f1': 0.996, 'support': 273}
  CWE-732: {'precision': 0.986, 'recall': 1.0, 'f1': 0.993, 'support': 280}
  CWE-787: {'precision': 0.796, 'recall': 0.89, 'f1': 0.84, 'support': 290}
  CWE-79: {'precision': 0.974, 'recall': 1.0, 'f1': 0.987, 'support': 297}
val Loss: 1.7820 Acc: 0.4925
val Align Loss: 2.3462 Class Loss: 1.5402
val Top-3 Acc: 0.8101
val Metrics per class:
  CWE-119: {'precision': 0.679, 'recall': 0.458, 'f1': 0.547, 'support': 319}
  CWE-125: {'precision': 0.489, 'recall': 0.517, 'f1': 0.503, 'support': 87}
  CWE-190: {'precision': 0.553, 'recall': 0.578, 'f1': 0.565, 'support': 45}
  CWE-20: {'precision': 0.365, 'recall': 0.565, 'f1': 0.444, 'support': 161}
  CWE-200: {'precision': 0.396, 'recall': 0.48, 'f1': 0.434, 'support': 75}
  CWE-284: {'precision': 0.7, 'recall': 0.7, 'f1': 0.7, 'support': 30}
  CWE-362: {'precision': 0.45, 'recall': 0.419, 'f1': 0.434, 'support': 43}
  CWE-404: {'precision': 0.824, 'recall': 1.0, 'f1': 0.903, 'support': 14}
  CWE-415: {'precision': 0.538, 'recall': 0.467, 'f1': 0.5, 'support': 15}
  CWE-416: {'precision': 0.538, 'recall': 0.127, 'f1': 0.206, 'support': 55}
  CWE-476: {'precision': 0.344, 'recall': 0.525, 'f1': 0.416, 'support': 40}
  CWE-59: {'precision': 0.667, 'recall': 0.4, 'f1': 0.5, 'support': 5}
  CWE-732: {'precision': 0.667, 'recall': 0.75, 'f1': 0.706, 'support': 8}
  CWE-787: {'precision': 0.325, 'recall': 0.52, 'f1': 0.4, 'support': 25}
  CWE-79: {'precision': 0.5, 'recall': 0.6, 'f1': 0.545, 'support': 10}
New best val acc: 0.4925, saving model.
test Loss: 1.7054 Acc: 0.5300
test Align Loss: 2.2911 Class Loss: 1.4543
test Top-3 Acc: 0.8373
test Metrics per class:
  CWE-119: {'precision': 0.723, 'recall': 0.502, 'f1': 0.592, 'support': 323}
  CWE-125: {'precision': 0.612, 'recall': 0.619, 'f1': 0.615, 'support': 84}
  CWE-190: {'precision': 0.651, 'recall': 0.622, 'f1': 0.636, 'support': 45}
  CWE-20: {'precision': 0.41, 'recall': 0.566, 'f1': 0.476, 'support': 182}
  CWE-200: {'precision': 0.357, 'recall': 0.375, 'f1': 0.366, 'support': 80}
  CWE-284: {'precision': 0.618, 'recall': 0.656, 'f1': 0.636, 'support': 32}
  CWE-362: {'precision': 0.425, 'recall': 0.459, 'f1': 0.442, 'support': 37}
  CWE-404: {'precision': 0.571, 'recall': 0.8, 'f1': 0.667, 'support': 5}
  CWE-415: {'precision': 0.467, 'recall': 0.778, 'f1': 0.583, 'support': 9}
  CWE-416: {'precision': 0.714, 'recall': 0.312, 'f1': 0.435, 'support': 48}
  CWE-476: {'precision': 0.444, 'recall': 0.649, 'f1': 0.527, 'support': 37}
  CWE-59: {'precision': 0.429, 'recall': 0.333, 'f1': 0.375, 'support': 9}
  CWE-732: {'precision': 0.588, 'recall': 0.909, 'f1': 0.714, 'support': 11}
  CWE-787: {'precision': 0.385, 'recall': 0.577, 'f1': 0.462, 'support': 26}
  CWE-79: {'precision': 0.308, 'recall': 0.667, 'f1': 0.421, 'support': 6}

Epoch 5/12
-----
train Loss: 0.6234 Acc: 0.8497
train Align Loss: 0.9162 Class Loss: 0.4980
train Top-3 Acc: 0.9639
train Metrics per class:
  CWE-119: {'precision': 0.532, 'recall': 0.405, 'f1': 0.46, 'support': 264}
  CWE-125: {'precision': 0.755, 'recall': 0.731, 'f1': 0.743, 'support': 283}
  CWE-190: {'precision': 0.936, 'recall': 0.927, 'f1': 0.931, 'support': 286}
  CWE-20: {'precision': 0.547, 'recall': 0.416, 'f1': 0.473, 'support': 279}
  CWE-200: {'precision': 0.654, 'recall': 0.773, 'f1': 0.709, 'support': 313}
  CWE-284: {'precision': 0.948, 'recall': 0.975, 'f1': 0.961, 'support': 278}
  CWE-362: {'precision': 0.826, 'recall': 0.858, 'f1': 0.842, 'support': 288}
  CWE-404: {'precision': 0.997, 'recall': 1.0, 'f1': 0.998, 'support': 331}
  CWE-415: {'precision': 0.965, 'recall': 0.987, 'f1': 0.976, 'support': 310}
  CWE-416: {'precision': 0.74, 'recall': 0.764, 'f1': 0.752, 'support': 301}
  CWE-476: {'precision': 0.845, 'recall': 0.921, 'f1': 0.881, 'support': 290}
  CWE-59: {'precision': 0.997, 'recall': 1.0, 'f1': 0.998, 'support': 285}
  CWE-732: {'precision': 0.993, 'recall': 1.0, 'f1': 0.997, 'support': 302}
  CWE-787: {'precision': 0.879, 'recall': 0.929, 'f1': 0.903, 'support': 282}
  CWE-79: {'precision': 0.989, 'recall': 1.0, 'f1': 0.994, 'support': 260}
val Loss: 1.9089 Acc: 0.4807
val Align Loss: 2.4361 Class Loss: 1.6830
val Top-3 Acc: 0.7908
val Metrics per class:
  CWE-119: {'precision': 0.697, 'recall': 0.426, 'f1': 0.529, 'support': 319}
  CWE-125: {'precision': 0.506, 'recall': 0.483, 'f1': 0.494, 'support': 87}
  CWE-190: {'precision': 0.424, 'recall': 0.622, 'f1': 0.505, 'support': 45}
  CWE-20: {'precision': 0.504, 'recall': 0.36, 'f1': 0.42, 'support': 161}
  CWE-200: {'precision': 0.386, 'recall': 0.52, 'f1': 0.443, 'support': 75}
  CWE-284: {'precision': 0.478, 'recall': 0.733, 'f1': 0.579, 'support': 30}
  CWE-362: {'precision': 0.4, 'recall': 0.465, 'f1': 0.43, 'support': 43}
  CWE-404: {'precision': 0.824, 'recall': 1.0, 'f1': 0.903, 'support': 14}
  CWE-415: {'precision': 0.526, 'recall': 0.667, 'f1': 0.588, 'support': 15}
  CWE-416: {'precision': 0.333, 'recall': 0.509, 'f1': 0.403, 'support': 55}
  CWE-476: {'precision': 0.432, 'recall': 0.475, 'f1': 0.452, 'support': 40}
  CWE-59: {'precision': 0.444, 'recall': 0.8, 'f1': 0.571, 'support': 5}
  CWE-732: {'precision': 0.857, 'recall': 0.75, 'f1': 0.8, 'support': 8}
  CWE-787: {'precision': 0.18, 'recall': 0.64, 'f1': 0.281, 'support': 25}
  CWE-79: {'precision': 0.857, 'recall': 0.6, 'f1': 0.706, 'support': 10}
test Loss: 1.8560 Acc: 0.4904
test Align Loss: 2.4141 Class Loss: 1.6168
test Top-3 Acc: 0.8158
test Metrics per class:
  CWE-119: {'precision': 0.713, 'recall': 0.393, 'f1': 0.507, 'support': 323}
  CWE-125: {'precision': 0.558, 'recall': 0.631, 'f1': 0.592, 'support': 84}
  CWE-190: {'precision': 0.492, 'recall': 0.644, 'f1': 0.558, 'support': 45}
  CWE-20: {'precision': 0.527, 'recall': 0.379, 'f1': 0.441, 'support': 182}
  CWE-200: {'precision': 0.373, 'recall': 0.475, 'f1': 0.418, 'support': 80}
  CWE-284: {'precision': 0.44, 'recall': 0.687, 'f1': 0.537, 'support': 32}
  CWE-362: {'precision': 0.417, 'recall': 0.541, 'f1': 0.471, 'support': 37}
  CWE-404: {'precision': 0.571, 'recall': 0.8, 'f1': 0.667, 'support': 5}
  CWE-415: {'precision': 0.437, 'recall': 0.778, 'f1': 0.56, 'support': 9}
  CWE-416: {'precision': 0.333, 'recall': 0.562, 'f1': 0.419, 'support': 48}
  CWE-476: {'precision': 0.479, 'recall': 0.622, 'f1': 0.541, 'support': 37}
  CWE-59: {'precision': 0.5, 'recall': 0.444, 'f1': 0.471, 'support': 9}
  CWE-732: {'precision': 1.0, 'recall': 0.909, 'f1': 0.952, 'support': 11}
  CWE-787: {'precision': 0.229, 'recall': 0.846, 'f1': 0.361, 'support': 26}
  CWE-79: {'precision': 0.6, 'recall': 0.5, 'f1': 0.545, 'support': 6}

Epoch 6/12
-----
train Loss: 0.5021 Acc: 0.8975
train Align Loss: 0.8333 Class Loss: 0.3601
train Top-3 Acc: 0.9784
train Metrics per class:
  CWE-119: {'precision': 0.692, 'recall': 0.575, 'f1': 0.628, 'support': 285}
  CWE-125: {'precision': 0.847, 'recall': 0.831, 'f1': 0.839, 'support': 307}
  CWE-190: {'precision': 0.953, 'recall': 0.939, 'f1': 0.946, 'support': 279}
  CWE-20: {'precision': 0.647, 'recall': 0.6, 'f1': 0.622, 'support': 305}
  CWE-200: {'precision': 0.741, 'recall': 0.777, 'f1': 0.759, 'support': 283}
  CWE-284: {'precision': 0.965, 'recall': 0.996, 'f1': 0.981, 'support': 278}
  CWE-362: {'precision': 0.869, 'recall': 0.928, 'f1': 0.898, 'support': 265}
  CWE-404: {'precision': 1.0, 'recall': 1.0, 'f1': 1.0, 'support': 281}
  CWE-415: {'precision': 0.981, 'recall': 0.991, 'f1': 0.986, 'support': 317}
  CWE-416: {'precision': 0.881, 'recall': 0.905, 'f1': 0.893, 'support': 294}
  CWE-476: {'precision': 0.907, 'recall': 0.95, 'f1': 0.928, 'support': 278}
  CWE-59: {'precision': 0.997, 'recall': 1.0, 'f1': 0.998, 'support': 296}
  CWE-732: {'precision': 0.993, 'recall': 1.0, 'f1': 0.997, 'support': 296}
  CWE-787: {'precision': 0.94, 'recall': 0.979, 'f1': 0.959, 'support': 289}
  CWE-79: {'precision': 1.0, 'recall': 1.0, 'f1': 1.0, 'support': 299}
val Loss: 1.7336 Acc: 0.5622
val Align Loss: 2.3741 Class Loss: 1.4590
val Top-3 Acc: 0.8391
val Metrics per class:
  CWE-119: {'precision': 0.623, 'recall': 0.636, 'f1': 0.629, 'support': 319}
  CWE-125: {'precision': 0.634, 'recall': 0.517, 'f1': 0.57, 'support': 87}
  CWE-190: {'precision': 0.542, 'recall': 0.578, 'f1': 0.559, 'support': 45}
  CWE-20: {'precision': 0.547, 'recall': 0.398, 'f1': 0.46, 'support': 161}
  CWE-200: {'precision': 0.409, 'recall': 0.627, 'f1': 0.495, 'support': 75}
  CWE-284: {'precision': 0.769, 'recall': 0.667, 'f1': 0.714, 'support': 30}
  CWE-362: {'precision': 0.6, 'recall': 0.349, 'f1': 0.441, 'support': 43}
  CWE-404: {'precision': 0.778, 'recall': 1.0, 'f1': 0.875, 'support': 14}
  CWE-415: {'precision': 0.5, 'recall': 0.533, 'f1': 0.516, 'support': 15}
  CWE-416: {'precision': 0.508, 'recall': 0.545, 'f1': 0.526, 'support': 55}
  CWE-476: {'precision': 0.449, 'recall': 0.55, 'f1': 0.494, 'support': 40}
  CWE-59: {'precision': 0.5, 'recall': 0.6, 'f1': 0.545, 'support': 5}
  CWE-732: {'precision': 1.0, 'recall': 0.75, 'f1': 0.857, 'support': 8}
  CWE-787: {'precision': 0.364, 'recall': 0.64, 'f1': 0.464, 'support': 25}
  CWE-79: {'precision': 0.833, 'recall': 0.5, 'f1': 0.625, 'support': 10}
New best val acc: 0.5622, saving model.
test Loss: 1.6423 Acc: 0.5782
test Align Loss: 2.3186 Class Loss: 1.3524
test Top-3 Acc: 0.8630
test Metrics per class:
  CWE-119: {'precision': 0.676, 'recall': 0.647, 'f1': 0.661, 'support': 323}
  CWE-125: {'precision': 0.679, 'recall': 0.631, 'f1': 0.654, 'support': 84}
  CWE-190: {'precision': 0.636, 'recall': 0.622, 'f1': 0.629, 'support': 45}
  CWE-20: {'precision': 0.602, 'recall': 0.407, 'f1': 0.485, 'support': 182}
  CWE-200: {'precision': 0.374, 'recall': 0.575, 'f1': 0.453, 'support': 80}
  CWE-284: {'precision': 0.647, 'recall': 0.687, 'f1': 0.667, 'support': 32}
  CWE-362: {'precision': 0.619, 'recall': 0.351, 'f1': 0.448, 'support': 37}
  CWE-404: {'precision': 0.556, 'recall': 1.0, 'f1': 0.714, 'support': 5}
  CWE-415: {'precision': 0.437, 'recall': 0.778, 'f1': 0.56, 'support': 9}
  CWE-416: {'precision': 0.414, 'recall': 0.5, 'f1': 0.453, 'support': 48}
  CWE-476: {'precision': 0.463, 'recall': 0.676, 'f1': 0.549, 'support': 37}
  CWE-59: {'precision': 0.571, 'recall': 0.444, 'f1': 0.5, 'support': 9}
  CWE-732: {'precision': 1.0, 'recall': 0.909, 'f1': 0.952, 'support': 11}
  CWE-787: {'precision': 0.386, 'recall': 0.654, 'f1': 0.486, 'support': 26}
  CWE-79: {'precision': 0.75, 'recall': 0.5, 'f1': 0.6, 'support': 6}

Epoch 7/12
-----
train Loss: 0.4433 Acc: 0.9187
train Align Loss: 0.7905 Class Loss: 0.2945
train Top-3 Acc: 0.9844
train Metrics per class:
  CWE-119: {'precision': 0.72, 'recall': 0.641, 'f1': 0.678, 'support': 301}
  CWE-125: {'precision': 0.886, 'recall': 0.853, 'f1': 0.869, 'support': 273}
  CWE-190: {'precision': 0.967, 'recall': 0.96, 'f1': 0.963, 'support': 273}
  CWE-20: {'precision': 0.73, 'recall': 0.639, 'f1': 0.681, 'support': 313}
  CWE-200: {'precision': 0.814, 'recall': 0.896, 'f1': 0.853, 'support': 288}
  CWE-284: {'precision': 0.989, 'recall': 1.0, 'f1': 0.995, 'support': 277}
  CWE-362: {'precision': 0.899, 'recall': 0.937, 'f1': 0.917, 'support': 284}
  CWE-404: {'precision': 1.0, 'recall': 1.0, 'f1': 1.0, 'support': 312}
  CWE-415: {'precision': 0.99, 'recall': 0.997, 'f1': 0.993, 'support': 292}
  CWE-416: {'precision': 0.876, 'recall': 0.919, 'f1': 0.897, 'support': 270}
  CWE-476: {'precision': 0.937, 'recall': 0.974, 'f1': 0.955, 'support': 305}
  CWE-59: {'precision': 1.0, 'recall': 1.0, 'f1': 1.0, 'support': 295}
  CWE-732: {'precision': 0.987, 'recall': 1.0, 'f1': 0.994, 'support': 307}
  CWE-787: {'precision': 0.965, 'recall': 0.989, 'f1': 0.977, 'support': 280}
  CWE-79: {'precision': 0.993, 'recall': 1.0, 'f1': 0.996, 'support': 282}
val Loss: 1.7796 Acc: 0.5461
val Align Loss: 2.3766 Class Loss: 1.5237
val Top-3 Acc: 0.8369
val Metrics per class:
  CWE-119: {'precision': 0.692, 'recall': 0.549, 'f1': 0.612, 'support': 319}
  CWE-125: {'precision': 0.573, 'recall': 0.54, 'f1': 0.556, 'support': 87}
  CWE-190: {'precision': 0.435, 'recall': 0.6, 'f1': 0.505, 'support': 45}
  CWE-20: {'precision': 0.413, 'recall': 0.59, 'f1': 0.486, 'support': 161}
  CWE-200: {'precision': 0.547, 'recall': 0.547, 'f1': 0.547, 'support': 75}
  CWE-284: {'precision': 0.714, 'recall': 0.667, 'f1': 0.69, 'support': 30}
  CWE-362: {'precision': 0.488, 'recall': 0.465, 'f1': 0.476, 'support': 43}
  CWE-404: {'precision': 0.824, 'recall': 1.0, 'f1': 0.903, 'support': 14}
  CWE-415: {'precision': 0.5, 'recall': 0.533, 'f1': 0.516, 'support': 15}
  CWE-416: {'precision': 0.459, 'recall': 0.309, 'f1': 0.37, 'support': 55}
  CWE-476: {'precision': 0.432, 'recall': 0.475, 'f1': 0.452, 'support': 40}
  CWE-59: {'precision': 0.75, 'recall': 0.6, 'f1': 0.667, 'support': 5}
  CWE-732: {'precision': 0.857, 'recall': 0.75, 'f1': 0.8, 'support': 8}
  CWE-787: {'precision': 0.429, 'recall': 0.48, 'f1': 0.453, 'support': 25}
  CWE-79: {'precision': 0.625, 'recall': 0.5, 'f1': 0.556, 'support': 10}
test Loss: 1.6402 Acc: 0.5846
test Align Loss: 2.2741 Class Loss: 1.3685
test Top-3 Acc: 0.8683
test Metrics per class:
  CWE-119: {'precision': 0.741, 'recall': 0.557, 'f1': 0.636, 'support': 323}
  CWE-125: {'precision': 0.598, 'recall': 0.655, 'f1': 0.625, 'support': 84}
  CWE-190: {'precision': 0.484, 'recall': 0.667, 'f1': 0.561, 'support': 45}
  CWE-20: {'precision': 0.507, 'recall': 0.626, 'f1': 0.56, 'support': 182}
  CWE-200: {'precision': 0.534, 'recall': 0.487, 'f1': 0.51, 'support': 80}
  CWE-284: {'precision': 0.7, 'recall': 0.656, 'f1': 0.677, 'support': 32}
  CWE-362: {'precision': 0.512, 'recall': 0.568, 'f1': 0.538, 'support': 37}
  CWE-404: {'precision': 0.571, 'recall': 0.8, 'f1': 0.667, 'support': 5}
  CWE-415: {'precision': 0.437, 'recall': 0.778, 'f1': 0.56, 'support': 9}
  CWE-416: {'precision': 0.48, 'recall': 0.5, 'f1': 0.49, 'support': 48}
  CWE-476: {'precision': 0.553, 'recall': 0.568, 'f1': 0.56, 'support': 37}
  CWE-59: {'precision': 0.333, 'recall': 0.222, 'f1': 0.267, 'support': 9}
  CWE-732: {'precision': 1.0, 'recall': 0.818, 'f1': 0.9, 'support': 11}
  CWE-787: {'precision': 0.457, 'recall': 0.615, 'f1': 0.525, 'support': 26}
  CWE-79: {'precision': 0.429, 'recall': 0.5, 'f1': 0.462, 'support': 6}

Epoch 8/12
-----
train Loss: 0.3805 Acc: 0.9382
train Align Loss: 0.7333 Class Loss: 0.2293
train Top-3 Acc: 0.9901
train Metrics per class:
  CWE-119: {'precision': 0.786, 'recall': 0.702, 'f1': 0.742, 'support': 272}
  CWE-125: {'precision': 0.893, 'recall': 0.901, 'f1': 0.897, 'support': 314}
  CWE-190: {'precision': 0.969, 'recall': 0.969, 'f1': 0.969, 'support': 294}
  CWE-20: {'precision': 0.762, 'recall': 0.698, 'f1': 0.729, 'support': 298}
  CWE-200: {'precision': 0.868, 'recall': 0.905, 'f1': 0.886, 'support': 304}
  CWE-284: {'precision': 0.987, 'recall': 1.0, 'f1': 0.993, 'support': 304}
  CWE-362: {'precision': 0.936, 'recall': 0.965, 'f1': 0.951, 'support': 289}
  CWE-404: {'precision': 1.0, 'recall': 1.0, 'f1': 1.0, 'support': 282}
  CWE-415: {'precision': 0.988, 'recall': 1.0, 'f1': 0.994, 'support': 255}
  CWE-416: {'precision': 0.945, 'recall': 0.959, 'f1': 0.952, 'support': 270}
  CWE-476: {'precision': 0.968, 'recall': 0.99, 'f1': 0.979, 'support': 310}
  CWE-59: {'precision': 1.0, 'recall': 1.0, 'f1': 1.0, 'support': 292}
  CWE-732: {'precision': 0.994, 'recall': 1.0, 'f1': 0.997, 'support': 309}
  CWE-787: {'precision': 0.959, 'recall': 0.984, 'f1': 0.971, 'support': 306}
  CWE-79: {'precision': 0.996, 'recall': 1.0, 'f1': 0.998, 'support': 253}
val Loss: 1.7629 Acc: 0.5697
val Align Loss: 2.3937 Class Loss: 1.4925
val Top-3 Acc: 0.8326
val Metrics per class:
  CWE-119: {'precision': 0.67, 'recall': 0.611, 'f1': 0.639, 'support': 319}
  CWE-125: {'precision': 0.584, 'recall': 0.517, 'f1': 0.549, 'support': 87}
  CWE-190: {'precision': 0.491, 'recall': 0.622, 'f1': 0.549, 'support': 45}
  CWE-20: {'precision': 0.491, 'recall': 0.516, 'f1': 0.503, 'support': 161}
  CWE-200: {'precision': 0.459, 'recall': 0.6, 'f1': 0.52, 'support': 75}
  CWE-284: {'precision': 0.724, 'recall': 0.7, 'f1': 0.712, 'support': 30}
  CWE-362: {'precision': 0.559, 'recall': 0.442, 'f1': 0.494, 'support': 43}
  CWE-404: {'precision': 0.875, 'recall': 1.0, 'f1': 0.933, 'support': 14}
  CWE-415: {'precision': 0.571, 'recall': 0.533, 'f1': 0.552, 'support': 15}
  CWE-416: {'precision': 0.471, 'recall': 0.436, 'f1': 0.453, 'support': 55}
  CWE-476: {'precision': 0.436, 'recall': 0.425, 'f1': 0.43, 'support': 40}
  CWE-59: {'precision': 0.75, 'recall': 0.6, 'f1': 0.667, 'support': 5}
  CWE-732: {'precision': 0.857, 'recall': 0.75, 'f1': 0.8, 'support': 8}
  CWE-787: {'precision': 0.472, 'recall': 0.68, 'f1': 0.557, 'support': 25}
  CWE-79: {'precision': 0.6, 'recall': 0.6, 'f1': 0.6, 'support': 10}
New best val acc: 0.5697, saving model.
test Loss: 1.6561 Acc: 0.6028
test Align Loss: 2.3346 Class Loss: 1.3653
test Top-3 Acc: 0.8747
test Metrics per class:
  CWE-119: {'precision': 0.735, 'recall': 0.635, 'f1': 0.681, 'support': 323}
  CWE-125: {'precision': 0.628, 'recall': 0.643, 'f1': 0.635, 'support': 84}
  CWE-190: {'precision': 0.577, 'recall': 0.667, 'f1': 0.619, 'support': 45}
  CWE-20: {'precision': 0.584, 'recall': 0.533, 'f1': 0.557, 'support': 182}
  CWE-200: {'precision': 0.413, 'recall': 0.537, 'f1': 0.467, 'support': 80}
  CWE-284: {'precision': 0.656, 'recall': 0.656, 'f1': 0.656, 'support': 32}
  CWE-362: {'precision': 0.583, 'recall': 0.568, 'f1': 0.575, 'support': 37}
  CWE-404: {'precision': 0.625, 'recall': 1.0, 'f1': 0.769, 'support': 5}
  CWE-415: {'precision': 0.437, 'recall': 0.778, 'f1': 0.56, 'support': 9}
  CWE-416: {'precision': 0.415, 'recall': 0.458, 'f1': 0.436, 'support': 48}
  CWE-476: {'precision': 0.585, 'recall': 0.649, 'f1': 0.615, 'support': 37}
  CWE-59: {'precision': 0.429, 'recall': 0.333, 'f1': 0.375, 'support': 9}
  CWE-732: {'precision': 1.0, 'recall': 0.818, 'f1': 0.9, 'support': 11}
  CWE-787: {'precision': 0.486, 'recall': 0.692, 'f1': 0.571, 'support': 26}
  CWE-79: {'precision': 0.5, 'recall': 0.667, 'f1': 0.571, 'support': 6}

Epoch 9/12
-----
train Loss: 0.3390 Acc: 0.9494
train Align Loss: 0.6959 Class Loss: 0.1860
train Top-3 Acc: 0.9933
train Metrics per class:
  CWE-119: {'precision': 0.81, 'recall': 0.755, 'f1': 0.782, 'support': 294}
  CWE-125: {'precision': 0.909, 'recall': 0.888, 'f1': 0.898, 'support': 269}
  CWE-190: {'precision': 0.969, 'recall': 0.973, 'f1': 0.971, 'support': 257}
  CWE-20: {'precision': 0.811, 'recall': 0.754, 'f1': 0.781, 'support': 301}
  CWE-200: {'precision': 0.883, 'recall': 0.939, 'f1': 0.91, 'support': 280}
  CWE-284: {'precision': 0.977, 'recall': 1.0, 'f1': 0.988, 'support': 300}
  CWE-362: {'precision': 0.974, 'recall': 0.984, 'f1': 0.979, 'support': 309}
  CWE-404: {'precision': 1.0, 'recall': 1.0, 'f1': 1.0, 'support': 309}
  CWE-415: {'precision': 0.997, 'recall': 1.0, 'f1': 0.998, 'support': 292}
  CWE-416: {'precision': 0.943, 'recall': 0.967, 'f1': 0.955, 'support': 276}
  CWE-476: {'precision': 0.98, 'recall': 0.993, 'f1': 0.987, 'support': 301}
  CWE-59: {'precision': 0.997, 'recall': 1.0, 'f1': 0.998, 'support': 295}
  CWE-732: {'precision': 1.0, 'recall': 1.0, 'f1': 1.0, 'support': 290}
  CWE-787: {'precision': 0.969, 'recall': 0.986, 'f1': 0.977, 'support': 281}
  CWE-79: {'precision': 1.0, 'recall': 1.0, 'f1': 1.0, 'support': 298}
val Loss: 1.7928 Acc: 0.5880
val Align Loss: 2.4655 Class Loss: 1.5045
val Top-3 Acc: 0.8412
val Metrics per class:
  CWE-119: {'precision': 0.661, 'recall': 0.643, 'f1': 0.652, 'support': 319}
  CWE-125: {'precision': 0.615, 'recall': 0.552, 'f1': 0.582, 'support': 87}
  CWE-190: {'precision': 0.528, 'recall': 0.622, 'f1': 0.571, 'support': 45}
  CWE-20: {'precision': 0.463, 'recall': 0.59, 'f1': 0.519, 'support': 161}
  CWE-200: {'precision': 0.621, 'recall': 0.547, 'f1': 0.582, 'support': 75}
  CWE-284: {'precision': 0.741, 'recall': 0.667, 'f1': 0.702, 'support': 30}
  CWE-362: {'precision': 0.656, 'recall': 0.488, 'f1': 0.56, 'support': 43}
  CWE-404: {'precision': 0.824, 'recall': 1.0, 'f1': 0.903, 'support': 14}
  CWE-415: {'precision': 0.5, 'recall': 0.6, 'f1': 0.545, 'support': 15}
  CWE-416: {'precision': 0.6, 'recall': 0.382, 'f1': 0.467, 'support': 55}
  CWE-476: {'precision': 0.5, 'recall': 0.4, 'f1': 0.444, 'support': 40}
  CWE-59: {'precision': 0.75, 'recall': 0.6, 'f1': 0.667, 'support': 5}
  CWE-732: {'precision': 0.857, 'recall': 0.75, 'f1': 0.8, 'support': 8}
  CWE-787: {'precision': 0.39, 'recall': 0.64, 'f1': 0.485, 'support': 25}
  CWE-79: {'precision': 0.714, 'recall': 0.5, 'f1': 0.588, 'support': 10}
New best val acc: 0.5880, saving model.
test Loss: 1.6592 Acc: 0.6081
test Align Loss: 2.3679 Class Loss: 1.3555
test Top-3 Acc: 0.8758
test Metrics per class:
  CWE-119: {'precision': 0.693, 'recall': 0.635, 'f1': 0.662, 'support': 323}
  CWE-125: {'precision': 0.584, 'recall': 0.702, 'f1': 0.638, 'support': 84}
  CWE-190: {'precision': 0.612, 'recall': 0.667, 'f1': 0.638, 'support': 45}
  CWE-20: {'precision': 0.557, 'recall': 0.615, 'f1': 0.585, 'support': 182}
  CWE-200: {'precision': 0.6, 'recall': 0.45, 'f1': 0.514, 'support': 80}
  CWE-284: {'precision': 0.724, 'recall': 0.656, 'f1': 0.689, 'support': 32}
  CWE-362: {'precision': 0.633, 'recall': 0.514, 'f1': 0.567, 'support': 37}
  CWE-404: {'precision': 0.625, 'recall': 1.0, 'f1': 0.769, 'support': 5}
  CWE-415: {'precision': 0.437, 'recall': 0.778, 'f1': 0.56, 'support': 9}
  CWE-416: {'precision': 0.455, 'recall': 0.417, 'f1': 0.435, 'support': 48}
  CWE-476: {'precision': 0.677, 'recall': 0.568, 'f1': 0.618, 'support': 37}
  CWE-59: {'precision': 0.429, 'recall': 0.333, 'f1': 0.375, 'support': 9}
  CWE-732: {'precision': 1.0, 'recall': 0.909, 'f1': 0.952, 'support': 11}
  CWE-787: {'precision': 0.37, 'recall': 0.654, 'f1': 0.472, 'support': 26}
  CWE-79: {'precision': 0.5, 'recall': 0.5, 'f1': 0.5, 'support': 6}

Epoch 10/12
-----
train Loss: 0.3153 Acc: 0.9575
train Align Loss: 0.6816 Class Loss: 0.1583
train Top-3 Acc: 0.9954
train Metrics per class:
  CWE-119: {'precision': 0.84, 'recall': 0.728, 'f1': 0.78, 'support': 309}
  CWE-125: {'precision': 0.95, 'recall': 0.947, 'f1': 0.948, 'support': 319}
  CWE-190: {'precision': 0.99, 'recall': 0.976, 'f1': 0.983, 'support': 297}
  CWE-20: {'precision': 0.823, 'recall': 0.837, 'f1': 0.83, 'support': 295}
  CWE-200: {'precision': 0.886, 'recall': 0.934, 'f1': 0.909, 'support': 290}
  CWE-284: {'precision': 0.996, 'recall': 0.996, 'f1': 0.996, 'support': 281}
  CWE-362: {'precision': 0.973, 'recall': 0.993, 'f1': 0.983, 'support': 292}
  CWE-404: {'precision': 1.0, 'recall': 1.0, 'f1': 1.0, 'support': 276}
  CWE-415: {'precision': 0.989, 'recall': 1.0, 'f1': 0.994, 'support': 266}
  CWE-416: {'precision': 0.964, 'recall': 0.982, 'f1': 0.973, 'support': 272}
  CWE-476: {'precision': 0.971, 'recall': 0.996, 'f1': 0.984, 'support': 270}
  CWE-59: {'precision': 1.0, 'recall': 1.0, 'f1': 1.0, 'support': 297}
  CWE-732: {'precision': 1.0, 'recall': 1.0, 'f1': 1.0, 'support': 300}
  CWE-787: {'precision': 0.983, 'recall': 0.997, 'f1': 0.99, 'support': 297}
  CWE-79: {'precision': 1.0, 'recall': 1.0, 'f1': 1.0, 'support': 291}
val Loss: 1.7914 Acc: 0.5773
val Align Loss: 2.4998 Class Loss: 1.4878
val Top-3 Acc: 0.8423
val Metrics per class:
  CWE-119: {'precision': 0.648, 'recall': 0.674, 'f1': 0.661, 'support': 319}
  CWE-125: {'precision': 0.671, 'recall': 0.54, 'f1': 0.599, 'support': 87}
  CWE-190: {'precision': 0.466, 'recall': 0.6, 'f1': 0.524, 'support': 45}
  CWE-20: {'precision': 0.452, 'recall': 0.528, 'f1': 0.487, 'support': 161}
  CWE-200: {'precision': 0.528, 'recall': 0.507, 'f1': 0.517, 'support': 75}
  CWE-284: {'precision': 0.741, 'recall': 0.667, 'f1': 0.702, 'support': 30}
  CWE-362: {'precision': 0.667, 'recall': 0.372, 'f1': 0.478, 'support': 43}
  CWE-404: {'precision': 0.824, 'recall': 1.0, 'f1': 0.903, 'support': 14}
  CWE-415: {'precision': 0.471, 'recall': 0.533, 'f1': 0.5, 'support': 15}
  CWE-416: {'precision': 0.478, 'recall': 0.4, 'f1': 0.436, 'support': 55}
  CWE-476: {'precision': 0.471, 'recall': 0.4, 'f1': 0.432, 'support': 40}
  CWE-59: {'precision': 0.75, 'recall': 0.6, 'f1': 0.667, 'support': 5}
  CWE-732: {'precision': 0.857, 'recall': 0.75, 'f1': 0.8, 'support': 8}
  CWE-787: {'precision': 0.552, 'recall': 0.64, 'f1': 0.593, 'support': 25}
  CWE-79: {'precision': 0.714, 'recall': 0.5, 'f1': 0.588, 'support': 10}
test Loss: 1.6595 Acc: 0.6274
test Align Loss: 2.4156 Class Loss: 1.3354
test Top-3 Acc: 0.8747
test Metrics per class:
  CWE-119: {'precision': 0.688, 'recall': 0.69, 'f1': 0.689, 'support': 323}
  CWE-125: {'precision': 0.679, 'recall': 0.655, 'f1': 0.667, 'support': 84}
  CWE-190: {'precision': 0.537, 'recall': 0.644, 'f1': 0.586, 'support': 45}
  CWE-20: {'precision': 0.6, 'recall': 0.626, 'f1': 0.613, 'support': 182}
  CWE-200: {'precision': 0.522, 'recall': 0.437, 'f1': 0.476, 'support': 80}
  CWE-284: {'precision': 0.677, 'recall': 0.656, 'f1': 0.667, 'support': 32}
  CWE-362: {'precision': 0.731, 'recall': 0.514, 'f1': 0.603, 'support': 37}
  CWE-404: {'precision': 0.625, 'recall': 1.0, 'f1': 0.769, 'support': 5}
  CWE-415: {'precision': 0.467, 'recall': 0.778, 'f1': 0.583, 'support': 9}
  CWE-416: {'precision': 0.435, 'recall': 0.562, 'f1': 0.491, 'support': 48}
  CWE-476: {'precision': 0.7, 'recall': 0.568, 'f1': 0.627, 'support': 37}
  CWE-59: {'precision': 0.571, 'recall': 0.444, 'f1': 0.5, 'support': 9}
  CWE-732: {'precision': 1.0, 'recall': 0.909, 'f1': 0.952, 'support': 11}
  CWE-787: {'precision': 0.56, 'recall': 0.538, 'f1': 0.549, 'support': 26}
  CWE-79: {'precision': 0.5, 'recall': 0.333, 'f1': 0.4, 'support': 6}

Epoch 11/12
-----
train Loss: 0.2945 Acc: 0.9660
train Align Loss: 0.6687 Class Loss: 0.1342
train Top-3 Acc: 0.9959
train Metrics per class:
  CWE-119: {'precision': 0.864, 'recall': 0.802, 'f1': 0.832, 'support': 293}
  CWE-125: {'precision': 0.968, 'recall': 0.945, 'f1': 0.957, 'support': 291}
  CWE-190: {'precision': 0.984, 'recall': 0.981, 'f1': 0.982, 'support': 308}
  CWE-20: {'precision': 0.845, 'recall': 0.845, 'f1': 0.845, 'support': 283}
  CWE-200: {'precision': 0.935, 'recall': 0.959, 'f1': 0.947, 'support': 269}
  CWE-284: {'precision': 0.984, 'recall': 1.0, 'f1': 0.992, 'support': 302}
  CWE-362: {'precision': 0.977, 'recall': 0.99, 'f1': 0.984, 'support': 303}
  CWE-404: {'precision': 1.0, 'recall': 1.0, 'f1': 1.0, 'support': 308}
  CWE-415: {'precision': 1.0, 'recall': 1.0, 'f1': 1.0, 'support': 290}
  CWE-416: {'precision': 0.969, 'recall': 0.972, 'f1': 0.97, 'support': 285}
  CWE-476: {'precision': 0.973, 'recall': 0.996, 'f1': 0.984, 'support': 254}
  CWE-59: {'precision': 1.0, 'recall': 1.0, 'f1': 1.0, 'support': 291}
  CWE-732: {'precision': 0.996, 'recall': 1.0, 'f1': 0.998, 'support': 279}
  CWE-787: {'precision': 0.979, 'recall': 0.997, 'f1': 0.988, 'support': 287}
  CWE-79: {'precision': 1.0, 'recall': 1.0, 'f1': 1.0, 'support': 309}
val Loss: 1.7935 Acc: 0.5923
val Align Loss: 2.4945 Class Loss: 1.4930
val Top-3 Acc: 0.8423
val Metrics per class:
  CWE-119: {'precision': 0.669, 'recall': 0.665, 'f1': 0.667, 'support': 319}
  CWE-125: {'precision': 0.6, 'recall': 0.552, 'f1': 0.575, 'support': 87}
  CWE-190: {'precision': 0.509, 'recall': 0.622, 'f1': 0.56, 'support': 45}
  CWE-20: {'precision': 0.482, 'recall': 0.596, 'f1': 0.533, 'support': 161}
  CWE-200: {'precision': 0.532, 'recall': 0.547, 'f1': 0.539, 'support': 75}
  CWE-284: {'precision': 0.769, 'recall': 0.667, 'f1': 0.714, 'support': 30}
  CWE-362: {'precision': 0.667, 'recall': 0.372, 'f1': 0.478, 'support': 43}
  CWE-404: {'precision': 0.824, 'recall': 1.0, 'f1': 0.903, 'support': 14}
  CWE-415: {'precision': 0.471, 'recall': 0.533, 'f1': 0.5, 'support': 15}
  CWE-416: {'precision': 0.575, 'recall': 0.418, 'f1': 0.484, 'support': 55}
  CWE-476: {'precision': 0.516, 'recall': 0.4, 'f1': 0.451, 'support': 40}
  CWE-59: {'precision': 0.75, 'recall': 0.6, 'f1': 0.667, 'support': 5}
  CWE-732: {'precision': 0.857, 'recall': 0.75, 'f1': 0.8, 'support': 8}
  CWE-787: {'precision': 0.552, 'recall': 0.64, 'f1': 0.593, 'support': 25}
  CWE-79: {'precision': 0.556, 'recall': 0.5, 'f1': 0.526, 'support': 10}
New best val acc: 0.5923, saving model.
test Loss: 1.6576 Acc: 0.6435
test Align Loss: 2.3995 Class Loss: 1.3396
test Top-3 Acc: 0.8769
test Metrics per class:
  CWE-119: {'precision': 0.711, 'recall': 0.693, 'f1': 0.702, 'support': 323}
  CWE-125: {'precision': 0.606, 'recall': 0.679, 'f1': 0.64, 'support': 84}
  CWE-190: {'precision': 0.652, 'recall': 0.667, 'f1': 0.659, 'support': 45}
  CWE-20: {'precision': 0.619, 'recall': 0.687, 'f1': 0.651, 'support': 182}
  CWE-200: {'precision': 0.507, 'recall': 0.462, 'f1': 0.484, 'support': 80}
  CWE-284: {'precision': 0.724, 'recall': 0.656, 'f1': 0.689, 'support': 32}
  CWE-362: {'precision': 0.645, 'recall': 0.541, 'f1': 0.588, 'support': 37}
  CWE-404: {'precision': 0.625, 'recall': 1.0, 'f1': 0.769, 'support': 5}
  CWE-415: {'precision': 0.467, 'recall': 0.778, 'f1': 0.583, 'support': 9}
  CWE-416: {'precision': 0.479, 'recall': 0.479, 'f1': 0.479, 'support': 48}
  CWE-476: {'precision': 0.741, 'recall': 0.541, 'f1': 0.625, 'support': 37}
  CWE-59: {'precision': 0.571, 'recall': 0.444, 'f1': 0.5, 'support': 9}
  CWE-732: {'precision': 1.0, 'recall': 0.909, 'f1': 0.952, 'support': 11}
  CWE-787: {'precision': 0.636, 'recall': 0.538, 'f1': 0.583, 'support': 26}
  CWE-79: {'precision': 0.571, 'recall': 0.667, 'f1': 0.615, 'support': 6}

Epoch 12/12
-----
train Loss: 0.2911 Acc: 0.9644
train Align Loss: 0.6567 Class Loss: 0.1344
train Top-3 Acc: 0.9968
train Metrics per class:
  CWE-119: {'precision': 0.881, 'recall': 0.81, 'f1': 0.844, 'support': 294}
  CWE-125: {'precision': 0.944, 'recall': 0.931, 'f1': 0.937, 'support': 305}
  CWE-190: {'precision': 0.987, 'recall': 0.993, 'f1': 0.99, 'support': 295}
  CWE-20: {'precision': 0.869, 'recall': 0.833, 'f1': 0.851, 'support': 287}
  CWE-200: {'precision': 0.903, 'recall': 0.957, 'f1': 0.929, 'support': 253}
  CWE-284: {'precision': 0.993, 'recall': 0.997, 'f1': 0.995, 'support': 298}
  CWE-362: {'precision': 0.967, 'recall': 0.99, 'f1': 0.978, 'support': 292}
  CWE-404: {'precision': 1.0, 'recall': 1.0, 'f1': 1.0, 'support': 322}
  CWE-415: {'precision': 0.984, 'recall': 1.0, 'f1': 0.992, 'support': 299}
  CWE-416: {'precision': 0.954, 'recall': 0.961, 'f1': 0.958, 'support': 282}
  CWE-476: {'precision': 0.983, 'recall': 0.997, 'f1': 0.99, 'support': 295}
  CWE-59: {'precision': 1.0, 'recall': 1.0, 'f1': 1.0, 'support': 261}
  CWE-732: {'precision': 0.997, 'recall': 1.0, 'f1': 0.998, 'support': 310}
  CWE-787: {'precision': 0.986, 'recall': 0.997, 'f1': 0.991, 'support': 288}
  CWE-79: {'precision': 1.0, 'recall': 1.0, 'f1': 1.0, 'support': 271}
val Loss: 1.7722 Acc: 0.6009
val Align Loss: 2.4761 Class Loss: 1.4706
val Top-3 Acc: 0.8444
val Metrics per class:
  CWE-119: {'precision': 0.654, 'recall': 0.693, 'f1': 0.673, 'support': 319}
  CWE-125: {'precision': 0.662, 'recall': 0.563, 'f1': 0.609, 'support': 87}
  CWE-190: {'precision': 0.529, 'recall': 0.6, 'f1': 0.562, 'support': 45}
  CWE-20: {'precision': 0.487, 'recall': 0.596, 'f1': 0.536, 'support': 161}
  CWE-200: {'precision': 0.583, 'recall': 0.56, 'f1': 0.571, 'support': 75}
  CWE-284: {'precision': 0.769, 'recall': 0.667, 'f1': 0.714, 'support': 30}
  CWE-362: {'precision': 0.654, 'recall': 0.395, 'f1': 0.493, 'support': 43}
  CWE-404: {'precision': 0.824, 'recall': 1.0, 'f1': 0.903, 'support': 14}
  CWE-415: {'precision': 0.5, 'recall': 0.533, 'f1': 0.516, 'support': 15}
  CWE-416: {'precision': 0.59, 'recall': 0.418, 'f1': 0.489, 'support': 55}
  CWE-476: {'precision': 0.5, 'recall': 0.375, 'f1': 0.429, 'support': 40}
  CWE-59: {'precision': 0.75, 'recall': 0.6, 'f1': 0.667, 'support': 5}
  CWE-732: {'precision': 0.857, 'recall': 0.75, 'f1': 0.8, 'support': 8}
  CWE-787: {'precision': 0.538, 'recall': 0.56, 'f1': 0.549, 'support': 25}
  CWE-79: {'precision': 0.556, 'recall': 0.5, 'f1': 0.526, 'support': 10}
New best val acc: 0.6009, saving model.
test Loss: 1.6518 Acc: 0.6403
test Align Loss: 2.3964 Class Loss: 1.3327
test Top-3 Acc: 0.8801
test Metrics per class:
  CWE-119: {'precision': 0.693, 'recall': 0.712, 'f1': 0.702, 'support': 323}
  CWE-125: {'precision': 0.667, 'recall': 0.667, 'f1': 0.667, 'support': 84}
  CWE-190: {'precision': 0.638, 'recall': 0.667, 'f1': 0.652, 'support': 45}
  CWE-20: {'precision': 0.607, 'recall': 0.654, 'f1': 0.63, 'support': 182}
  CWE-200: {'precision': 0.536, 'recall': 0.462, 'f1': 0.497, 'support': 80}
  CWE-284: {'precision': 0.724, 'recall': 0.656, 'f1': 0.689, 'support': 32}
  CWE-362: {'precision': 0.625, 'recall': 0.541, 'f1': 0.58, 'support': 37}
  CWE-404: {'precision': 0.571, 'recall': 0.8, 'f1': 0.667, 'support': 5}
  CWE-415: {'precision': 0.429, 'recall': 0.667, 'f1': 0.522, 'support': 9}
  CWE-416: {'precision': 0.469, 'recall': 0.479, 'f1': 0.474, 'support': 48}
  CWE-476: {'precision': 0.7, 'recall': 0.568, 'f1': 0.627, 'support': 37}
  CWE-59: {'precision': 0.5, 'recall': 0.333, 'f1': 0.4, 'support': 9}
  CWE-732: {'precision': 1.0, 'recall': 0.909, 'f1': 0.952, 'support': 11}
  CWE-787: {'precision': 0.636, 'recall': 0.538, 'f1': 0.583, 'support': 26}
  CWE-79: {'precision': 0.571, 'recall': 0.667, 'f1': 0.615, 'support': 6}

Training complete in 95m 9s
Best val Acc: 0.6009
