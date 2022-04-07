#import the necessary packages
import os
import scipy.io
import cv2
import pandas as pd


class DataProcessor:
    """
    Class for reading, processing and writing data from the
    .mat annotation files.
    """

    def __init__(self):
        self.column_names = ['filename', 'width', 'height', 'xmin', 'ymin', 'xmax', 'ymax']
        self.processed_data = pd.DataFrame()

    @staticmethod
    def extract_mat_contents( annot_directory, image_directory):
        """
        create MAT parser.
        """

        mat = scipy.io.loadmat(annot_directory)

        # Get the height and width for our image

        height, width = cv2.imread(image_directory).shape[:2]

        # Get the bounding box coordinates

        x1, y2, y1, x2 = tuple(map(tuple, mat['box_coord']))[0]

        filename = image_directory.split('/')[3]

        # Return the extracted attributes
        return filename, width, height, x1,y1,x2,y2



    def read_process_data(self, image_dir, annot_dir):
        """
        Process raw data into useful useful format for model.
        """

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
            value = self.extract_mat_contents(mat_path, img_path)

            # Append the attributes to the mat_list
            mat_list.append(value)


        # Create the DataFrame from mat_list
        self.processed_data = pd.DataFrame(mat_list, columns = self.column_names)
        self.processed_data.drop(['width', 'height'], axis = 1, inplace = True)



    def write_data(self, processed_data_path):
        """
        Save processed data to directory.
        """
        # Saving the Pandas DataFrame as CSV File
        self.processed_data.to_csv(processed_data_path, index = None, header = False)
