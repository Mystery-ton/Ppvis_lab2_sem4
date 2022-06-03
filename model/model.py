import re
import sys

from utility.parsers.reader import XmlReader
from utility.parsers.writer import XmlWriter


class ModelComponent:
    _not_filtered = []

    def __init__(self, table):
        self.table = table

    def read_data(self, path):
        try:
            handler = XmlReader()
            handler.parser.setContentHandler(handler)
            url = 'D:/Ppvis_lab2_sem4/data/' + path
            handler.parser.parse(url)

            for data in handler.table_data:
                self.add_new_student(data)
        except Exception as e:
            print(e)
            pass

    @staticmethod
    def create_empty_file(path):
        try:
            with open(path, 'w'):
                pass
            return True
        except Exception as e:
            return False

    def write_data_to_file(self, path: str):
        path = 'D:/Ppvis_lab2_sem4/data/' + path
        if self.create_empty_file(path):
            dom = XmlWriter(path)
            data_dict = {}
            for row in self.table.row_data:
                data_dict['name'] = row[0]
                data_dict['father_name'] = row[1]
                data_dict['father_wage'] = row[2]
                data_dict['mother_name'] = row[3]
                data_dict['mother_wage'] = row[4]
                data_dict['brothers_number'] = row[5]
                data_dict['sisters_number'] = row[6]
                dom.create_xml_student(data_dict)

            dom.create_xml_file()

    def add_new_student(self, row):
        try:

            self.table.row_data.insert(
                len(self.table.row_data),
                (
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                )
            )
        except ValueError as v:
            pass

    @staticmethod
    def get_second_name(name: str):
        return name.split()[1]

    @staticmethod
    def get_first_name(name: str):
        return name.split()[0]

    def refresh_students(self):
        try:
            self.table.row_data += self._not_filtered
        except ValueError as v:
            pass

        self._not_filtered = []

    def select_students(self, filters: list):
        selected_students = []

        for row in self.table.row_data:
            # search by first name
            if filters[0]:
                first_name = self.get_first_name(row[0])
                filter_first_name = filters[0]
                if first_name != filter_first_name:
                    selected_students.append(tuple(row))

            # search by last name
            if filters[1]:
                last_name = self.get_second_name(row[0])
                filter_last_name = filters[1]
                if last_name != filter_last_name:
                    selected_students.append(tuple(row))

            # search by parent first name
            if filters[2]:
                parents_names = (self.get_first_name(row[1]), self.get_first_name(row[3]))
                filter_first_name = filters[2]
                if filter_first_name not in parents_names:
                    selected_students.append(tuple(row))

            # search by parent last name
            if filters[3]:
                parents_surnames = (self.get_second_name(row[1]), self.get_second_name(row[3]))
                filter_last_name = filters[3]
                if filter_last_name not in parents_surnames:
                    selected_students.append(tuple(row))

            # search by number of brothers/sisters
            if filters[4]:
                if row[5] != filters[4] and row[6] != filters[4]:
                    selected_students.append(tuple(row))

            # boundaries search
            # must be updated
            upper = None
            lower = None
            if filters[5]:
                try:
                    lower = int(filters[5])
                except Exception as e:
                    pass

            if filters[6]:
                try:
                    upper = int(filters[6])
                except Exception as e:
                    pass

            father_wage = int(row[2])
            mother_wage = int(row[4])

            if upper and lower:
                if (lower > father_wage or father_wage > upper) and (lower > mother_wage or mother_wage > upper):
                    selected_students.append(tuple(row))

            elif lower:
                if lower > father_wage and lower > mother_wage:
                    selected_students.append(tuple(row))

            elif upper:
                if upper < father_wage and upper < mother_wage:
                    selected_students.append(tuple(row))

        return selected_students

    def filter_students(self, filters: list):
        self._not_filtered = self.select_students(filters=filters)
        for row in self._not_filtered:
            try:
                self.table.row_data.remove(row)
            except Exception as e:
                pass

    @staticmethod
    def empty_filters(filters):
        for filt in filters:
            if filt != '':
                return False

        return True

    def delete_students(self, filters):
        deleted_count = 0
        if self.empty_filters(filters):
            return deleted_count
        students = self.select_students(filters=filters)
        for row in self.table.row_data[:]:
            if row not in students:
                try:
                    self.table.row_data.remove(row)
                    deleted_count += 1
                except Exception as e:
                    pass
        return deleted_count
