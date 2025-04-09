

package system_features

class SystemFeatures:
    def __init__(self):
        self.features = {
            "feature1": "This is feature 1",
            "feature2": "This is feature 2",
            "feature3": "This is feature 3"
        }

    def get_features(self):
        return self.features

    def add_feature(self, feature_name, feature_description):
        if not isinstance(feature_name, str) or not isinstance(feature_description, str):
            raise ValueError("Feature name and description must be strings")
        if not feature_name or not feature_description:
            raise ValueError("Feature name and description cannot be empty")
        try:
            self.features[feature_name] = feature_description
        except Exception as e:
            raise Exception(f"Failed to add feature: {str(e)}")

    def remove_feature(self, feature_name):
        if not isinstance(feature_name, str):
            raise ValueError("Feature name must be a string")
        if not feature_name:
            raise ValueError("Feature name cannot be empty")
        try:
            if feature_name in self.features:
                del self.features[feature_name]
        except Exception as e:
            raise Exception(f"Failed to remove feature: {str(e)}")

    def update_feature(self, feature_name, feature_description):
        if not isinstance(feature_name, str) or not isinstance(feature_description, str):
            raise ValueError("Feature name and description must be strings")
        if not feature_name or not feature_description:
            raise ValueError("Feature name and description cannot be empty")
        try:
            if feature_name in self.features:
                self.features[feature_name] = feature_description
        except Exception as e:
            raise Exception(f"Failed to update feature: {str(e)}")