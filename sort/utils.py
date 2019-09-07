
class SortingException(Exception):
    """ General sorting exception """


def validate_input_collection(collection):
    """ checks if the input collection list consists of elements of same type
        :param collection: list of input element
        :return: returns true if all elements of collections are of same type
            else false
    """
    if not collection:
        return True

    element_type = type(collection[0])
    return all(isinstance(x, element_type) for x in collection)


