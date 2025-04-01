

import os
import json

theTopScript = "top_script.py"

def export_campaignSynthesis(campaign_data):
    if not isinstance(campaign_data, dict):
        raise ValueError("Invalid campaign data")

    file_name = theTopScript
    if os.path.exists(file_name):
        raise FileExistsError("File already exists")

    try:
        with open(file_name, "w") as f:
            json.dump(campaign_data, f)
    except Exception as e:
        raise IOError("Failed to write to file") from e

    return os.path.abspath(file_name)