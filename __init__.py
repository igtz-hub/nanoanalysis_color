import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, Normalize
import matplotlib.cm as cm

custom1_cmap = LinearSegmentedColormap.from_list('nanoanalysis_bright',['#B50E0E', '#FF8E00', "#F6F93A", "#0080FF", \
                                                               "#452ABE", "#DE46AE"])

custom2_cmap = LinearSegmentedColormap.from_list('nanoanalysis_muted',['#CE0000', '#FF8E00', "#0080FF", \
                                                               "#BA008B"])

custom3_cmap = LinearSegmentedColormap.from_list('nanoanalysis_hazy',["#DA4F4F", "#8BF371", "#71B2F3", \
                                                               "#745BE7", "#EA83C9"])


plt.register_cmap(name = 'nanoanalysis_bright', cmap=custom1_cmap)
plt.register_cmap(name = 'nanoanalysis_muted', cmap=custom2_cmap)
plt.register_cmap(name = 'nanoanalysis_hazy', cmap=custom3_cmap)
