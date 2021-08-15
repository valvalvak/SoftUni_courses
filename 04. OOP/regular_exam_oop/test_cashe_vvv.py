class CasheV:
    def __init__(self, name: str):
        self.name = name
        pass

    @staticmethod
    def get_obj_form_list(obj, obj_list, clue: str):
        got_obj = [ob for ob in obj_list if obj.name == clue]
        return got_obj
