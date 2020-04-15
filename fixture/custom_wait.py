

class there_is_window_other_than(object):

    def __init__(self, old_windows):
        self.old_windows = old_windows

    def __call__(self, wd):
        handles = wd.window_handles
        new = [x for x in handles if x not in self.old_windows]
        if len(new) > 0:
            return new[0]
        else:
            return False