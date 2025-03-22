import os


class renamer:

	def __init__(self):
		self.JellyfinStyle = "{name} S{season}E{episode}{extension}"
		inputlocation = "./inputFiles"
		outputlocation = "./outputFiles"

		AbsoluteInputPath = os.path.join(os.getcwd(),inputlocation)
		AbsoluteOutputPath = os.path.join(os.getcwd(),outputlocation)
		self.AbsoluteInputPath = os.path.abspath(AbsoluteInputPath)
		self.AbsoluteOutputPath = os.path.abspath(AbsoluteOutputPath)

		if not os.path.exists(self.AbsoluteInputPath):
			os.mkdir(self.AbsoluteInputPath)
		if not os.path.exists(self.AbsoluteOutputPath):
			os.mkdir(self.AbsoluteOutputPath)


	def main(self):
		print("renamer started!")
		showName = input("what is the show called?: ")

		AbsInputFiles = self.GetInputFiles()
		AbsOutputFiles = []

		for file in AbsInputFiles:
			print(file)
			FileEpisode = self.FindEpisodeInName(file)
			FileSeason = self.FindSeasonInName(file)
			FileExtension = self.FindExtensionInName(file)
			AbsOutputFiles.append( self.renameAndMoveFile(file,showName,FileEpisode,FileSeason,FileExtension) )
		for file in AbsOutputFiles:
			print(file)
		print(f"renamed and moved { len(AbsInputFiles) } files!")

	#returns a two char long string of number: 01,02 ...
	def FindEpisodeInName(self, AbsoluteFilePath):
		file = AbsoluteFilePath.split("/")
		file = file[ len(file) - 1 ]
		episode = "00"
		print(f"Episode is: {episode}")
		return episode

	def FindSeasonInName(self, AbsoluteFilePath):
		file = AbsoluteFilePath.split("/")
		file = file[ len(file) - 1 ]
		season ="00"
		print(f"season is: {season}")
		return season

	def FindExtensionInName(self, AbsoluteFilePath):
		file = AbsoluteFilePath.split("/")
		list = file[len(file) - 1].split(".")
		extension = "." + list[len(list) - 1]
		print(f"extension is: {extension}")
		return extension


	#get Files from input Directory and return a list of 
	#Absolute filepaths
	def GetInputFiles(self):
		inputDirFileList = os.listdir(self.AbsoluteInputPath)
		AbsInputFiles = []
		for	entry in inputDirFileList:
			entry = os.path.join(self.AbsoluteInputPath, entry )
			if not os.path.isfile(entry): continue
			AbsInputFiles.append(entry)
		return AbsInputFiles

	def renameAndMoveFile(self, AbsFileInput,name,episode,season,extension):
			try:
				outputPath = os.path.join(self.AbsoluteOutputPath,f"./{name}/{season}")

				if not os.path.exists(outputPath):
					os.makedirs(outputPath,exist_ok=True)

				newFileName = os.path.join(
					outputPath,
					self.JellyfinStyle.format(name=name,episode=episode,season=season,extension=extension)
				)
				os.rename(AbsFileInput,newFileName)# moves file to new directory with new name
				print("file renamed")
				return newFileName
			except IsADirectoryError:
				print(f"[WARNING] can't rename file into directory {AbsFileInput}")
			except NotADirectoryError:
				print("[WANING] source is directory but destination is a file")
			except PermissionError:
				print(f"[WANING] file permission error while renaming file:{AbsFileInput}")
			except FileExistsError:
				print(f"[WANING] we somehow got the same file more than once!! file: {AbsFileInput}")
				os.rename(AbsFileInput,newFileName+".notRealExtension")



if __name__ == "__main__":
	rn = renamer()
	rn.main()