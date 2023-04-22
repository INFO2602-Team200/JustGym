# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .exerciseData import exerciseData_views
from .userData import userData_views
from .workout import workout_views
from .community import community_views

views = [user_views, index_views, exerciseData_views,userData_views, workout_views, community_views ] 
# blueprints must be added to this list