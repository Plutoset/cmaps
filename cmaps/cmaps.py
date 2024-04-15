#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
from glob import glob
from packaging import version

import matplotlib
import matplotlib.cm
import numpy as np

from ._version import __version__
from .colormap import Colormap

CMAPSFILE_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'colormaps')
USER_CMAPFILE_DIR = os.environ.get('CMAP_DIR')

if version.parse(matplotlib.__version__) < version.parse('3.2.0'):
    raise Exception('cmaps of version {} only supports matplotlib greater than 3.2'.format(__version__))

if version.parse(matplotlib.__version__) >= version.parse('3.7'):
    get_cmap = matplotlib.colormaps.get_cmap
    register_cmap = matplotlib.colormaps.register
else:
    get_cmap = matplotlib.cm.get_cmap
    register_cmap = matplotlib.cm.register_cmap


class Cmaps(object):
    """colormaps"""

    def __init__(self, ):
        self._parse_cmaps()
        self.__version__ = __version__

    def _coltbl(self, cmap_file):
        pattern = re.compile(r'(\d\.?\d*)\s+(\d\.?\d*)\s+(\d\.?\d*).*')
        with open(cmap_file) as cmap:
            cmap_buff = cmap.read()
        cmap_buff = re.compile('ncolors.*\n').sub('', cmap_buff)
        if re.search(r'\s*\d\.\d*', cmap_buff):
            return np.asarray(pattern.findall(cmap_buff), 'f4')
        else:
            return np.asarray(pattern.findall(cmap_buff), 'u1') / 255.

    def _parse_cmaps(self):
        if USER_CMAPFILE_DIR is not None:
            cmapsflist = sorted(glob(os.path.join(USER_CMAPFILE_DIR, '*.rgb')))
            for cmap_file in cmapsflist:
                cname = os.path.basename(cmap_file).split('.rgb')[0]
                # start with the number will result illegal attribute
                if cname[0].isdigit() or cname.startswith('_'):
                    cname = 'C' + cname
                if '-' in cname:
                    cname = 'cmaps_' + cname.replace('-', '_')
                if '+' in cname:
                    cname = 'cmaps_' + cname.replace('+', '_')

                try:
                    cmap = get_cmap(cname)
                except:
                    cmap = Colormap(self._coltbl(cmap_file), name=cname)
                    register_cmap(name=cname, cmap=cmap)
                setattr(self, cname, cmap)

                cname = cname + '_r'
                try:
                    cmap = get_cmap(cname)
                except:
                    cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
                    register_cmap(name=cname, cmap=cmap)
                setattr(self, cname, cmap)

    @property
    def N3gauss(self):
        cname = "N3gauss"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "3gauss.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def N3gauss_r(self):
        cname = "N3gauss_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "3gauss.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def N3saw(self):
        cname = "N3saw"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "3saw.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def N3saw_r(self):
        cname = "N3saw_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "3saw.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BkBlAqGrYeOrReViWh200(self):
        cname = "BkBlAqGrYeOrReViWh200"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BkBlAqGrYeOrReViWh200.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BkBlAqGrYeOrReViWh200_r(self):
        cname = "BkBlAqGrYeOrReViWh200_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BkBlAqGrYeOrReViWh200.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BlAqGrWh2YeOrReVi22(self):
        cname = "BlAqGrWh2YeOrReVi22"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BlAqGrWh2YeOrReVi22.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BlAqGrWh2YeOrReVi22_r(self):
        cname = "BlAqGrWh2YeOrReVi22_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BlAqGrWh2YeOrReVi22.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BlAqGrYeOrRe(self):
        cname = "BlAqGrYeOrRe"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BlAqGrYeOrRe.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BlAqGrYeOrRe_r(self):
        cname = "BlAqGrYeOrRe_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BlAqGrYeOrRe.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BlAqGrYeOrReVi200(self):
        cname = "BlAqGrYeOrReVi200"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BlAqGrYeOrReVi200.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BlAqGrYeOrReVi200_r(self):
        cname = "BlAqGrYeOrReVi200_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BlAqGrYeOrReVi200.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BlGrYeOrReVi200(self):
        cname = "BlGrYeOrReVi200"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BlGrYeOrReVi200.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BlGrYeOrReVi200_r(self):
        cname = "BlGrYeOrReVi200_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BlGrYeOrReVi200.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BlRe(self):
        cname = "BlRe"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BlRe.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BlRe_r(self):
        cname = "BlRe_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BlRe.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BlWhRe(self):
        cname = "BlWhRe"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BlWhRe.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BlWhRe_r(self):
        cname = "BlWhRe_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BlWhRe.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BlueDarkOrange18(self):
        cname = "BlueDarkOrange18"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BlueDarkOrange18.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BlueDarkOrange18_r(self):
        cname = "BlueDarkOrange18_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BlueDarkOrange18.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BlueDarkRed18(self):
        cname = "BlueDarkRed18"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BlueDarkRed18.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BlueDarkRed18_r(self):
        cname = "BlueDarkRed18_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BlueDarkRed18.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BlueGreen14(self):
        cname = "BlueGreen14"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BlueGreen14.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BlueGreen14_r(self):
        cname = "BlueGreen14_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BlueGreen14.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BlueRed(self):
        cname = "BlueRed"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BlueRed.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BlueRed_r(self):
        cname = "BlueRed_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BlueRed.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BlueRedGray(self):
        cname = "BlueRedGray"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BlueRedGray.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BlueRedGray_r(self):
        cname = "BlueRedGray_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BlueRedGray.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BlueWhiteOrangeRed(self):
        cname = "BlueWhiteOrangeRed"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BlueWhiteOrangeRed.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BlueWhiteOrangeRed_r(self):
        cname = "BlueWhiteOrangeRed_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BlueWhiteOrangeRed.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BlueYellowRed(self):
        cname = "BlueYellowRed"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BlueYellowRed.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BlueYellowRed_r(self):
        cname = "BlueYellowRed_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BlueYellowRed.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BrownBlue12(self):
        cname = "BrownBlue12"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BrownBlue12.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def BrownBlue12_r(self):
        cname = "BrownBlue12_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "BrownBlue12.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def CBR_coldhot(self):
        cname = "CBR_coldhot"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "CBR_coldhot.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def CBR_coldhot_r(self):
        cname = "CBR_coldhot_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "CBR_coldhot.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def CBR_drywet(self):
        cname = "CBR_drywet"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "CBR_drywet.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def CBR_drywet_r(self):
        cname = "CBR_drywet_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "CBR_drywet.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def CBR_set3(self):
        cname = "CBR_set3"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "CBR_set3.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def CBR_set3_r(self):
        cname = "CBR_set3_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "CBR_set3.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def CBR_wet(self):
        cname = "CBR_wet"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "CBR_wet.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def CBR_wet_r(self):
        cname = "CBR_wet_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "CBR_wet.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def Cat12(self):
        cname = "Cat12"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "Cat12.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def Cat12_r(self):
        cname = "Cat12_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "Cat12.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GHRSST_anomaly(self):
        cname = "GHRSST_anomaly"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GHRSST_anomaly.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GHRSST_anomaly_r(self):
        cname = "GHRSST_anomaly_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GHRSST_anomaly.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_cool(self):
        cname = "GMT_cool"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_cool.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_cool_r(self):
        cname = "GMT_cool_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_cool.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_copper(self):
        cname = "GMT_copper"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_copper.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_copper_r(self):
        cname = "GMT_copper_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_copper.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_drywet(self):
        cname = "GMT_drywet"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_drywet.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_drywet_r(self):
        cname = "GMT_drywet_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_drywet.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_gebco(self):
        cname = "GMT_gebco"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_gebco.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_gebco_r(self):
        cname = "GMT_gebco_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_gebco.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_globe(self):
        cname = "GMT_globe"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_globe.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_globe_r(self):
        cname = "GMT_globe_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_globe.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_gray(self):
        cname = "GMT_gray"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_gray.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_gray_r(self):
        cname = "GMT_gray_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_gray.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_haxby(self):
        cname = "GMT_haxby"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_haxby.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_haxby_r(self):
        cname = "GMT_haxby_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_haxby.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_hot(self):
        cname = "GMT_hot"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_hot.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_hot_r(self):
        cname = "GMT_hot_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_hot.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_jet(self):
        cname = "GMT_jet"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_jet.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_jet_r(self):
        cname = "GMT_jet_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_jet.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_nighttime(self):
        cname = "GMT_nighttime"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_nighttime.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_nighttime_r(self):
        cname = "GMT_nighttime_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_nighttime.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_no_green(self):
        cname = "GMT_no_green"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_no_green.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_no_green_r(self):
        cname = "GMT_no_green_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_no_green.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_ocean(self):
        cname = "GMT_ocean"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_ocean.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_ocean_r(self):
        cname = "GMT_ocean_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_ocean.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_paired(self):
        cname = "GMT_paired"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_paired.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_paired_r(self):
        cname = "GMT_paired_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_paired.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_panoply(self):
        cname = "GMT_panoply"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_panoply.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_panoply_r(self):
        cname = "GMT_panoply_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_panoply.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_polar(self):
        cname = "GMT_polar"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_polar.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_polar_r(self):
        cname = "GMT_polar_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_polar.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_red2green(self):
        cname = "GMT_red2green"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_red2green.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_red2green_r(self):
        cname = "GMT_red2green_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_red2green.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_relief(self):
        cname = "GMT_relief"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_relief.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_relief_r(self):
        cname = "GMT_relief_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_relief.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_relief_oceanonly(self):
        cname = "GMT_relief_oceanonly"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_relief_oceanonly.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_relief_oceanonly_r(self):
        cname = "GMT_relief_oceanonly_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_relief_oceanonly.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_seis(self):
        cname = "GMT_seis"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_seis.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_seis_r(self):
        cname = "GMT_seis_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_seis.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_split(self):
        cname = "GMT_split"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_split.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_split_r(self):
        cname = "GMT_split_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_split.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_topo(self):
        cname = "GMT_topo"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_topo.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_topo_r(self):
        cname = "GMT_topo_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_topo.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_wysiwyg(self):
        cname = "GMT_wysiwyg"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_wysiwyg.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_wysiwyg_r(self):
        cname = "GMT_wysiwyg_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_wysiwyg.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_wysiwygcont(self):
        cname = "GMT_wysiwygcont"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_wysiwygcont.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_wysiwygcont_r(self):
        cname = "GMT_wysiwygcont_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GMT_wysiwygcont.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GSFC_landsat_udf_density(self):
        cname = "GSFC_landsat_udf_density"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GSFC_landsat_udf_density.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GSFC_landsat_udf_density_r(self):
        cname = "GSFC_landsat_udf_density_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GSFC_landsat_udf_density.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GrayWhiteGray(self):
        cname = "GrayWhiteGray"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GrayWhiteGray.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GrayWhiteGray_r(self):
        cname = "GrayWhiteGray_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GrayWhiteGray.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GreenMagenta16(self):
        cname = "GreenMagenta16"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GreenMagenta16.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GreenMagenta16_r(self):
        cname = "GreenMagenta16_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GreenMagenta16.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GreenYellow(self):
        cname = "GreenYellow"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GreenYellow.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GreenYellow_r(self):
        cname = "GreenYellow_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "GreenYellow.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Accent(self):
        cname = "MPL_Accent"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Accent.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Accent_r(self):
        cname = "MPL_Accent_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Accent.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Blues(self):
        cname = "MPL_Blues"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Blues.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Blues_r(self):
        cname = "MPL_Blues_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Blues.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_BrBG(self):
        cname = "MPL_BrBG"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_BrBG.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_BrBG_r(self):
        cname = "MPL_BrBG_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_BrBG.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_BuGn(self):
        cname = "MPL_BuGn"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_BuGn.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_BuGn_r(self):
        cname = "MPL_BuGn_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_BuGn.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_BuPu(self):
        cname = "MPL_BuPu"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_BuPu.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_BuPu_r(self):
        cname = "MPL_BuPu_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_BuPu.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Dark2(self):
        cname = "MPL_Dark2"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Dark2.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Dark2_r(self):
        cname = "MPL_Dark2_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Dark2.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_GnBu(self):
        cname = "MPL_GnBu"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_GnBu.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_GnBu_r(self):
        cname = "MPL_GnBu_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_GnBu.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Greens(self):
        cname = "MPL_Greens"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Greens.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Greens_r(self):
        cname = "MPL_Greens_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Greens.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Greys(self):
        cname = "MPL_Greys"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Greys.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Greys_r(self):
        cname = "MPL_Greys_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Greys.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_OrRd(self):
        cname = "MPL_OrRd"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_OrRd.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_OrRd_r(self):
        cname = "MPL_OrRd_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_OrRd.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Oranges(self):
        cname = "MPL_Oranges"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Oranges.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Oranges_r(self):
        cname = "MPL_Oranges_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Oranges.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_PRGn(self):
        cname = "MPL_PRGn"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_PRGn.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_PRGn_r(self):
        cname = "MPL_PRGn_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_PRGn.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Paired(self):
        cname = "MPL_Paired"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Paired.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Paired_r(self):
        cname = "MPL_Paired_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Paired.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Pastel1(self):
        cname = "MPL_Pastel1"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Pastel1.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Pastel1_r(self):
        cname = "MPL_Pastel1_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Pastel1.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Pastel2(self):
        cname = "MPL_Pastel2"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Pastel2.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Pastel2_r(self):
        cname = "MPL_Pastel2_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Pastel2.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_PiYG(self):
        cname = "MPL_PiYG"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_PiYG.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_PiYG_r(self):
        cname = "MPL_PiYG_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_PiYG.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_PuBu(self):
        cname = "MPL_PuBu"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_PuBu.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_PuBu_r(self):
        cname = "MPL_PuBu_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_PuBu.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_PuBuGn(self):
        cname = "MPL_PuBuGn"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_PuBuGn.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_PuBuGn_r(self):
        cname = "MPL_PuBuGn_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_PuBuGn.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_PuOr(self):
        cname = "MPL_PuOr"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_PuOr.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_PuOr_r(self):
        cname = "MPL_PuOr_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_PuOr.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_PuRd(self):
        cname = "MPL_PuRd"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_PuRd.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_PuRd_r(self):
        cname = "MPL_PuRd_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_PuRd.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Purples(self):
        cname = "MPL_Purples"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Purples.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Purples_r(self):
        cname = "MPL_Purples_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Purples.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_RdBu(self):
        cname = "MPL_RdBu"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_RdBu.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_RdBu_r(self):
        cname = "MPL_RdBu_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_RdBu.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_RdGy(self):
        cname = "MPL_RdGy"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_RdGy.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_RdGy_r(self):
        cname = "MPL_RdGy_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_RdGy.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_RdPu(self):
        cname = "MPL_RdPu"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_RdPu.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_RdPu_r(self):
        cname = "MPL_RdPu_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_RdPu.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_RdYlBu(self):
        cname = "MPL_RdYlBu"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_RdYlBu.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_RdYlBu_r(self):
        cname = "MPL_RdYlBu_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_RdYlBu.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_RdYlGn(self):
        cname = "MPL_RdYlGn"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_RdYlGn.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_RdYlGn_r(self):
        cname = "MPL_RdYlGn_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_RdYlGn.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Reds(self):
        cname = "MPL_Reds"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Reds.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Reds_r(self):
        cname = "MPL_Reds_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Reds.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Set1(self):
        cname = "MPL_Set1"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Set1.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Set1_r(self):
        cname = "MPL_Set1_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Set1.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Set2(self):
        cname = "MPL_Set2"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Set2.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Set2_r(self):
        cname = "MPL_Set2_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Set2.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Set3(self):
        cname = "MPL_Set3"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Set3.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Set3_r(self):
        cname = "MPL_Set3_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Set3.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Spectral(self):
        cname = "MPL_Spectral"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Spectral.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_Spectral_r(self):
        cname = "MPL_Spectral_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_Spectral.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_StepSeq(self):
        cname = "MPL_StepSeq"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_StepSeq.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_StepSeq_r(self):
        cname = "MPL_StepSeq_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_StepSeq.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_YlGn(self):
        cname = "MPL_YlGn"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_YlGn.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_YlGn_r(self):
        cname = "MPL_YlGn_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_YlGn.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_YlGnBu(self):
        cname = "MPL_YlGnBu"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_YlGnBu.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_YlGnBu_r(self):
        cname = "MPL_YlGnBu_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_YlGnBu.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_YlOrBr(self):
        cname = "MPL_YlOrBr"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_YlOrBr.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_YlOrBr_r(self):
        cname = "MPL_YlOrBr_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_YlOrBr.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_YlOrRd(self):
        cname = "MPL_YlOrRd"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_YlOrRd.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_YlOrRd_r(self):
        cname = "MPL_YlOrRd_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_YlOrRd.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_afmhot(self):
        cname = "MPL_afmhot"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_afmhot.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_afmhot_r(self):
        cname = "MPL_afmhot_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_afmhot.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_autumn(self):
        cname = "MPL_autumn"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_autumn.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_autumn_r(self):
        cname = "MPL_autumn_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_autumn.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_bone(self):
        cname = "MPL_bone"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_bone.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_bone_r(self):
        cname = "MPL_bone_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_bone.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_brg(self):
        cname = "MPL_brg"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_brg.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_brg_r(self):
        cname = "MPL_brg_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_brg.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_bwr(self):
        cname = "MPL_bwr"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_bwr.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_bwr_r(self):
        cname = "MPL_bwr_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_bwr.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_cool(self):
        cname = "MPL_cool"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_cool.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_cool_r(self):
        cname = "MPL_cool_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_cool.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_coolwarm(self):
        cname = "MPL_coolwarm"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_coolwarm.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_coolwarm_r(self):
        cname = "MPL_coolwarm_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_coolwarm.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_copper(self):
        cname = "MPL_copper"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_copper.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_copper_r(self):
        cname = "MPL_copper_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_copper.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_cubehelix(self):
        cname = "MPL_cubehelix"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_cubehelix.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_cubehelix_r(self):
        cname = "MPL_cubehelix_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_cubehelix.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_flag(self):
        cname = "MPL_flag"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_flag.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_flag_r(self):
        cname = "MPL_flag_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_flag.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_gist_earth(self):
        cname = "MPL_gist_earth"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_gist_earth.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_gist_earth_r(self):
        cname = "MPL_gist_earth_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_gist_earth.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_gist_gray(self):
        cname = "MPL_gist_gray"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_gist_gray.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_gist_gray_r(self):
        cname = "MPL_gist_gray_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_gist_gray.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_gist_heat(self):
        cname = "MPL_gist_heat"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_gist_heat.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_gist_heat_r(self):
        cname = "MPL_gist_heat_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_gist_heat.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_gist_ncar(self):
        cname = "MPL_gist_ncar"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_gist_ncar.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_gist_ncar_r(self):
        cname = "MPL_gist_ncar_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_gist_ncar.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_gist_rainbow(self):
        cname = "MPL_gist_rainbow"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_gist_rainbow.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_gist_rainbow_r(self):
        cname = "MPL_gist_rainbow_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_gist_rainbow.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_gist_stern(self):
        cname = "MPL_gist_stern"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_gist_stern.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_gist_stern_r(self):
        cname = "MPL_gist_stern_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_gist_stern.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_gist_yarg(self):
        cname = "MPL_gist_yarg"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_gist_yarg.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_gist_yarg_r(self):
        cname = "MPL_gist_yarg_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_gist_yarg.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_gnuplot(self):
        cname = "MPL_gnuplot"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_gnuplot.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_gnuplot_r(self):
        cname = "MPL_gnuplot_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_gnuplot.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_gnuplot2(self):
        cname = "MPL_gnuplot2"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_gnuplot2.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_gnuplot2_r(self):
        cname = "MPL_gnuplot2_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_gnuplot2.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_hot(self):
        cname = "MPL_hot"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_hot.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_hot_r(self):
        cname = "MPL_hot_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_hot.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_hsv(self):
        cname = "MPL_hsv"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_hsv.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_hsv_r(self):
        cname = "MPL_hsv_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_hsv.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_jet(self):
        cname = "MPL_jet"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_jet.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_jet_r(self):
        cname = "MPL_jet_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_jet.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_ocean(self):
        cname = "MPL_ocean"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_ocean.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_ocean_r(self):
        cname = "MPL_ocean_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_ocean.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_pink(self):
        cname = "MPL_pink"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_pink.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_pink_r(self):
        cname = "MPL_pink_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_pink.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_prism(self):
        cname = "MPL_prism"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_prism.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_prism_r(self):
        cname = "MPL_prism_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_prism.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_rainbow(self):
        cname = "MPL_rainbow"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_rainbow.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_rainbow_r(self):
        cname = "MPL_rainbow_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_rainbow.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_s3pcpn(self):
        cname = "MPL_s3pcpn"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_s3pcpn.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_s3pcpn_r(self):
        cname = "MPL_s3pcpn_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_s3pcpn.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_s3pcpn_l(self):
        cname = "MPL_s3pcpn_l"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_s3pcpn_l.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_s3pcpn_l_r(self):
        cname = "MPL_s3pcpn_l_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_s3pcpn_l.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_seismic(self):
        cname = "MPL_seismic"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_seismic.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_seismic_r(self):
        cname = "MPL_seismic_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_seismic.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_spring(self):
        cname = "MPL_spring"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_spring.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_spring_r(self):
        cname = "MPL_spring_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_spring.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_sstanom(self):
        cname = "MPL_sstanom"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_sstanom.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_sstanom_r(self):
        cname = "MPL_sstanom_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_sstanom.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_summer(self):
        cname = "MPL_summer"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_summer.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_summer_r(self):
        cname = "MPL_summer_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_summer.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_terrain(self):
        cname = "MPL_terrain"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_terrain.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_terrain_r(self):
        cname = "MPL_terrain_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_terrain.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_viridis(self):
        cname = "MPL_viridis"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_viridis.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_viridis_r(self):
        cname = "MPL_viridis_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_viridis.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_winter(self):
        cname = "MPL_winter"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_winter.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MPL_winter_r(self):
        cname = "MPL_winter_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "MPL_winter.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NCV_banded(self):
        cname = "NCV_banded"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NCV_banded.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NCV_banded_r(self):
        cname = "NCV_banded_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NCV_banded.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NCV_blu_red(self):
        cname = "NCV_blu_red"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NCV_blu_red.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NCV_blu_red_r(self):
        cname = "NCV_blu_red_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NCV_blu_red.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NCV_blue_red(self):
        cname = "NCV_blue_red"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NCV_blue_red.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NCV_blue_red_r(self):
        cname = "NCV_blue_red_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NCV_blue_red.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NCV_bright(self):
        cname = "NCV_bright"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NCV_bright.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NCV_bright_r(self):
        cname = "NCV_bright_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NCV_bright.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NCV_gebco(self):
        cname = "NCV_gebco"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NCV_gebco.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NCV_gebco_r(self):
        cname = "NCV_gebco_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NCV_gebco.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NCV_jaisnd(self):
        cname = "NCV_jaisnd"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NCV_jaisnd.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NCV_jaisnd_r(self):
        cname = "NCV_jaisnd_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NCV_jaisnd.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NCV_jet(self):
        cname = "NCV_jet"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NCV_jet.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NCV_jet_r(self):
        cname = "NCV_jet_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NCV_jet.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NCV_manga(self):
        cname = "NCV_manga"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NCV_manga.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NCV_manga_r(self):
        cname = "NCV_manga_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NCV_manga.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NCV_rainbow2(self):
        cname = "NCV_rainbow2"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NCV_rainbow2.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NCV_rainbow2_r(self):
        cname = "NCV_rainbow2_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NCV_rainbow2.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NCV_roullet(self):
        cname = "NCV_roullet"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NCV_roullet.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NCV_roullet_r(self):
        cname = "NCV_roullet_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NCV_roullet.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_div_vegetation_a(self):
        cname = "NEO_div_vegetation_a"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NEO_div_vegetation_a.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_div_vegetation_a_r(self):
        cname = "NEO_div_vegetation_a_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NEO_div_vegetation_a.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_div_vegetation_b(self):
        cname = "NEO_div_vegetation_b"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NEO_div_vegetation_b.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_div_vegetation_b_r(self):
        cname = "NEO_div_vegetation_b_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NEO_div_vegetation_b.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_div_vegetation_c(self):
        cname = "NEO_div_vegetation_c"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NEO_div_vegetation_c.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_div_vegetation_c_r(self):
        cname = "NEO_div_vegetation_c_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NEO_div_vegetation_c.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_modis_ndvi(self):
        cname = "NEO_modis_ndvi"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NEO_modis_ndvi.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_modis_ndvi_r(self):
        cname = "NEO_modis_ndvi_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NEO_modis_ndvi.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NMCRef(self):
        cname = "NMCRef"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NMCRef.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NMCRef_r(self):
        cname = "NMCRef_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NMCRef.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NMCVel(self):
        cname = "NMCVel"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NMCVel.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NMCVel_r(self):
        cname = "NMCVel_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NMCVel.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NOC_ndvi(self):
        cname = "NOC_ndvi"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NOC_ndvi.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NOC_ndvi_r(self):
        cname = "NOC_ndvi_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "NOC_ndvi.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def OceanLakeLandSnow(self):
        cname = "OceanLakeLandSnow"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "OceanLakeLandSnow.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def OceanLakeLandSnow_r(self):
        cname = "OceanLakeLandSnow_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "OceanLakeLandSnow.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def SVG_Gallet13(self):
        cname = "SVG_Gallet13"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "SVG_Gallet13.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def SVG_Gallet13_r(self):
        cname = "SVG_Gallet13_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "SVG_Gallet13.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def SVG_Lindaa06(self):
        cname = "SVG_Lindaa06"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "SVG_Lindaa06.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def SVG_Lindaa06_r(self):
        cname = "SVG_Lindaa06_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "SVG_Lindaa06.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def SVG_Lindaa07(self):
        cname = "SVG_Lindaa07"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "SVG_Lindaa07.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def SVG_Lindaa07_r(self):
        cname = "SVG_Lindaa07_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "SVG_Lindaa07.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def SVG_bhw3_22(self):
        cname = "SVG_bhw3_22"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "SVG_bhw3_22.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def SVG_bhw3_22_r(self):
        cname = "SVG_bhw3_22_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "SVG_bhw3_22.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def SVG_es_landscape_79(self):
        cname = "SVG_es_landscape_79"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "SVG_es_landscape_79.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def SVG_es_landscape_79_r(self):
        cname = "SVG_es_landscape_79_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "SVG_es_landscape_79.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def SVG_feb_sunrise(self):
        cname = "SVG_feb_sunrise"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "SVG_feb_sunrise.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def SVG_feb_sunrise_r(self):
        cname = "SVG_feb_sunrise_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "SVG_feb_sunrise.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def SVG_foggy_sunrise(self):
        cname = "SVG_foggy_sunrise"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "SVG_foggy_sunrise.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def SVG_foggy_sunrise_r(self):
        cname = "SVG_foggy_sunrise_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "SVG_foggy_sunrise.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def SVG_fs2006(self):
        cname = "SVG_fs2006"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "SVG_fs2006.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def SVG_fs2006_r(self):
        cname = "SVG_fs2006_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "SVG_fs2006.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def StepSeq25(self):
        cname = "StepSeq25"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "StepSeq25.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def StepSeq25_r(self):
        cname = "StepSeq25_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "StepSeq25.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def UKM_hadcrut(self):
        cname = "UKM_hadcrut"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "UKM_hadcrut_10.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def UKM_hadcrut_r(self):
        cname = "UKM_hadcrut_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "UKM_hadcrut_10.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def ViBlGrWhYeOrRe(self):
        cname = "ViBlGrWhYeOrRe"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "ViBlGrWhYeOrRe.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def ViBlGrWhYeOrRe_r(self):
        cname = "ViBlGrWhYeOrRe_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "ViBlGrWhYeOrRe.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def WhBlGrYeRe(self):
        cname = "WhBlGrYeRe"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "WhBlGrYeRe.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def WhBlGrYeRe_r(self):
        cname = "WhBlGrYeRe_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "WhBlGrYeRe.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def WhBlReWh(self):
        cname = "WhBlReWh"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "WhBlReWh.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def WhBlReWh_r(self):
        cname = "WhBlReWh_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "WhBlReWh.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def WhViBlGrYeOrRe(self):
        cname = "WhViBlGrYeOrRe"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "WhViBlGrYeOrRe.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def WhViBlGrYeOrRe_r(self):
        cname = "WhViBlGrYeOrRe_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "WhViBlGrYeOrRe.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def WhViBlGrYeOrReWh(self):
        cname = "WhViBlGrYeOrReWh"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "WhViBlGrYeOrReWh.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def WhViBlGrYeOrReWh_r(self):
        cname = "WhViBlGrYeOrReWh_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "WhViBlGrYeOrReWh.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def WhiteBlue(self):
        cname = "WhiteBlue"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "WhiteBlue.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def WhiteBlue_r(self):
        cname = "WhiteBlue_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "WhiteBlue.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def WhiteBlueGreenYellowRed(self):
        cname = "WhiteBlueGreenYellowRed"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "WhiteBlueGreenYellowRed.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def WhiteBlueGreenYellowRed_r(self):
        cname = "WhiteBlueGreenYellowRed_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "WhiteBlueGreenYellowRed.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def WhiteGreen(self):
        cname = "WhiteGreen"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "WhiteGreen.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def WhiteGreen_r(self):
        cname = "WhiteGreen_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "WhiteGreen.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def WhiteYellowOrangeRed(self):
        cname = "WhiteYellowOrangeRed"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "WhiteYellowOrangeRed.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def WhiteYellowOrangeRed_r(self):
        cname = "WhiteYellowOrangeRed_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "WhiteYellowOrangeRed.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def amwg(self):
        cname = "amwg"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "amwg.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def amwg_r(self):
        cname = "amwg_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "amwg.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def amwg256(self):
        cname = "amwg256"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "amwg256.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def amwg256_r(self):
        cname = "amwg256_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "amwg256.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def amwg_blueyellowred(self):
        cname = "amwg_blueyellowred"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "amwg_blueyellowred.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def amwg_blueyellowred_r(self):
        cname = "amwg_blueyellowred_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "amwg_blueyellowred.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cb_9step(self):
        cname = "cb_9step"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cb_9step.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cb_9step_r(self):
        cname = "cb_9step_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cb_9step.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cb_rainbow(self):
        cname = "cb_rainbow"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cb_rainbow.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cb_rainbow_r(self):
        cname = "cb_rainbow_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cb_rainbow.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cb_rainbow_inv(self):
        cname = "cb_rainbow_inv"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cb_rainbow_inv.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cb_rainbow_inv_r(self):
        cname = "cb_rainbow_inv_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cb_rainbow_inv.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def circular_0(self):
        cname = "circular_0"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "circular_0.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def circular_0_r(self):
        cname = "circular_0_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "circular_0.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def circular_1(self):
        cname = "circular_1"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "circular_1.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def circular_1_r(self):
        cname = "circular_1_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "circular_1.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def circular_2(self):
        cname = "circular_2"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "circular_2.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def circular_2_r(self):
        cname = "circular_2_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "circular_2.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cividis(self):
        cname = "cividis"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cividis.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cividis_r(self):
        cname = "cividis_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cividis.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_algae(self):
        cname = "cmocean_algae"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_algae.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_algae_r(self):
        cname = "cmocean_algae_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_algae.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_amp(self):
        cname = "cmocean_amp"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_amp.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_amp_r(self):
        cname = "cmocean_amp_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_amp.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_balance(self):
        cname = "cmocean_balance"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_balance.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_balance_r(self):
        cname = "cmocean_balance_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_balance.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_curl(self):
        cname = "cmocean_curl"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_curl.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_curl_r(self):
        cname = "cmocean_curl_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_curl.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_deep(self):
        cname = "cmocean_deep"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_deep.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_deep_r(self):
        cname = "cmocean_deep_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_deep.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_delta(self):
        cname = "cmocean_delta"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_delta.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_delta_r(self):
        cname = "cmocean_delta_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_delta.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_dense(self):
        cname = "cmocean_dense"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_dense.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_dense_r(self):
        cname = "cmocean_dense_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_dense.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_gray(self):
        cname = "cmocean_gray"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_gray.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_gray_r(self):
        cname = "cmocean_gray_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_gray.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_haline(self):
        cname = "cmocean_haline"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_haline.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_haline_r(self):
        cname = "cmocean_haline_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_haline.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_ice(self):
        cname = "cmocean_ice"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_ice.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_ice_r(self):
        cname = "cmocean_ice_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_ice.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_matter(self):
        cname = "cmocean_matter"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_matter.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_matter_r(self):
        cname = "cmocean_matter_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_matter.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_oxy(self):
        cname = "cmocean_oxy"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_oxy.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_oxy_r(self):
        cname = "cmocean_oxy_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_oxy.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_phase(self):
        cname = "cmocean_phase"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_phase.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_phase_r(self):
        cname = "cmocean_phase_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_phase.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_solar(self):
        cname = "cmocean_solar"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_solar.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_solar_r(self):
        cname = "cmocean_solar_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_solar.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_speed(self):
        cname = "cmocean_speed"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_speed.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_speed_r(self):
        cname = "cmocean_speed_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_speed.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_tempo(self):
        cname = "cmocean_tempo"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_tempo.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_tempo_r(self):
        cname = "cmocean_tempo_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_tempo.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_thermal(self):
        cname = "cmocean_thermal"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_thermal.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_thermal_r(self):
        cname = "cmocean_thermal_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_thermal.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_turbid(self):
        cname = "cmocean_turbid"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_turbid.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmocean_turbid_r(self):
        cname = "cmocean_turbid_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmocean_turbid.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmp_b2r(self):
        cname = "cmp_b2r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmp_b2r.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmp_b2r_r(self):
        cname = "cmp_b2r_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmp_b2r.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmp_flux(self):
        cname = "cmp_flux"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmp_flux.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmp_flux_r(self):
        cname = "cmp_flux_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmp_flux.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmp_haxby(self):
        cname = "cmp_haxby"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmp_haxby.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmp_haxby_r(self):
        cname = "cmp_haxby_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cmp_haxby.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cosam(self):
        cname = "cosam"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cosam.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cosam_r(self):
        cname = "cosam_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cosam.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cosam12(self):
        cname = "cosam12"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cosam12.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cosam12_r(self):
        cname = "cosam12_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cosam12.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cyclic(self):
        cname = "cyclic"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cyclic.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cyclic_r(self):
        cname = "cyclic_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "cyclic.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def default(self):
        cname = "default"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "default.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def default_r(self):
        cname = "default_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "default.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def detail(self):
        cname = "detail"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "detail.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def detail_r(self):
        cname = "detail_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "detail.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def drought_severity(self):
        cname = "drought_severity"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "drought_severity.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def drought_severity_r(self):
        cname = "drought_severity_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "drought_severity.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def example(self):
        cname = "example"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "example.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def example_r(self):
        cname = "example_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "example.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def extrema(self):
        cname = "extrema"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "extrema.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def extrema_r(self):
        cname = "extrema_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "extrema.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def grads_default(self):
        cname = "grads_default"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "grads_default.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def grads_default_r(self):
        cname = "grads_default_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "grads_default.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def grads_rainbow(self):
        cname = "grads_rainbow"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "grads_rainbow.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def grads_rainbow_r(self):
        cname = "grads_rainbow_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "grads_rainbow.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def gscyclic(self):
        cname = "gscyclic"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "gscyclic.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def gscyclic_r(self):
        cname = "gscyclic_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "gscyclic.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def gsdtol(self):
        cname = "gsdtol"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "gsdtol.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def gsdtol_r(self):
        cname = "gsdtol_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "gsdtol.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def gsltod(self):
        cname = "gsltod"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "gsltod.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def gsltod_r(self):
        cname = "gsltod_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "gsltod.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def gui_default(self):
        cname = "gui_default"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "gui_default.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def gui_default_r(self):
        cname = "gui_default_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "gui_default.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def helix(self):
        cname = "helix"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "helix.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def helix_r(self):
        cname = "helix_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "helix.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def helix1(self):
        cname = "helix1"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "helix1.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def helix1_r(self):
        cname = "helix1_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "helix1.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def hlu_default(self):
        cname = "hlu_default"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "hlu_default.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def hlu_default_r(self):
        cname = "hlu_default_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "hlu_default.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def hotcold_18lev(self):
        cname = "hotcold_18lev"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "hotcold_18lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def hotcold_18lev_r(self):
        cname = "hotcold_18lev_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "hotcold_18lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def hotcolr_19lev(self):
        cname = "hotcolr_19lev"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "hotcolr_19lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def hotcolr_19lev_r(self):
        cname = "hotcolr_19lev_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "hotcolr_19lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def hotres(self):
        cname = "hotres"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "hotres.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def hotres_r(self):
        cname = "hotres_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "hotres.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def lithology(self):
        cname = "lithology"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "lithology.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def lithology_r(self):
        cname = "lithology_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "lithology.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def matlab_hot(self):
        cname = "matlab_hot"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "matlab_hot.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def matlab_hot_r(self):
        cname = "matlab_hot_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "matlab_hot.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def matlab_hsv(self):
        cname = "matlab_hsv"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "matlab_hsv.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def matlab_hsv_r(self):
        cname = "matlab_hsv_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "matlab_hsv.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def matlab_jet(self):
        cname = "matlab_jet"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "matlab_jet.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def matlab_jet_r(self):
        cname = "matlab_jet_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "matlab_jet.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def matlab_lines(self):
        cname = "matlab_lines"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "matlab_lines.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def matlab_lines_r(self):
        cname = "matlab_lines_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "matlab_lines.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def mch_default(self):
        cname = "mch_default"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "mch_default.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def mch_default_r(self):
        cname = "mch_default_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "mch_default.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def ncl_default(self):
        cname = "ncl_default"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "ncl_default.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def ncl_default_r(self):
        cname = "ncl_default_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "ncl_default.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def ncview_default(self):
        cname = "ncview_default"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "ncview_default.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def ncview_default_r(self):
        cname = "ncview_default_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "ncview_default.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def nice_gfdl(self):
        cname = "nice_gfdl"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "nice_gfdl.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def nice_gfdl_r(self):
        cname = "nice_gfdl_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "nice_gfdl.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def nrl_sirkes(self):
        cname = "nrl_sirkes"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "nrl_sirkes.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def nrl_sirkes_r(self):
        cname = "nrl_sirkes_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "nrl_sirkes.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def nrl_sirkes_nowhite(self):
        cname = "nrl_sirkes_nowhite"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "nrl_sirkes_nowhite.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def nrl_sirkes_nowhite_r(self):
        cname = "nrl_sirkes_nowhite_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "nrl_sirkes_nowhite.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def perc2_9lev(self):
        cname = "perc2_9lev"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "perc2_9lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def perc2_9lev_r(self):
        cname = "perc2_9lev_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "perc2_9lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def percent_11lev(self):
        cname = "percent_11lev"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "percent_11lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def percent_11lev_r(self):
        cname = "percent_11lev_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "percent_11lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def posneg_1(self):
        cname = "posneg_1"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "posneg_1.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def posneg_1_r(self):
        cname = "posneg_1_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "posneg_1.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def posneg_2(self):
        cname = "posneg_2"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "posneg_2.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def posneg_2_r(self):
        cname = "posneg_2_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "posneg_2.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def prcp_1(self):
        cname = "prcp_1"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "prcp_1.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def prcp_1_r(self):
        cname = "prcp_1_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "prcp_1.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def prcp_2(self):
        cname = "prcp_2"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "prcp_2.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def prcp_2_r(self):
        cname = "prcp_2_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "prcp_2.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def prcp_3(self):
        cname = "prcp_3"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "prcp_3.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def prcp_3_r(self):
        cname = "prcp_3_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "prcp_3.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def precip2_15lev(self):
        cname = "precip2_15lev"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "precip2_15lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def precip2_15lev_r(self):
        cname = "precip2_15lev_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "precip2_15lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def precip2_17lev(self):
        cname = "precip2_17lev"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "precip2_17lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def precip2_17lev_r(self):
        cname = "precip2_17lev_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "precip2_17lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def precip3_16lev(self):
        cname = "precip3_16lev"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "precip3_16lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def precip3_16lev_r(self):
        cname = "precip3_16lev_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "precip3_16lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def precip4_11lev(self):
        cname = "precip4_11lev"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "precip4_11lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def precip4_11lev_r(self):
        cname = "precip4_11lev_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "precip4_11lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def precip4_diff_19lev(self):
        cname = "precip4_diff_19lev"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "precip4_diff_19lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def precip4_diff_19lev_r(self):
        cname = "precip4_diff_19lev_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "precip4_diff_19lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def precip_11lev(self):
        cname = "precip_11lev"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "precip_11lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def precip_11lev_r(self):
        cname = "precip_11lev_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "precip_11lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def precip_diff_12lev(self):
        cname = "precip_diff_12lev"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "precip_diff_12lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def precip_diff_12lev_r(self):
        cname = "precip_diff_12lev_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "precip_diff_12lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def precip_diff_1lev(self):
        cname = "precip_diff_1lev"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "precip_diff_1lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def precip_diff_1lev_r(self):
        cname = "precip_diff_1lev_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "precip_diff_1lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def psgcap(self):
        cname = "psgcap"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "psgcap.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def psgcap_r(self):
        cname = "psgcap_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "psgcap.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def radar(self):
        cname = "radar"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "radar.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def radar_r(self):
        cname = "radar_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "radar.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def radar_1(self):
        cname = "radar_1"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "radar_1.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def radar_1_r(self):
        cname = "radar_1_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "radar_1.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmaps_rainbow_gray(self):
        cname = "cmaps_rainbow_gray"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "rainbow+gray.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmaps_rainbow_gray_r(self):
        cname = "cmaps_rainbow_gray_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "rainbow+gray.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmaps_rainbow_white_gray(self):
        cname = "cmaps_rainbow_white_gray"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "rainbow+white+gray.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmaps_rainbow_white_gray_r(self):
        cname = "cmaps_rainbow_white_gray_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "rainbow+white+gray.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmaps_rainbow_white(self):
        cname = "cmaps_rainbow_white"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "rainbow+white.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmaps_rainbow_white_r(self):
        cname = "cmaps_rainbow_white_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "rainbow+white.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def rainbow(self):
        cname = "rainbow"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "rainbow.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def rainbow_r(self):
        cname = "rainbow_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "rainbow.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def rh_19lev(self):
        cname = "rh_19lev"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "rh_19lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def rh_19lev_r(self):
        cname = "rh_19lev_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "rh_19lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def seaice_1(self):
        cname = "seaice_1"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "seaice_1.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def seaice_1_r(self):
        cname = "seaice_1_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "seaice_1.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def seaice_2(self):
        cname = "seaice_2"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "seaice_2.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def seaice_2_r(self):
        cname = "seaice_2_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "seaice_2.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def so4_21(self):
        cname = "so4_21"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "so4_21.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def so4_21_r(self):
        cname = "so4_21_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "so4_21.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def so4_23(self):
        cname = "so4_23"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "so4_23.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def so4_23_r(self):
        cname = "so4_23_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "so4_23.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def spread_15lev(self):
        cname = "spread_15lev"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "spread_15lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def spread_15lev_r(self):
        cname = "spread_15lev_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "spread_15lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def srip_reanalysis(self):
        cname = "srip_reanalysis"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "srip_reanalysis.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def srip_reanalysis_r(self):
        cname = "srip_reanalysis_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "srip_reanalysis.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def sunshine_9lev(self):
        cname = "sunshine_9lev"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "sunshine_9lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def sunshine_9lev_r(self):
        cname = "sunshine_9lev_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "sunshine_9lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def sunshine_diff_12lev(self):
        cname = "sunshine_diff_12lev"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "sunshine_diff_12lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def sunshine_diff_12lev_r(self):
        cname = "sunshine_diff_12lev_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "sunshine_diff_12lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def t2m_29lev(self):
        cname = "t2m_29lev"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "t2m_29lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def t2m_29lev_r(self):
        cname = "t2m_29lev_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "t2m_29lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def tbrAvg1(self):
        cname = "tbrAvg1"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "tbrAvg1.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def tbrAvg1_r(self):
        cname = "tbrAvg1_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "tbrAvg1.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def tbrStd1(self):
        cname = "tbrStd1"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "tbrStd1.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def tbrStd1_r(self):
        cname = "tbrStd1_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "tbrStd1.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def tbrVar1(self):
        cname = "tbrVar1"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "tbrVar1.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def tbrVar1_r(self):
        cname = "tbrVar1_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "tbrVar1.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmaps_tbr_240_300(self):
        cname = "cmaps_tbr_240_300"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "tbr_240-300.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmaps_tbr_240_300_r(self):
        cname = "cmaps_tbr_240_300_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "tbr_240-300.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmaps_tbr_stdev_0_30(self):
        cname = "cmaps_tbr_stdev_0_30"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "tbr_stdev_0-30.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmaps_tbr_stdev_0_30_r(self):
        cname = "cmaps_tbr_stdev_0_30_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "tbr_stdev_0-30.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmaps_tbr_var_0_500(self):
        cname = "cmaps_tbr_var_0_500"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "tbr_var_0-500.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmaps_tbr_var_0_500_r(self):
        cname = "cmaps_tbr_var_0_500_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "tbr_var_0-500.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def temp1(self):
        cname = "temp1"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "temp1.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def temp1_r(self):
        cname = "temp1_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "temp1.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def temp_19lev(self):
        cname = "temp_19lev"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "temp_19lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def temp_19lev_r(self):
        cname = "temp_19lev_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "temp_19lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def temp_diff_18lev(self):
        cname = "temp_diff_18lev"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "temp_diff_18lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def temp_diff_18lev_r(self):
        cname = "temp_diff_18lev_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "temp_diff_18lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def temp_diff_1lev(self):
        cname = "temp_diff_1lev"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "temp_diff_1lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def temp_diff_1lev_r(self):
        cname = "temp_diff_1lev_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "temp_diff_1lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def testcmap(self):
        cname = "testcmap"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "testcmap.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def testcmap_r(self):
        cname = "testcmap_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "testcmap.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def thelix(self):
        cname = "thelix"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "thelix.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def thelix_r(self):
        cname = "thelix_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "thelix.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def topo_15lev(self):
        cname = "topo_15lev"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "topo_15lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def topo_15lev_r(self):
        cname = "topo_15lev_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "topo_15lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def uniform(self):
        cname = "uniform"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "uniform.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def uniform_r(self):
        cname = "uniform_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "uniform.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def vegetation_ClarkU(self):
        cname = "vegetation_ClarkU"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "vegetation_ClarkU.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def vegetation_ClarkU_r(self):
        cname = "vegetation_ClarkU_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "vegetation_ClarkU.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def vegetation_modis(self):
        cname = "vegetation_modis"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "vegetation_modis.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def vegetation_modis_r(self):
        cname = "vegetation_modis_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "vegetation_modis.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def wgne15(self):
        cname = "wgne15"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "wgne15.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def wgne15_r(self):
        cname = "wgne15_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "wgne15.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmaps_wh_bl_gr_ye_re(self):
        cname = "cmaps_wh_bl_gr_ye_re"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "wh-bl-gr-ye-re.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def cmaps_wh_bl_gr_ye_re_r(self):
        cname = "cmaps_wh_bl_gr_ye_re_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "wh-bl-gr-ye-re.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def wind_17lev(self):
        cname = "wind_17lev"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "wind_17lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def wind_17lev_r(self):
        cname = "wind_17lev_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "wind_17lev.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def wxpEnIR(self):
        cname = "wxpEnIR"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "wxpEnIR.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def wxpEnIR_r(self):
        cname = "wxpEnIR_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl", "wxpEnIR.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def Carbone42(self):
        cname = "Carbone42"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "Carbone42.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def Carbone42_r(self):
        cname = "Carbone42_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "Carbone42.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NMCRef(self):
        cname = "NMCRef"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NMCRef.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NMCRef_r(self):
        cname = "NMCRef_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NMCRef.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NMCVel2(self):
        cname = "NMCVel2"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NMCVel2.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NMCVel2_r(self):
        cname = "NMCVel2_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NMCVel2.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NWSRef(self):
        cname = "NWSRef"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NWSRef.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NWSRef_r(self):
        cname = "NWSRef_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NWSRef.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NWSSPW(self):
        cname = "NWSSPW"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NWSSPW.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NWSSPW_r(self):
        cname = "NWSSPW_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NWSSPW.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NWSVel(self):
        cname = "NWSVel"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NWSVel.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NWSVel_r(self):
        cname = "NWSVel_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NWSVel.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def TopoGray(self):
        cname = "TopoGray"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "TopoGray.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def TopoGray_r(self):
        cname = "TopoGray_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "TopoGray.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def TwoClass(self):
        cname = "TwoClass"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "TwoClass.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def TwoClass_r(self):
        cname = "TwoClass_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "TwoClass.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def mask(self):
        cname = "mask"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "mask.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def mask_r(self):
        cname = "mask_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "mask.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_seis(self):
        cname = "GMT_seis"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "GMT_seis.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_seis_r(self):
        cname = "GMT_seis_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "GMT_seis.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_relief(self):
        cname = "GMT_relief"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "GMT_relief.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_relief_r(self):
        cname = "GMT_relief_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "GMT_relief.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_earth(self):
        cname = "GMT_earth"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "GMT_earth.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_earth_r(self):
        cname = "GMT_earth_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "GMT_earth.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NYT_drought(self):
        cname = "NYT_drought"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NYT_drought.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NYT_drought_r(self):
        cname = "NYT_drought_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NYT_drought.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def UKM_hadcrut_10(self):
        cname = "UKM_hadcrut_10"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "UKM_hadcrut_10.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def UKM_hadcrut_10_r(self):
        cname = "UKM_hadcrut_10_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "UKM_hadcrut_10.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def SVS_tempanomaly(self):
        cname = "SVS_tempanomaly"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "SVS_tempanomaly.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def SVS_tempanomaly_r(self):
        cname = "SVS_tempanomaly_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "SVS_tempanomaly.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_split(self):
        cname = "GMT_split"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "GMT_split.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_split_r(self):
        cname = "GMT_split_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "GMT_split.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def EO_aura_omi_formal(self):
        cname = "EO_aura_omi_formal"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "EO_aura_omi_formal.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def EO_aura_omi_formal_r(self):
        cname = "EO_aura_omi_formal_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "EO_aura_omi_formal.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def EO_carbon_density(self):
        cname = "EO_carbon_density"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "EO_carbon_density.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def EO_carbon_density_r(self):
        cname = "EO_carbon_density_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "EO_carbon_density.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def EO_lightning_lis_otd(self):
        cname = "EO_lightning_lis_otd"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "EO_lightning_lis_otd.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def EO_lightning_lis_otd_r(self):
        cname = "EO_lightning_lis_otd_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "EO_lightning_lis_otd.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def EO_sargassum_tamo(self):
        cname = "EO_sargassum_tamo"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "EO_sargassum_tamo.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def EO_sargassum_tamo_r(self):
        cname = "EO_sargassum_tamo_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "EO_sargassum_tamo.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def EO_soil_moist_div(self):
        cname = "EO_soil_moist_div"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "EO_soil_moist_div.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def EO_soil_moist_div_r(self):
        cname = "EO_soil_moist_div_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "EO_soil_moist_div.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def EO_temp_anom_4(self):
        cname = "EO_temp_anom_4"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "EO_temp_anom_4.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def EO_temp_anom_4_r(self):
        cname = "EO_temp_anom_4_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "EO_temp_anom_4.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def EVL_wind_anom(self):
        cname = "EVL_wind_anom"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "EVL_wind_anom.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def EVL_wind_anom_r(self):
        cname = "EVL_wind_anom_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "EVL_wind_anom.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GISS_isccp_rainbow(self):
        cname = "GISS_isccp_rainbow"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "GISS_isccp_rainbow.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GISS_isccp_rainbow_r(self):
        cname = "GISS_isccp_rainbow_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "GISS_isccp_rainbow.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GISS_isccp_rainbow_20(self):
        cname = "GISS_isccp_rainbow_20"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "GISS_isccp_rainbow_20.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GISS_isccp_rainbow_20_r(self):
        cname = "GISS_isccp_rainbow_20_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "GISS_isccp_rainbow_20.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_seis_20(self):
        cname = "GMT_seis_20"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "GMT_seis_20.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def GMT_seis_20_r(self):
        cname = "GMT_seis_20_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "GMT_seis_20.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MRO_ice_freq(self):
        cname = "MRO_ice_freq"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "MRO_ice_freq.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def MRO_ice_freq_r(self):
        cname = "MRO_ice_freq_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "MRO_ice_freq.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NCDC_snow_anom(self):
        cname = "NCDC_snow_anom"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NCDC_snow_anom.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NCDC_snow_anom_r(self):
        cname = "NCDC_snow_anom_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NCDC_snow_anom.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NCDC_temp_anom_f(self):
        cname = "NCDC_temp_anom_f"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NCDC_temp_anom_f.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NCDC_temp_anom_f_r(self):
        cname = "NCDC_temp_anom_f_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NCDC_temp_anom_f.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_albedo_change(self):
        cname = "NEO_albedo_change"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_albedo_change.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_albedo_change_r(self):
        cname = "NEO_albedo_change_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_albedo_change.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_amsre_ss(self):
        cname = "NEO_amsre_ss"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_amsre_ss.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_amsre_ss_r(self):
        cname = "NEO_amsre_ss_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_amsre_ss.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_amsre_sst_anom(self):
        cname = "NEO_amsre_sst_anom"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_amsre_sst_anom.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_amsre_sst_anom_r(self):
        cname = "NEO_amsre_sst_anom_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_amsre_sst_anom.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_aod_diff(self):
        cname = "NEO_aod_diff"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_aod_diff.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_aod_diff_r(self):
        cname = "NEO_aod_diff_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_aod_diff.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_aquarius_sss(self):
        cname = "NEO_aquarius_sss"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_aquarius_sss.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_aquarius_sss_r(self):
        cname = "NEO_aquarius_sss_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_aquarius_sss.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_bright_temp(self):
        cname = "NEO_bright_temp"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_bright_temp.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_bright_temp_r(self):
        cname = "NEO_bright_temp_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_bright_temp.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_carb_emit_anom(self):
        cname = "NEO_carb_emit_anom"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_carb_emit_anom.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_carb_emit_anom_r(self):
        cname = "NEO_carb_emit_anom_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_carb_emit_anom.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_cdom(self):
        cname = "NEO_cdom"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_cdom.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_cdom_r(self):
        cname = "NEO_cdom_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_cdom.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_ceres_insol(self):
        cname = "NEO_ceres_insol"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_ceres_insol.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_ceres_insol_r(self):
        cname = "NEO_ceres_insol_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_ceres_insol.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_ceres_lw(self):
        cname = "NEO_ceres_lw"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_ceres_lw.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_ceres_lw_r(self):
        cname = "NEO_ceres_lw_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_ceres_lw.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_ceres_ne(self):
        cname = "NEO_ceres_ne"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_ceres_ne.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_ceres_ne_r(self):
        cname = "NEO_ceres_ne_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_ceres_ne.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_ceres_sw(self):
        cname = "NEO_ceres_sw"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_ceres_sw.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_ceres_sw_r(self):
        cname = "NEO_ceres_sw_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_ceres_sw.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_chlorophyll(self):
        cname = "NEO_chlorophyll"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_chlorophyll.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_chlorophyll_r(self):
        cname = "NEO_chlorophyll_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_chlorophyll.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_chlorophyll_o(self):
        cname = "NEO_chlorophyll_o"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_chlorophyll_o.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_chlorophyll_o_r(self):
        cname = "NEO_chlorophyll_o_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_chlorophyll_o.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_div_vegetation_(self):
        cname = "NEO_div_vegetation_"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_div_vegetation_.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_div_vegetation__r(self):
        cname = "NEO_div_vegetation__r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_div_vegetation_.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_evapstress(self):
        cname = "NEO_evapstress"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_evapstress.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_evapstress_r(self):
        cname = "NEO_evapstress_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_evapstress.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_gebco_bathymetry(self):
        cname = "NEO_gebco_bathymetry"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_gebco_bathymetry.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_gebco_bathymetry_r(self):
        cname = "NEO_gebco_bathymetry_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_gebco_bathymetry.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_ggmcf(self):
        cname = "NEO_ggmcf"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_ggmcf.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_ggmcf_r(self):
        cname = "NEO_ggmcf_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_ggmcf.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_giss_temp_anom(self):
        cname = "NEO_giss_temp_anom"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_giss_temp_anom.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_giss_temp_anom_r(self):
        cname = "NEO_giss_temp_anom_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_giss_temp_anom.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_grace_lwe_anom(self):
        cname = "NEO_grace_lwe_anom"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_grace_lwe_anom.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_grace_lwe_anom_r(self):
        cname = "NEO_grace_lwe_anom_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_grace_lwe_anom.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_grav_anom(self):
        cname = "NEO_grav_anom"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_grav_anom.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_grav_anom_r(self):
        cname = "NEO_grav_anom_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_grav_anom.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_imperv_surf(self):
        cname = "NEO_imperv_surf"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_imperv_surf.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_imperv_surf_r(self):
        cname = "NEO_imperv_surf_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_imperv_surf.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_meltseason_anom(self):
        cname = "NEO_meltseason_anom"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_meltseason_anom.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_meltseason_anom_r(self):
        cname = "NEO_meltseason_anom_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_meltseason_anom.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_modis_aer_od(self):
        cname = "NEO_modis_aer_od"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_modis_aer_od.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_modis_aer_od_r(self):
        cname = "NEO_modis_aer_od_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_modis_aer_od.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_modis_bs_albedo(self):
        cname = "NEO_modis_bs_albedo"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_modis_bs_albedo.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_modis_bs_albedo_r(self):
        cname = "NEO_modis_bs_albedo_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_modis_bs_albedo.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_modis_chlor(self):
        cname = "NEO_modis_chlor"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_modis_chlor.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_modis_chlor_r(self):
        cname = "NEO_modis_chlor_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_modis_chlor.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_modis_cld_ci(self):
        cname = "NEO_modis_cld_ci"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_modis_cld_ci.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_modis_cld_ci_r(self):
        cname = "NEO_modis_cld_ci_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_modis_cld_ci.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_modis_cld_fr(self):
        cname = "NEO_modis_cld_fr"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_modis_cld_fr.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_modis_cld_fr_r(self):
        cname = "NEO_modis_cld_fr_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_modis_cld_fr.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_modis_cld_o(self):
        cname = "NEO_modis_cld_o"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_modis_cld_o.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_modis_cld_o_r(self):
        cname = "NEO_modis_cld_o_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_modis_cld_o.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_modis_cld_rd(self):
        cname = "NEO_modis_cld_rd"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_modis_cld_rd.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_modis_cld_rd_r(self):
        cname = "NEO_modis_cld_rd_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_modis_cld_rd.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_modis_cld_wp(self):
        cname = "NEO_modis_cld_wp"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_modis_cld_wp.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_modis_cld_wp_r(self):
        cname = "NEO_modis_cld_wp_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_modis_cld_wp.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_modis_ls(self):
        cname = "NEO_modis_ls"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_modis_ls.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_modis_ls_r(self):
        cname = "NEO_modis_ls_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_modis_ls.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_modis_lst_anom(self):
        cname = "NEO_modis_lst_anom"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_modis_lst_anom.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_modis_lst_anom_r(self):
        cname = "NEO_modis_lst_anom_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_modis_lst_anom.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_modis_sky_wv(self):
        cname = "NEO_modis_sky_wv"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_modis_sky_wv.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_modis_sky_wv_r(self):
        cname = "NEO_modis_sky_wv_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_modis_sky_wv.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_modis_sst_45(self):
        cname = "NEO_modis_sst_45"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_modis_sst_45.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_modis_sst_45_r(self):
        cname = "NEO_modis_sst_45_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_modis_sst_45.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_mopitt_co(self):
        cname = "NEO_mopitt_co"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_mopitt_co.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_mopitt_co_r(self):
        cname = "NEO_mopitt_co_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_mopitt_co.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_ns_airtemp(self):
        cname = "NEO_ns_airtemp"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_ns_airtemp.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_ns_airtemp_r(self):
        cname = "NEO_ns_airtemp_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_ns_airtemp.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_omi_no2(self):
        cname = "NEO_omi_no2"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_omi_no2.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_omi_no2_r(self):
        cname = "NEO_omi_no2_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_omi_no2.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_omi_ozone_to3(self):
        cname = "NEO_omi_ozone_to3"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_omi_ozone_to3.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_omi_ozone_to3_r(self):
        cname = "NEO_omi_ozone_to3_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_omi_ozone_to3.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_omi_uvi(self):
        cname = "NEO_omi_uvi"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_omi_uvi.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_omi_uvi_r(self):
        cname = "NEO_omi_uvi_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_omi_uvi.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_pollution_conc_9(self):
        cname = "NEO_pollution_conc_9"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_pollution_conc_9.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_pollution_conc_9_r(self):
        cname = "NEO_pollution_conc_9_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_pollution_conc_9.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_pollution_mor(self):
        cname = "NEO_pollution_mor"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_pollution_mor.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_pollution_mor_r(self):
        cname = "NEO_pollution_mor_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_pollution_mor.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_rainfall_anom_9(self):
        cname = "NEO_rainfall_anom_9"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_rainfall_anom_9.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_rainfall_anom_9_r(self):
        cname = "NEO_rainfall_anom_9_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_rainfall_anom_9.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_seasurf_hgt_anom(self):
        cname = "NEO_seasurf_hgt_anom"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_seasurf_hgt_anom.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_seasurf_hgt_anom_r(self):
        cname = "NEO_seasurf_hgt_anom_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_seasurf_hgt_anom.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_sedac_pop(self):
        cname = "NEO_sedac_pop"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_sedac_pop.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_sedac_pop_r(self):
        cname = "NEO_sedac_pop_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_sedac_pop.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_snow_water(self):
        cname = "NEO_snow_water"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_snow_water.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_snow_water_r(self):
        cname = "NEO_snow_water_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_snow_water.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_soil_moisture(self):
        cname = "NEO_soil_moisture"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_soil_moisture.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_soil_moisture_r(self):
        cname = "NEO_soil_moisture_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_soil_moisture.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_soil_moisture_anom(self):
        cname = "NEO_soil_moisture_anom"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_soil_moisture_anom.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_soil_moisture_anom_r(self):
        cname = "NEO_soil_moisture_anom_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_soil_moisture_anom.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_soil_moisture_anom_nl(self):
        cname = "NEO_soil_moisture_anom_nl"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_soil_moisture_anom_nl.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_soil_moisture_anom_nl_r(self):
        cname = "NEO_soil_moisture_anom_nl_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_soil_moisture_anom_nl.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_soil_moisture_pale(self):
        cname = "NEO_soil_moisture_pale"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_soil_moisture_pale.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_soil_moisture_pale_r(self):
        cname = "NEO_soil_moisture_pale_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_soil_moisture_pale.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_srtm_topography(self):
        cname = "NEO_srtm_topography"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_srtm_topography.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_srtm_topography_r(self):
        cname = "NEO_srtm_topography_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_srtm_topography.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_tree_cover(self):
        cname = "NEO_tree_cover"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_tree_cover.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_tree_cover_r(self):
        cname = "NEO_tree_cover_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_tree_cover.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_trmm_rainfall(self):
        cname = "NEO_trmm_rainfall"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_trmm_rainfall.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_trmm_rainfall_r(self):
        cname = "NEO_trmm_rainfall_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_trmm_rainfall.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_wind_spd_anom(self):
        cname = "NEO_wind_spd_anom"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_wind_spd_anom.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_wind_spd_anom_r(self):
        cname = "NEO_wind_spd_anom_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_wind_spd_anom.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_wind_spd_anomaly_pwg(self):
        cname = "NEO_wind_spd_anomaly_pwg"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_wind_spd_anomaly_pwg.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def NEO_wind_spd_anomaly_pwg_r(self):
        cname = "NEO_wind_spd_anomaly_pwg_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "NEO_wind_spd_anomaly_pwg.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def SVS_soilmoisture(self):
        cname = "SVS_soilmoisture"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "SVS_soilmoisture.rgb")
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap

    @property
    def SVS_soilmoisture_r(self):
        cname = "SVS_soilmoisture_r"
        try:
            return get_cmap(cname)
        except:
            cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined", "SVS_soilmoisture.rgb")
            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
            register_cmap(name=cname, cmap=cmap)
            return cmap
