# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libxrender(AutotoolsPackage):
    """libXrender - library for the Render Extension to the X11 protocol."""

    homepage = "http://cgit.freedesktop.org/xorg/lib/libXrender"
    url      = "https://www.x.org/archive/individual/lib/libXrender-0.9.10.tar.gz"

    version('0.9.10', sha256='770527cce42500790433df84ec3521e8bf095dfe5079454a92236494ab296adf')
    version('0.9.9',  sha256='beeac64ff8d225f775019eb7c688782dee9f4cc7b412a65538f8dde7be4e90fe')

    depends_on('libx11@1.6:')

    depends_on('renderproto@0.9:', type=('build', 'link'))
    depends_on('pkgconfig', type='build')
    depends_on('util-macros', type='build')
