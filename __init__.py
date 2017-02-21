# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Grim
                                 A QGIS plugin
 Analysing GRoyne Impacts on Morphology Script
                             -------------------
        begin                : 2017-02-17
        copyright            : (C) 2017 by Thomas Burke
        email                : thomasmns@outlook.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Grim class from file Grim.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .grim import Grim
    return Grim(iface)
