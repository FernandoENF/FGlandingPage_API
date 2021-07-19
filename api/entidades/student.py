class Student:
    def __init__(self, name, email, telephone, recommended_by, code):
        self.__name = name
        self.__email = email
        self.__telephone = telephone
        self.__recommended_by = recommended_by
        self.__code = code

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def telephone(self):
        return self.__telephone

    @telephone.setter
    def telephone(self, telephone):
        self.__telephone = telephone

    @property
    def recommended_by(self):
        return self.__recommended_by

    @recommended_by.setter
    def recommended_by(self, recommended_by):
        self.__recommended_by = recommended_by

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code):
        self.__code = code

