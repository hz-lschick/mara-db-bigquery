from mara_db.dbs import DB

class BigQueryDB(DB):
    def __init__(self, location: str = None, project: str = None, dataset: str = None):
        """
        Connection information for Google Big Query

        location: Default geographic location to use when creating datasets or determining where jobs should run
        project: Default project to use for requests.
        dataset: Default dataset reference to use for requests. (this is equal to the dataset in Big Query)

        """
        self.location = location
        self.project = project
        self.dataset = dataset
