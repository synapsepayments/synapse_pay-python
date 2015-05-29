import inspect
import re
import string

class PathBuilder(object):
    class PathTemplate(string.Template):
        delimiter = ':'

    @classmethod 
    def build(cls, obj, params, path_template):
    	# Take a path like:
	    #   ":path/:id/dogs/:dog_id"
	    # and convert it to:
	    #   "#{object.path}/#{object.id}/dogs/#{params[:id]}" => "/objects/1/dogs/2"
	    #
	    # Path priority is:
	    #   1. Object - this will be a class or an instance of a class.
	    #   2. Params - this is a hash of key values. All keys *must* be symbolized.

        path = path_template
        if hasattr(obj, 'api_attributes') and not inspect.isclass(obj):
            attributes = obj.api_attributes()
            path = PathBuilder.PathTemplate(path).safe_substitute(**attributes)
        if not params:
            params = {}
        path = PathBuilder.PathTemplate(path).safe_substitute(**params)

        remaining = [m.start() for m in re.finditer(r':', path)]
        if len(remaining):
            raise ValueError("The template path (%s) can not be properly created from the provided object and params." % path)
        return path 

