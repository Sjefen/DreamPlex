# -*- coding: utf-8 -*-
"""
DreamPlex Plugin by DonDavici, 2012
 
https://github.com/DonDavici/DreamPlex

Some of the code is from other plugins:
all credits to the coders :-)

DreamPlex Plugin is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

DreamPlex Plugin is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
"""
#===============================================================================
# IMPORT
#===============================================================================
from DP_LibMain import DP_LibMain

from DPH_Singleton import Singleton

from __common__ import printl2 as printl

#===============================================================================
# 
#===============================================================================
class DP_LibShows(DP_LibMain):

	#===========================================================================
	# 
	#===========================================================================
	def __init__(self, session, initalEntryData):
		printl ("", self, "S")

		self.initalEntryData = initalEntryData
		printl("initalEntryData: " + str(self.initalEntryData), self, "D")

		DP_LibMain.__init__(self, session, "tvshows")

		printl ("", self, "C")

	#===============================================================================
	# 
	#===============================================================================
	def loadLibrary(self, entryData = None):
		printl ("", self, "S")
		printl("entryData: " + str(entryData), self, "D")

		if entryData is None:
			entryData = self.initalEntryData

		url = entryData["contentUrl"]
		printl("url: " + str(url), self, "D")

		# Diplay all TVShows
		if "viewMode" not in entryData:
			showEpisodesDirectly = False

			if "showEpisodesDirectly" in entryData:
				if entryData["showEpisodesDirectly"]:
					showEpisodesDirectly = True

			if showEpisodesDirectly:
				printl("show episodes directly ...", self, "D")
				library, mediaContainer = Singleton().getPlexInstance().getEpisodesOfSeason(url, directMode=True)
			else:
				printl("show TV shows ...", self, "D")
				library, mediaContainer = Singleton().getPlexInstance().getShowsFromSection(url)

		# Display the Seasons Menu
		elif entryData["viewMode"] == "ShowSeasons":
			printl("show seasons of TV show ...", self, "D")
			library, mediaContainer = Singleton().getPlexInstance().getSeasonsOfShow(url)

		# Display the Episodes Menu
		elif entryData["viewMode"] == "ShowEpisodes":
			printl("show episodes of season ...", self, "D")
			library, mediaContainer = Singleton().getPlexInstance().getEpisodesOfSeason(url)

		printl ("", self, "C")
		return library, mediaContainer
