# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

from preprocessing import DataProcessor
import os


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    preprocessor = DataProcessor()

    logger.info('setting up the paths')
    image_dir = os.path.sep.join([input_filepath, "images"])
    annot_dir = os.path.sep.join([input_filepath, "annotations"])
    csv_path = os.path.sep.join([output_filepath, "airplanes.csv"])

    logger.info('reading and processing data')
    preprocessor.read_process_data(image_dir, annot_dir)

    logger.info('saving processed data')
    preprocessor.write_data(csv_path)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
