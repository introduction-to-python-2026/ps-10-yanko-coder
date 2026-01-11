seal_image = load_image('/content/Screenshot 2025-05-13 073842.png')
clean_seal_image = median(seal_image, ball(3))
edge_image = edge_detection(clean_seal_image)
binary = (edge_image > 80).astype(np.uint8)
