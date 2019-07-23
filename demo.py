import os

from ocr_utils import detect, get_logger
from trans_utils import translate

if __name__ == "__main__":
    logger = get_logger()

    file_path_name = 'images/example-1.jpg'
    logger.info('filename: ' + file_path_name)
    results = detect(file_path_name)
    print(results)

    for ret in results:
        dst = translate(ret['words'])
        print(ret['words'])
        print(dst)



