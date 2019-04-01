#!/usr/bin/env python3

"""Built from the "Complex plugin example" from the KiCad documentation:
docs.kicad-pcb.org/doxygen/md_Documentation_development_pcbnew-plugins.html#ppi_complex_exam

> It is recommended to name the file containing the ActionPlugin derived class as `<package-name>_action.py`.
"""


import pcbnew
import os

class CopperTracerAction(pcbnew.ActionPlugin):
	def defaults(self):
		self.name = "CopperTracer auto-router"
		self.category = "Routing"
		self.description = "Automatically route the tracks on the PCB using CopperTracer"
		self.show_toolbar_button = True
		self.icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png')

	def Run(self):
		# The entry function of the plugin that is executed on user action
		print("Hello World")
