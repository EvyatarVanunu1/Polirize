import dataclasses


class MagicList(list):

    def __init__(self, data_cls=None, *args, **kwargs):
        if not dataclasses.is_dataclass(data_cls):
            raise TypeError(f'data_cls should be a dataclass')
        elif not isinstance(data_cls, type):
            raise TypeError(f'data_cls should be a dataclass and not an instance of one')

        super().__init__(*args, **kwargs)
        self.data_cls = data_cls

    def __getitem__(self, item):
        # when trying to access the next available index in the list and the data_cls is specified
        if self.data_cls and len(self) == item:
            self.append(self.data_cls())
            return self[item]

        return super().__getitem__(item)

    def __setitem__(self, key, value):
        # when trying to set the next available index in the list
        if len(self) == key:
            self.append(value)
        else:
            super().__setitem__(key, value)


