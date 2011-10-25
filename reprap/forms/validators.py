from colander import Invalid

def commaSpaceSeparatedListFactory(num):
    """Returns a validator that checks for a certain number of separated items in a list"""
    
    def commaSpaceSeparatedList(node, value):
        """ Checks to make sure that the value is a comma/space separated list """
        try:
            if ' ' in value:
                values = value.split(' ')
                if not len(values) >= num:
                    raise Exception
            elif ',' in value:
                values = value.split(',')
                if not len(values) >= num:
                    raise Exception
            elif ', ' in value:
                values = value.split(', ')
                if not len(values) >= num:
                    raise Exception
            else:
                if value != "":
                    return
                raise Exception
        except Exception:
            raise Invalid(node,
                          "Please enter a comma/space separated list of %d items." % num)
    
    return commaSpaceSeparatedList