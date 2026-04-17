from matplotlib.colors import LinearSegmentedColormap

nanoanalysis_bright = LinearSegmentedColormap.from_list('nanoanalysis_bright',['#B50E0E', '#FF8E00', "#F6F93A", "#0080FF", \
                                                               "#452ABE", "#DE46AE"])

nanoanalysis_muted = LinearSegmentedColormap.from_list('nanoanalysis_muted',["#BD2020", "#EDC430", "#2FAC55" , \
                                                               "#2F95AC", "#352FAC", "#B63896"])

nanoanalysis_hazy = LinearSegmentedColormap.from_list('nanoanalysis_hazy',["#EA4A4A", "#EFD267", "#5BDD82" , \
                                                               "#67D5EE", "#5F66E9", "#E484CC"])
