# from pandas import DataFrame
# from sklearn.ensemble import RandomForestClassifier
# import pickle
class Machine:

    def __init__(self, df):
        pass

    def __call__(self, feature_basis):
        pass

    def save(self, filepath):
        pass

    @staticmethod
    def open(filepath):
        pass

    def info(self):
        pass

# class Machine:
#     def __init__(self, df):
#         """
#         Initialize the object with a pandas DataFrame.
#         """
#         self.df = df

#     def __call__(self, feature_basis):
#         """
#         Allow the object to be called like a function.
#         feature_basis should be a tuple: (x, y, target)
#         """
#         x, y, target = feature_basis

#         return self.chart(x, y, target)

#     def save(self, filepath):
#         """
#         Save the most recently generated chart to the given filepath.
#         File type is inferred from the extension:
#         html → saves as HTML
#         png  → saves as PNG
#         svg  → saves as SVG
#         """
#         if not hasattr(self, "last_chart") or self.last_chart is None:
#         raise ValueError("No chart has been generated yet.")

#         ext = filepath.lower().split(".")[-1]

#         if ext == "html":
#         self.last_chart.save(filepath)
#         elif ext in ("png", "svg"):
#         self.last_chart.save(filepath)
#     else:
#         raise ValueError("Unsupported file format. Use .html, .png, or .svg.")

#     @staticmethod
#     def open(filepath):
#         """
#    Loads a saved Chart object from a pickle file.
#    """
    

#     with open(filepath, "rb") as f:
#         obj = pickle.load(f)

#     return obj

#     def info(self):
#         """
#     Prints a summary of the chart's underlying DataFrame and 
#     any stored chart configuration.
#     """
#     print("=== Chart Information ===")
#     print(f"DataFrame shape: {self.df.shape}")
#     print("\nColumns:")
#     for col in self.df.columns:
#         print(f" - {col} (dtype: {self.df[col].dtype})")

#     print("\nDataFrame .info():")
#     print(self.df.info())

#     # If the chart stores additional configuration, list it.
#     cfg = getattr(self, "config", None)
#     if cfg:
#         print("\nChart Configuration:")
#         for k, v in cfg.items():
#             print(f" - {k}: {v}")
