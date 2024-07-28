"""Frequency plasma parameters."""

import astropy.units as u
import numpy as np

from plasmapy.particles.decorators import particle_input
from plasmapy.particles.particle_class import ParticleLike
from plasmapy.utils.decorators import (
    validate_quantities,
)
from astropy import constants


@particle_input
@validate_quantities(
    validations_on_return={
        "units": [u.rad / u.s, u.Hz],
        "equivalencies": [(u.cy / u.s, u.Hz)],
    },
)
def plasma_frequency(
    n: u.Quantity[u.m**-3],
    particle: ParticleLike,
    *,
    mass_numb: int | None = None,
    Z: float | None = None,
) -> u.Quantity[u.rad / u.s]:
    r"""Calculate the particle plasma frequency.

    Parameters
    ----------
    n : `~astropy.units.Quantity`
        Particle number density in units convertible to m\ :sup:`-3`.

    particle : |particle-like|
        Representation of the particle species.

    Z : real number, optional
        The charge number of an ion or neutral atom, if not provided
        in ``particle``.

    mass_numb : integer, optional
        The mass number of an isotope, if not provided in ``particle``.

    Returns
    -------
    `~astropy.units.Quantity`
        The particle plasma frequency in radians per second.

    Notes
    -----
    The particle plasma frequency is

    .. math::
        ω_p = \sqrt{\frac{n |q|}{ε_0 m}}

    where :math:`n` is the number density, :math:`q` is the particle
    charge, and :math:`m` is the particle mass.

    Examples
    --------
    >>> import astropy.units as u
    >>> plasma_frequency(1e19 * u.m**-3, particle="p+")
    <Quantity 4.16329...e+09 rad / s>
    """
    return np.sqrt(n * np.abs(particle.charge) / (constants.eps0 * particle.mass))
