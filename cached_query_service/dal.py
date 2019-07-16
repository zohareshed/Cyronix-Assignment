import os

FILE_START_OFFSET_FLAG = 0


class DBNotFoundError(Exception):
    pass


class BinaryDAL(object):
    def __init__(self, db_path):
        if not os.path.exists(db_path):
            raise DBNotFoundError(f"The db does not exist in the path: {db_path}")
        self.db_path = db_path

    def get_data(self, offset: int, data_length: int) -> bytes:
        """
        If the offset is bigger than the db, or the length is - the function will return b''
        :param offset:
        :param data_length:
        :return:
        """
        with open(self.db_path, 'rb') as f:
            f.seek(offset, FILE_START_OFFSET_FLAG)
            return f.read(data_length)
