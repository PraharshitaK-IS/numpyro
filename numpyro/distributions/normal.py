# Source code modified from scipy.stats._continuous_distns.py
#
# Copyright (c) 2001, 2002 Enthought, Inc.
# All rights reserved.
#
# Copyright (c) 2003-2019 SciPy Developers.
# All rights reserved.

import jax.numpy as np
import jax.random as random

from numpyro.distributions.distribution import jax_continuous


_norm_pdf_C = np.sqrt(2 * np.pi)
_norm_pdf_logC = np.log(_norm_pdf_C)


def _norm_pdf(x):
    return np.exp(-x ** 2 / 2.0) / _norm_pdf_C


def _norm_logpdf(x):
    return -x ** 2 / 2.0 - _norm_pdf_logC


class norm_gen(jax_continuous):
    def _rvs(self):
        return random.normal(self._random_state, self._size)

    def _stats(self):
        return 0.0, 1.0, 0.0, 0.0

    def _entropy(self):
        return 0.5 * (np.log(2 * np.pi) + 1)


norm = norm_gen(name='norm')
