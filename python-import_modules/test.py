""" example to demonstrate how imports will skip the __name__ == "__main__" """

import test_import as t

result: int = t.add(1, 2)
print(result)
print(123)
