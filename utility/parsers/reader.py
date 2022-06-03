import xml.sax as sax


class XmlReader(sax.ContentHandler):
    def __init__(self) -> None:
        super().__init__()
        self.table_data = []
        self.student_data = []
        self.parser = sax.make_parser()

    # attrs??
    # what a method??
    def startElement(self, name, attrs):
        self.current = name
        if name == 'student':
            pass

    def characters(self, content):
        if self.current == 'name':
            self.name = content
        elif self.current == 'father_name':
            self.father_name = content
        elif self.current == 'father_wage':
            self.father_wage = content
        elif self.current == 'mother_name':
            self.mother_name = content
        elif self.current == 'mother_wage':
            self.mother_wage = content
        elif self.current == 'brothers_number':
            self.brothers_number = content
        elif self.current == 'sisters_number':
            self.sisters_number = content

    def endElement(self, name):
        if self.current == 'name':
            self.student_data.append(self.name)
        elif self.current == 'father_name':
            self.student_data.append(self.father_name)
        elif self.current == 'father_wage':
            self.student_data.append(self.father_wage)
        elif self.current == 'mother_name':
            self.student_data.append(self.mother_name)
        elif self.current == 'mother_wage':
            self.student_data.append(self.mother_wage)
        elif self.current == 'brothers_number':
            self.student_data.append(self.brothers_number)
        elif self.current == 'sisters_number':
            self.student_data.append(self.sisters_number)

        if len(self.student_data) == 7:
            self.table_data.append(tuple(self.student_data))
            self.student_data = []

        self.current = ''
