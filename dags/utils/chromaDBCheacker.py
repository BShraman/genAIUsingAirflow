from chromadb import Client
import chromadb
from chromadb.config import Settings

class ChromaDBChecker:
    """
    A class to check if a specific collection exists in ChromaDB.
    """

    def __init__(self, collection_name = "", persist_directory="/opt/chromadb"):
        """
        Initialize the ChromaDBChecker with the directory for ChromaDB persistence.

        Args:
            persist_directory (str): Path to the directory where ChromaDB collections are stored.
        """
        # Initialize the client

        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection_name = collection_name
        

    def check_collection_exists(self, create_class_task_id: str, class_already_exists_task_id: str):
        """
        Checks if a collection (class) exists in ChromaDB.

        Args:
            collection_name (str): The name of the collection to check.

        Returns:
            dict: A dictionary with 'class_exists' (1 for exists, 0 for not exists).
        """

        try:
            collection = self.client.get_collection(name=self.collection_name)
            return class_already_exists_task_id
        except Exception:
            pass
        return create_class_task_id
        