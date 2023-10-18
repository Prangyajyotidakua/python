def surface_area_of_cuboid(dimensions):
    if len(dimensions) != 3:
        raise ValueError("Dimensions should be a list of length, width, and height.")
    
    length, width, height = dimensions

    # Calculate the surface area of the cuboid
    surface_area = 2 * (length * width + width * height + height * length)

    return surface_area

# Example usage:
dimensions = [4, 3, 5]  # Length, Width, Height
surface_area = surface_area_of_cuboid(dimensions)
print("Surface Area of Cuboid:", surface_area)
