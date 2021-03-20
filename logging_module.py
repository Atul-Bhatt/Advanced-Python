# demonstrade the use of five logging functions
import logging


def main():
    # TODO: set the basicConfig level and save into a file
    logging.basicConfig(level=logging.DEBUG, filename="output.log")

    # TODO: use all five logging methods
    logging.debug("This is a debug message.")
    logging.info("This is just an info.")
    logging.warning("This is just a warning.")
    logging.error("This is an error.")
    logging.critical("This is a critical error.")


if __name__ == '__main__':
    main()
