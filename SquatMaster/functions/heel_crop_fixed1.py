def heel_crop_fixed(points, frame, frame_count_trim, aspect_ratio, yminus_factor, size_factor, height_fixed):
    
    x_coords, y_coords = zip(*points)

    img_height, img_width, _ = frame.shape

    min_x = int(round(min(x_coords),5) *img_width)
    max_x = int(round(max(x_coords),5) *img_width)
    min_y = int(round(min(y_coords),5) *img_height)
    max_y = int(round(max(y_coords),5) *img_height)

    height = max_y - min_y
    center_x = (min_x + max_x) / 2
    distance_below_min_y = int(height * yminus_factor)
    height_fixed = int(height_fixed * size_factor)
    width = int(height_fixed * aspect_ratio)

    new_min_x = int(center_x - width/2)
    new_max_x = int(center_x + width/2)
    new_min_y = int(min_y - distance_below_min_y)
    new_max_y = int(new_min_y + height_fixed)

    # print('min_y = ', min_y)
    # print('new_min_y = ', new_min_y)

    # new_min_x = max(new_min_x, 0)
    # new_min_y = max(new_min_y, 0)
    # new_max_x = min(new_max_x, 100)
    # new_max_y = min(new_max_y, 100)

    # if (new_min_x >= new_max_x or new_min_y >= new_max_y or (new_max_x - new_min_x) / (new_max_y - new_min_y) != aspect_ratio):
    #     print('Cannot preserve aspect ratio')
    #     return

    image_trimmed = frame[new_min_y:new_max_y, new_min_x:new_max_x]
    frame_count_trim += 1

    return image_trimmed, frame_count_trim, height