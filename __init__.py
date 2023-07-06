# -*- coding: utf-8 -*-
"""
/***************************************************************************
 telepacLoader
                                 A QGIS plugin
 Charger les xml issu de Télépac
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-27
        copyright            : (C) 2023 by Matthieu AUGUSTIN
        email                : mattaugustin48@gmail.com
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
    """Load telepacLoader class from file telepacLoader.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .telepacLoader import telepacLoader
    return telepacLoader(iface)
