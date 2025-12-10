from os import getenv
from certifi import where
from dotenv import load_dotenv
from BloomtechMonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient

class Database:
    """
    Database interface for MongoDB operations with MonsterLab data.
    Handles seeding, resetting, counting, and data retrieval operations.
    """
    
    load_dotenv()
    database = MongoClient(getenv("MONGO_URL"), tlsCAFile=where())["Database"]
    
    def __init__(self, collection: str = "monsters"):
        """
        Initialize database connection to specified collection.
        
        Args:
            collection (str): Name of the MongoDB collection
        """
        self.collection = self.database[collection]

    def seed(self, amount: int) -> bool:
        """
        Seed the collection with specified number of monster documents.
        
        Args:
            amount (int): Number of monster documents to create
            
        Returns:
            bool: True if seeding was successful
        """
        monsters = [Monster().to_dict() for _ in range(amount)]
        return self.collection.insert_many(monsters).acknowledged

    def reset(self) -> bool:
        """
        Delete all documents from the collection.
        
        Returns:
            bool: True if reset was successful
        """
        return self.collection.delete_many({}).acknowledged

    def count(self) -> int:
        """
        Count the number of documents in the collection.
        
        Returns:
            int: Number of documents in the collection
        """
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        """
        Retrieve all documents as a pandas DataFrame.
        
        Returns:
            DataFrame: DataFrame containing all collection documents
        """
        documents = list(self.collection.find({}, {"_id": False}))
        return DataFrame(documents) if documents else DataFrame()
    
    def html_table(self) -> str:
        """
        Generate HTML table representation of the collection data.
        
        Returns:
            str: HTML table string, or None if collection is empty
        """
        df = self.dataframe()
        if df.empty:
            return None
        return df.to_html(classes="table table-striped", index=False)
    
if __name__ == "__main__":
    db = Database()
    db.reset()
    db.seed(1000)
    