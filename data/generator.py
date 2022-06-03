from random import randint
from utility.parsers.writer import XmlWriter

import names


class XmlGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_xml_file(count_of_students):
        path = 'D:/Ppvis_lab2_sem4/data/excellent.xml'
        data_dict = {}
        with open(path, 'w') as file:
            writer = XmlWriter(path)
            for _ in range(count_of_students):
                surname = ' ' + names.get_last_name()
                data_dict['name'] = names.get_first_name() + surname
                data_dict['father_name'] = names.get_first_name('male') + surname
                data_dict['father_wage'] = randint(50, 1000)
                data_dict['mother_name'] = names.get_first_name('female') + surname
                data_dict['mother_wage'] = randint(50, 1000)
                data_dict['brothers_number'] = randint(0, 8)
                data_dict['sisters_number'] = randint(0, 8)
                writer.create_xml_student(data_dict)
        writer.create_xml_file()


def main():
    XmlGenerator.generate_xml_file(40)


if __name__ == "__main__":
    main()
