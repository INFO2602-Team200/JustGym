# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .exerciseData import exerciseData_views

views = [user_views, index_views, exerciseData_views ] 
# blueprints must be added to this list