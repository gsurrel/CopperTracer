#!/usr/bin/env python3

"""Built from the "Complex plugin example" from the KiCad documentation:
docs.kicad-pcb.org/doxygen/md_Documentation_development_pcbnew-plugins.html#ppi_complex_exam

> The `__init__.py` file is then used to instantiate and register the plugin to Pcbnew as follows.
"""

from .CopperTracer_action import CopperTracerAction # Note the relative import!
CopperTracerAction().register() # Instantiate and register to Pcbnew