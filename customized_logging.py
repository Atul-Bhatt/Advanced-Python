# demonstrate the use of customized logging
import logging


def anotherFunction():
    logging.debug("This is another function.")


def main():
    # TODO: define the format string
    frmtstr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
    datestr = "%m/%d/%Y %I:%M:%S %p"

    # TODO: set the basicConfig default level
    logging.basicConfig(level=logging.DEBUG,
                        filename='output_comtomized.log',
                        filemode='w',
                        format=frmtstr,
                        datefmt=datestr)

    # TODO: print the log messages
    logging.debug("This is a debug message.")
    logging.info("This is an info message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")
    logging.critical("This is a critical message.")
    anotherFunction()


if __name__ == '__main__':
    main()
