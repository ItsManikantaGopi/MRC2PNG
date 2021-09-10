import numpy as np
import mrcfile as mrc
import matplotlib.pyplot as plt
from tqdm import tqdm
import warnings
warnings.simplefilter('ignore')
# to mute some warnings produced when opening the tomos
class MRC2PNG:
	"""
	class to convert MRC file to PNG
	"""
	def __init__(self,mrc_file,particle_locations,\
		starting_image_number,no_of_images,destination_path):
		self.mrc_data = MRC2PNG.Load_data_from_mrc_file(mrc_file)
		self.particle_locations = MRC2PNG.Load_particle_locations(particle_locations)
		self.starting_image_number = starting_image_number
		self.no_of_images = no_of_images
		self.destination_path = destination_path
	def run(self):
		"""
		method for begining conversion
		"""
		self.get_some_random_subtomograms(self.mrc__data,self.particle_locations\
			,self.no_of_images,self.destination_path,\
			self.starting_image_number,self.subtomo_size)

	@staticmethod
	def Load_data_from_mrc_file(mrc_file):
		"""
		method to load data from mrc_file
		and return that data
		"""
		with mrc.open(mrc_file, permissive=True) as file_:
			gt_data = file_.data
		return get_data
	@staticmethod
	def Load_particle_locations(particle_locations_text_file):
		"""
		method to load locations of the particles in mrc files 
		using the text files given for locations
		"""
		locations = []
		with open(particle_locations_text_file, 'rU') as f:
			for line in f:
				pdb_id, X, Y, Z, *_ = line.rstrip('\n').split()
				locations.append((pdb_id, int(float(X)), int(float(Y)), int(float(Z))))
		return locations
	@staticmethod
	def check_dirs_and_create(destination_path):
		"""
		method to check whether the mask and normal
		folders are there in destintion path or not
		"""
		if not os.path.exists(destination_path):
			os.mkdirs(destination_path)
	@staticmethod
	def get_coordinates(mrc_data,locations,subtomo_size):
		"""
		method to get coordinates of subtomo grams from the
		tomograms with given size and locations
		"""
		# find random location from ground txt truth file
		l = locations[np.random.choice(len(locations))]
	    # calculate figure XYZ corners
	    loc_x = int(float(l[1])) - (subtomo_size//2), int(float(l[1])) + (subtomo_size//2)
	    loc_y = int(float(l[2])) - (subtomo_size//2), int(float(l[2])) + (subtomo_size//2)
	    loc_z = int(float(l[3]))
	    # rec dimensions are 512x512x512, while ground truth is 512x512x200
	    # check if full subtomo_size x subtomo_size square figure can be plotted
	    if not((loc_x[0] < 0 or loc_y[0] < 0) or (loc_x[1] > \
	        mrc_data.shape[2] or loc_y[1] > mrc_data.shape[1])):
	    return (fits,loc_x,loc_y,loc_z)
	@staticmethod
	def get_some_random_subtomograms(mrc__data,locations,no_of_images,\
		destination_path,starting_image_number=0,subtomo_size=64):
	  """
	  method to convert mrc_data to png files
	  """
	  # saving P random 64x64 subtomograms into figure
	  check_dirs_and_create(destination_path)
	  for i in tqdm(range(no_of_images),desc = "creating_images"):
	      # finding plotting coordinates for central slice of a subtomogram of i-th subtomogram
	      # that fits to specified size
	      fits = False
	      while not fits:
	          fits,loc_x,loc_y,loc_z = get_coordinates(mrc_data,locations,subtomo_size)
	      # load reconstruction and ground truths
	      png = mrc_data[loc_z, loc_y[0]:loc_y[1], loc_x[0]:loc_x[1]]
	      # plot them into figure
	      plt.imsave(destination_path+f'/{starting_number+i}.png',png)
