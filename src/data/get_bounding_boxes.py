
## Reference: https://learnopencv.com/classification-with-localization/

def extract_mat_contents(annot_directory, image_directory):

    # create MAT parser

    mat = scipy.io.loadmat(annot_directory)

    # Get the height and width for our image

    height, width = cv2.imread(image_directory).shape[:2]

    # Get the bounding box coordinates

    x1, y2, y1, x2 = tuple(map(tuple, mat['box_coord']))[0]

    filename = image_directory.split('/')[1]

    # Return the extracted attributes
    return filename, width, height, x1,y1,x2,y2



# Function to convert MAT files to CSV
def mat_to_csv(image_dir, annot_dir):

    # List containing all our attributes regarding each image
    mat_list = []


    # Get each file in the image and annotation directory
    mat_files = sorted(os.listdir(annot_dir))
    img_files = sorted(os.listdir(image_dir))

    # Loop over each of the image and its label
    for mat, image_file in zip(mat_files, img_files):

        # Full mat path
        mat_path = os.path.join(annot_dir, mat)

        # Full path Image
        img_path = os.path.join(image_dir, image_file)

        # Get Attributes for each image
        value = extract_mat_contents(mat_path, img_path)

        # Append the attributes to the mat_list
        mat_list.append(value)

    # Columns for Pandas DataFrame
    column_name = ['filename', 'width', 'height', 'xmin', 'ymin', 'xmax', 'ymax']

    # Create the DataFrame from mat_list
    mat_df = pd.DataFrame(mat_list, columns = column_name)

    # Return the dataframe
    return mat_df


if __name__ == '__main__':

    #import the necessary packages
    import os
    import scipy.io
    import cv2
    import pandas as pd


    ANNOTS_MAT_DIR = "annotations"
    IMAGES_DIR = "images"
    ANNOTS_PATH = "airplanes.csv"

    # Run the function to convert all the MAT files to a Pandas DataFrame
    labels_df = mat_to_csv(image_dir = IMAGES_DIR, annot_dir = ANNOTS_MAT_DIR)

    labels_df.drop(['width', 'height'], axis = 1, inplace = True)

    # Saving the Pandas DataFrame as CSV File
    labels_df.to_csv((ANNOTS_PATH), index = None, header = False)
