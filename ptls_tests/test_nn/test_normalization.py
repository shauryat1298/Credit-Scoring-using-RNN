import torch
import numpy as np

from ptls.nn.normalization import L2NormEncoder


def test_norm_encoder():
    x = torch.tensor([
        [1.0, 0.0],
        [0.0, 2.0],
        [3.0, 4.0],
    ], dtype=torch.float64)

    f = L2NormEncoder()
    out = f(x).numpy()
    exp = np.array([
        [1.0, 0.0],
        [0.0, 1.0],
        [0.6, 0.8],
    ])
    np.testing.assert_array_almost_equal(exp, out)
