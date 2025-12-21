from datetime import datetime
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

class Machine:
    """
    Machine Learning interface for monster rarity prediction.
    Uses Random Forest Classifier to predict monster rarity based on attributes.
    """
    
    def __init__(self, df: DataFrame):
        """
        Initialize the machine learning model with training data.
        
        Args:
            df (DataFrame): DataFrame containing monster data with features and target
        """
        self.name = "Random Forest Classifier"
        self.timestamp = datetime.now()
        
        # Prepare target and features
        target = df["Rarity"]
        features = df[["Level", "Health", "Energy", "Sanity"]]
        
        # Encode target variable
        self.label_encoder = LabelEncoder()
        target_encoded = self.label_encoder.fit_transform(target)
        
        # Initialize and train the model
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(features, target_encoded)
        
        # Store feature names for reference
        self.feature_names = features.columns.tolist()
    
    def __call__(self, pred_basis: DataFrame) -> tuple:
        """
        Make predictions on new data.
        
        Args:
            pred_basis (DataFrame): DataFrame containing feature data for prediction
            
        Returns:
            tuple: (prediction, confidence) where prediction is the predicted rarity
                   and confidence is the probability of the prediction
        """
        # Ensure we have the correct features
        features = pred_basis[self.feature_names]
        
        # Make prediction
        prediction_encoded = self.model.predict(features)
        prediction = self.label_encoder.inverse_transform(prediction_encoded)[0]
        
        # Get prediction probability
        probabilities = self.model.predict_proba(features)
        max_prob_index = prediction_encoded[0]
        confidence = probabilities[0][max_prob_index]
        
        return prediction, confidence
    
    def save(self, filepath: str) -> None:
        """
        Save the trained model to a file using joblib.
        
        Args:
            filepath (str): Path where to save the model
        """
        model_data = {
            'model': self.model,
            'label_encoder': self.label_encoder,
            'feature_names': self.feature_names,
            'name': self.name,
            'timestamp': self.timestamp
        }
        joblib.dump(model_data, filepath)
    
    @staticmethod
    def open(filepath: str) -> 'Machine':
        """
        Load a saved model from a file using joblib.
        
        Args:
            filepath (str): Path to the saved model file
            
        Returns:
            Machine: Loaded machine learning model instance
        """
        model_data = joblib.load(filepath)
        
        # Create a new instance
        instance = Machine.__new__(Machine)
        
        # Restore attributes
        instance.model = model_data['model']
        instance.label_encoder = model_data['label_encoder']
        instance.feature_names = model_data['feature_names']
        instance.name = model_data['name']
        instance.timestamp = model_data['timestamp']
        
        return instance
    
    def info(self) -> str:
        """
        Get information about the model.
        
        Returns:
            str: String containing model name and initialization timestamp
        """
        return f"{self.name} initialized at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"